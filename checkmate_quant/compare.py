"""Compare exported scenarios. Same counts do not imply true code parity."""
from __future__ import annotations
from decimal import Decimal
from .ledger import Ledger
from .metrics import summarize


def compare_ledgers(normal: Ledger, stressed: Ledger) -> dict:
    a = summarize(normal)
    b = summarize(stressed)
    mismatches = []
    for i, (left, right) in enumerate(zip(normal.exits, stressed.exits), 1):
        if left.trade_number != right.trade_number or left.exit_time != right.exit_time or left.direction != right.direction:
            mismatches.append({'ordinal': i, 'normal_trade_number': left.trade_number,
                               'stress_trade_number': right.trade_number,
                               'normal_exit_time': left.exit_time,
                               'stress_exit_time': right.exit_time})
    return {
        'normal_sha256': normal.sha256,
        'stress_sha256': stressed.sha256,
        'identical_file_bytes': normal.sha256 == stressed.sha256,
        'normal_closed_legs': len(normal.exits),
        'stress_closed_legs': len(stressed.exits),
        'closed_leg_count_difference': len(stressed.exits) - len(normal.exits),
        'matched_prefix_ordinal_count': min(len(normal.exits),len(stressed.exits)),
        'ordinal_identity_mismatches': len(mismatches),
        'first_ordinal_identity_mismatch': mismatches[0] if mismatches else None,
        'normal_net_pnl_usd': a['net_pnl_usd'],
        'stress_net_pnl_usd': b['net_pnl_usd'],
        'stress_minus_normal_net_usd': str(Decimal(b['net_pnl_usd'])-Decimal(a['net_pnl_usd'])),
        'normal_closed_leg_drawdown_usd': a['max_closed_leg_drawdown_usd'],
        'stress_closed_leg_drawdown_usd': b['max_closed_leg_drawdown_usd'],
        'interpretation_note': 'Ordinal matching is diagnostic only; independent source/chart/setting parity must be established separately',
    }
