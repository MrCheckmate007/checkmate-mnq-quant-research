# Architecture and responsibility boundaries

**Separate projects:** Checkmate MNQ is a rules-driven quantitative futures research system. The separately maintained **Checkmate AI** repository concerns agentic enterprise program decision support, not trading.

Private strategy research is conducted in TradingView/Pine with historical data and session-aware risk controls. Optional execution adapters are outside this repository. This public Python package intentionally cannot produce trading signals or place orders. It supports documentation and independent review of **exported ledger math**.

## Modules

1. `ledger.py`: bytes SHA-256 and type-aware CSV reader; exit-first export handling.
2. `metrics.py`: closed-leg financial metrics and export-clock daily aggregates.
3. `compare.py`: ordinal diagnostics between scenarios and comparison of reported figures.
4. `cli.py`: local-only terminal interface.
5. `tests/`: synthetic fixture checks.

## Trust boundary

TradingView exports are **reports** rather than tick-level ground truth. Matching hashes show identical bytes, not independently repeated computations. Report-based drawdown omits open-equity troughs. The proprietary exit module, entry engine, risk gates, and live order orchestrator are not reproduced here.
