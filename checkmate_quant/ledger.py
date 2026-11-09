"""Read TradingView List of Trades CSV with exit-first/entry-second rows.

No strategy logic, signals, broker details, or data sources are bundled here.
"""
from __future__ import annotations
import csv
import hashlib
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path


@dataclass(frozen=True)
class ExitLeg:
    trade_number: str
    exit_time: str
    net_pnl: Decimal
    commission: Decimal
    favorable_excursion: Decimal
    adverse_excursion: Decimal
    exit_price: Decimal
    qty: Decimal
    direction: str


@dataclass(frozen=True)
class Ledger:
    source: Path
    sha256: str
    exits: tuple[ExitLeg, ...]
    row_count: int
    entry_count: int


def decimal_of(value: str | None, *, field: str) -> Decimal:
    s = (value or '').strip().replace(',', '').replace('$', '')
    if s.startswith('(') and s.endswith(')'):
        s = '-' + s[1:-1]
    try:
        number = Decimal(s)
    except (InvalidOperation, TypeError) as exc:
        raise ValueError(f'Invalid numeric field {field}: {value!r}') from exc
    if not number.is_finite():
        raise ValueError(f'Non-finite numeric field {field}: {value!r}')
    return number


def load_ledger(path: str | Path) -> Ledger:
    p = Path(path)
    raw = p.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    exits: list[ExitLeg] = []
    entry_count = 0
    row_count = 0
    required = {
        'Trade number', 'Type', 'Date and time', 'Net PnL USD',
        'Commission USD', 'Favorable excursion USD', 'Adverse excursion USD',
        'Price USD', 'Size (qty)',
    }
    with p.open('r', encoding='utf-8-sig', newline='') as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise ValueError('CSV header is missing')
        missing = required - set(reader.fieldnames)
        if missing:
            raise ValueError(f'Missing TradingView CSV columns: {sorted(missing)}')
        for i, row in enumerate(reader, start=2):
            row_count += 1
            kind = (row['Type'] or '').strip().lower()
            if kind.startswith('entry'):
                entry_count += 1
                continue
            if not kind.startswith('exit'):
                raise ValueError(f'Unexpected trade Type on CSV row {i}: {row["Type"]!r}')
            stamp = (row['Date and time'] or '').strip()
            if not stamp:
                raise ValueError(f'Missing date on CSV row {i}')
            exits.append(ExitLeg(
                trade_number=(row['Trade number'] or '').strip(),
                exit_time=stamp,
                net_pnl=decimal_of(row['Net PnL USD'], field='Net PnL USD'),
                commission=decimal_of(row['Commission USD'], field='Commission USD'),
                favorable_excursion=decimal_of(row['Favorable excursion USD'],field='Favorable excursion USD'),
                adverse_excursion=decimal_of(row['Adverse excursion USD'],field='Adverse excursion USD'),
                exit_price=decimal_of(row['Price USD'],field='Price USD'),
                qty=decimal_of(row['Size (qty)'],field='Size (qty)'),
                direction=kind,
            ))
    # Preserve stable file order for ties, but sort chronologically for drawdown.
    sorted_exits = tuple(sorted(exits, key=lambda leg: leg.exit_time))
    return Ledger(source=p, sha256=digest, exits=sorted_exits,
                  row_count=row_count, entry_count=entry_count)
