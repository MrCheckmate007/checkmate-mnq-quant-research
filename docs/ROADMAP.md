# Learning and engineering roadmap

## P0 — Start here

- [x] Create public-safe research package and README
- [x] Parse exported closed legs without double-counting entry rows
- [x] Create synthetic tests and CI
- [x] Compare stressed and normal exported ledgers
- [ ] Finish H25 source/CSV reproducibility gate (A/B/C/D) before claiming parity
- [ ] Add actual private report profile with missing-column and session-clock audit

## P1 — Quant research engineering

- [ ] pandas/NumPy notebook: serial correlation, rolling volatility, returns, and leg attribution
- [ ] Statistical tests and block bootstrap for daily results
- [ ] Walk-forward research with purged and time-ordered splits where relevant
- [ ] Monte Carlo sensitivity to regime, costs, and losing streaks
- [ ] Extend reporting to separate open-equity/intraday drawdown once appropriate data exists

## P2 — Trading systems knowledge

- [ ] Build a synthetic FIX order lifecycle demo with acknowledgements/fills/cancels
- [ ] Simulate market data gaps, stale prices and order reconciliation
- [ ] Introduce Docker, static analysis, type checking, and metrics instrumentation

## P3 — Proof for interviews

- [ ] Document a full research question, initial hypothesis, test plan, failed tests and decisions
- [ ] Publish one anonymized benchmark report with methodology and limitations
- [ ] Prepare architecture tradeoff walkthrough for an institutional trading TPM panel
