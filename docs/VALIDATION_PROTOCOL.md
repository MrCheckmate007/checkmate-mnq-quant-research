# P0 validation and reproducibility protocol

## Current evidence status (2026-11-08)

**PARTIALLY VERIFIED — H25 INVESTIGATION OPEN.** Prior internal audit identified byte-identical research exports. Matching SHA-256 hashes establish duplicate file content, not that the Pine strategy was rerun independently. Historical H25 annual-versus-short-window differences remain unresolved. The latest frozen production/control scripts must remain unchanged throughout the investigation. This public repo does not include those scripts.

## Required reproducibility gate

- [ ] A: original frozen H25 source and settings; same beginning and end dates; export CSV.
- [ ] B: rerun *without changing any settings or data window*; export CSV.
- [ ] Hash both full CSV files and compare every closed leg, timestamp, size, price, and outcome.
- [ ] C: same start, change only end date by one day; compare common fully closed positions, accounting for cutoff positions.
- [ ] D (diagnostic): same settings/end, change only start date; examine warmup and path dependence.
- [ ] Snapshot source SHA-256; Pine inputs, chart time zone, deep backtesting, commission, slippage, recalculation, external sources, margin, rollover and continuous contract settings.
- [ ] Establish holdout dates before optimization, not after observing results.
- [ ] Run cost stresses on the same source and date range, then compare differences.
- [ ] Reconcile broker fills and TradingView alerts separately for actual live history, with fill IDs and timestamps under **private storage**.

## Acceptance criteria

Identical A/B closed trade ledgers at entry and exit level; fully explained A/C boundary artifacts; disclosed D history sensitivity; no test leakage; costs specified; adverse cases preserved. Do not use improving annual simulated P&L to close the reproducibility gap.

## Additional research gates

- Chronological out-of-sample and walk-forward validation (with no same-period parameter selection).
- Market regime and session strata (Asian and European only; U.S. cash session is not a target).
- Confidence intervals or block-bootstrap estimates to reflect serial dependence.
- Study net expectancy and daily risk, not headline win rate or max favorable excursion alone.
- Conservative costs, slippage and anomalous/reversal session testing.
- No increase in live trading exposure based only on backtests.
