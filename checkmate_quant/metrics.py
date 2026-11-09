"""Descriptive *export-based* quantitative risk/performance statistics."""
from __future__ import annotations
from collections import defaultdict
from decimal import Decimal
from .ledger import Ledger


def summarize(ledger: Ledger) -> dict:
    exits = ledger.exits
    profits = sum((x.net_pnl for x in exits if x.net_pnl > 0), Decimal(0))
    losses = -sum((x.net_pnl for x in exits if x.net_pnl < 0), Decimal(0))
    net = sum((x.net_pnl for x in exits), Decimal(0))
    comm = sum((x.commission for x in exits), Decimal(0))
    equity = Decimal(0)
    peak = Decimal(0)
    max_closed_drawdown = Decimal(0)
    daily = defaultdict(lambda: Decimal(0))
    for leg in exits:
        equity += leg.net_pnl
        peak = max(peak, equity)
        max_closed_drawdown = max(max_closed_drawdown, peak - equity)
        daily[leg.exit_time[:10]] += leg.net_pnl
    winners = sum(x.net_pnl > 0 for x in exits)
    n = len(exits)
    return {
        'source_sha256': ledger.sha256,
        'csv_rows': ledger.row_count,
        'entry_rows': ledger.entry_count,
        'closed_exit_legs': n,
        'net_pnl_usd': str(net),
        'gross_profitable_legs_usd': str(profits),
        'absolute_gross_losing_legs_usd': str(losses),
        'profit_factor': str(profits / losses) if losses else None,
        'winning_leg_fraction': round(winners/n,6) if n else None,
        'recorded_commission_usd': str(comm),
        'max_closed_leg_drawdown_usd': str(max_closed_drawdown),
        'trading_days_in_export_clock': len(daily),
        'losing_days_in_export_clock': sum(p < 0 for p in daily.values()),
        'worst_day_usd': str(min(daily.values())) if daily else None,
        'worst_day_export_date': (min(daily,key=daily.get) if daily else None),
        'clock_note': 'Dates are based on unconverted CSV export timestamps',
        'evidence_note': 'TradingView-exported simulation/report values; not independently verified live fills',
    }
