# Checkmate MNQ — Quantitative Research & Validation

**Independent portfolio research project | systematic futures research | not a live trading product**

> **Research status (November 2026):** Checkmate is a rules-driven, session-aware research system for Micro E-mini Nasdaq-100 (MNQ) futures using 1-minute market data. Its methodology includes historical backtesting, execution-cost stress tests, exit behavior investigation, and risk/telemetry analysis. Historical strategy reports are **simulated**. Broker-tracked observation spans approximately **one month at most** and is not an independently audited track record. A reproducibility investigation remains open. No investment results or statistical edge are claimed by this repository.

This repository is a **public-safe, reproducible Python research companion**, **not** the proprietary TradingView/Pine Script strategy, Checkmate AI agentic program-management tool, or a broker execution system. It deliberately does not publish strategy entries, exits, alpha signals, account details, raw proprietary research exports, or private broker data.

## What can be demonstrated now?

- Parse TradingView **List of Trades** CSV exports, which can record an exit before its entry in the exported file.
- Count each **exit leg once** (not both the entry and exit rows) when calculating historical reporting metrics.
- Compute net P&L, win rate, profit factor, worst day, losing days, and **closed-leg equity drawdown**.
- Compare independently supplied normal-cost and harsh-cost export files, with file hashes, first mismatched records, and cost sensitivity.
- Use deterministic synthetic fixtures and automated tests so reviewers can run the toolkit **without access to proprietary code or data**.
- Document validation limitations, missing controls, and a reproducibility gate.

**Not demonstrated:** execution of or parity with the original Pine engine, a statistically established trading edge, production-ready order routing, exchange-quality tick data, consistent full-year reproducibility, or audited forward returns.

## Quick start (Python 3.10+)

```bash
python -m unittest discover -s tests -v
python -m checkmate_quant.cli summary examples/synthetic_normal.csv
python -m checkmate_quant.cli compare examples/synthetic_normal.csv examples/synthetic_harsh.csv
```

To analyze a private export **locally**, without committing the file:

```bash
mkdir -p data/private
# Save your own TradingView List of Trades files in data/private/.
python -m checkmate_quant.cli summary data/private/your_own_export.csv --json
python -m checkmate_quant.cli compare data/private/normal.csv data/private/harsh.csv --json
```

This is a reporting/validation aid: it reads TradingView-computed results. It **does not independently reproduce an order book, exchange fills, or the proprietary strategy**.

## Architecture

```text
Private TradingView/Pine strategy  ──────┐
  (NEVER in this public repository)      │
                                        ▼
                              Private CSV exports
                                        │
                                        ▼
                              CSV parsing + hashing
                                        │
                          ┌─────────────┴─────────────┐
                          ▼                           ▼
                   Performance summary         Normal / harsh diff
                          │                           │
                          └─────────────┬─────────────┘
                                        ▼
                            Local research review
                            (no orders or execution)
```

For validation methodology, see [docs/VALIDATION_PROTOCOL.md](docs/VALIDATION_PROTOCOL.md). For career relevance, see [docs/HIRING_PORTFOLIO.md](docs/HIRING_PORTFOLIO.md).

## Limitations and definitions

- Monetary figures, transaction costs, and equity metrics come from the TradingView CSV; the tool does not reconstruct independent fills.
- **Closed-leg drawdown** uses reported closed exits only. It is **not** maximum intraday open-equity drawdown, margin risk, or realized brokerage-account drawdown.
- CSV timestamps are used in their **exported clock** for date bucketing. The code makes no unsupported UTC or Eastern Time conversion.
- Profit factor is total positive exit-leg net P&L divided by absolute total negative exit-leg net P&L; it is undefined with no losses.
- For TradingView row formats, this tool assumes one exit row represents one closed leg, as documented in the test fixtures. Confirm broker parity independently.
- Matching by trade number and exit timestamp is a diagnostic only; differences in source runs, chart properties, market-data adjustments, or trade ordering can require manual investigation.
- Synthetic fixtures have **invented** values and are not Checkmate performance reports.

## Public/private boundary

| Public here | Keep private |
|---|---|
| README, architecture, reproducibility methodology | Frozen Pine strategy/source and regime/exit parameters |
| Python CSV analysis utility and tests | Raw TradingView signals and complete exports |
| Synthetic fixtures | Broker credentials, API tokens, positions, account IDs |
| Research limitations and roadmap | Proprietary alerts, source mappings and executable trade rules |

This repository does **not** grant permission to reproduce the private Checkmate trading strategy. No open-source license is provided; all rights reserved unless an explicit license is added later.

## Roadmap

Read [docs/ROADMAP.md](docs/ROADMAP.md) for current P0–P3 gates and [docs/SKILL_BUILDING_PLAN.md](docs/SKILL_BUILDING_PLAN.md) for the 12-week practical curriculum. Contributions and claims must be measured against the published test suite and explicit reproducibility criteria.
