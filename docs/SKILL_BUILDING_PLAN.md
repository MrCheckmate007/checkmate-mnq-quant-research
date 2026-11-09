# Quant finance skills — 12-week applied plan

**Objective:** transition from an enterprise AI/FinTech TPM background into credible trading technology TPM and investment platform roles, while building an independent quantitative research engineering portfolio. This program does **not** confer institutional trading experience.

| Weeks | Skill | Exercise | Acceptance evidence |
|---|---|---|---|
| 1–2 | Python/SQL, version control, typed data models | Read private TV reports locally, validate schema and duplicate fills, test input errors | Tests pass; CLI outputs and limitations documented; no private data committed |
| 3–4 | Probability/statistics | Compute expectancy, distribution of daily P&L, uncertainty by block bootstrap | Notebook with assumptions, confidence intervals, sample-size cautions |
| 5–6 | Backtest validity | Chronological out-of-sample split and walk-forward evaluation; holdout never optimized | Frozen run manifest and tests for date leakage; failed experiments documented |
| 7–8 | Market microstructure, FIX/OMS/EMS | Diagram order life cycle; implement dummy order messages using entirely synthetic data | Documented sequence of new order → acknowledgment → partial fill → cancel/reject; stale feed safety cases |
| 9–10 | Trading reliability engineering | Add a simulated data-feed monitor, retries, structured logs, test pipeline, Docker | Fault injection and incident runbook with recovery paths |
| 11–12 | Interviews and case-study storytelling | Explain Checkmate architecture, reproducibility failure, test design, tradeoffs and operational risk | 5-minute and 20-minute technical walkthroughs; clear research-vs-live disclaimer |

## Next five tickets (do in this order)

- [ ] **QNT-001** Finish immutable H25 source+settings A/B reproducibility with source SHA and all TradingView properties captured.
- [ ] **QNT-002** Extend CSV parser to pair entry/exit legs and emit first mismatch *without revealing signal comments*.
- [ ] **QNT-003** Add time-zone and session-day configuration (explicit exchange/export clock; no implicit conversions).
- [ ] **QNT-004** Implement block bootstrap on daily net returns; explain sample dependence.
- [ ] **QNT-005** Create public synthetic FIX/OMS order-state demonstration and a pre-trade risk checklist.

## Technical interview questions this portfolio should eventually answer

1. How do you know two export runs came from the same source, properties, inputs, and historical data?
2. How do cost assumptions and market conditions change the distribution of outcomes?
3. How do you prevent test leakage and explain deteriorating out-of-sample performance?
4. How would you detect stale or out-of-order market data before allowing trading?
5. How do order acknowledgments and broker fills reconcile with internal position state?
6. Why do closed-trade P&L and intraday open-equity drawdown differ?
7. How do you lead trading engineers, researchers, and risk stakeholders through a failed release?
