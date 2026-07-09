# System Design: FICC Rates Bond Research OS

## 1. Design Goal

The goal is to build a small but real research workflow for interest-rate bond
analysis.

The system should answer:

```text
Given a macro / rates event and a yield curve snapshot,
what scenario are we in,
what research hypothesis does it imply,
what risk should a human reviewer check,
and what report should be produced?
```

This is not an auto-trading system. It is a research assistant and report
generation workflow.

## 2. Target Use Case

The first use case is interest-rate bond research.

Examples:

- government bonds
- policy bank bonds
- local government bonds
- interest-rate swaps / repo rate context in later versions

The MVP starts with generic rates-bond reasoning and synthetic data. It should
not depend on proprietary datasets.

## 3. High-Level Architecture

```text
                 +----------------------+
                 | synthetic event data |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 |   event classifier   |
                 +----------+-----------+
                            |
                            v
+----------------------+    +----------------------+    +----------------------+
| yield curve snapshot | -> | curve state analyzer | -> | scenario classifier  |
+----------------------+    +----------------------+    +----------+-----------+
                                                               |
                                                               v
                                                    +----------------------+
                                                    | hypothesis generator |
                                                    +----------+-----------+
                                                               |
                                                               v
                                                    +----------------------+
                                                    | risk checklist       |
                                                    +----------+-----------+
                                                               |
                                                               v
                                                    +----------------------+
                                                    | markdown report      |
                                                    +----------------------+
```

## 4. Core Data Contracts

### 4.1 RatesEvent

Represents a macro / FICC event.

Fields:

```text
date
time
source
event_type
text
country_or_market
confidence
```

Example event types:

```text
central_bank
liquidity
inflation
growth
fiscal_policy
bond_supply
risk_sentiment
regulatory
```

### 4.2 YieldCurveSnapshot

Represents the current yield curve.

Fields:

```text
date
tenor
yield_bps
change_1d_bps
change_5d_bps
change_20d_bps
```

MVP tenors:

```text
1Y
3Y
5Y
7Y
10Y
30Y
```

### 4.3 CurveState

Derived from `YieldCurveSnapshot`.

Fields:

```text
level
slope_10y_1y
slope_10y_3y
curvature_10y_5y_1y
parallel_move_bps
slope_move_bps
curvature_move_bps
```

### 4.4 Scenario

Classifies curve movement.

Core scenarios:

```text
bull_steepener
bull_flattener
bear_steepener
bear_flattener
parallel_rally
parallel_selloff
range_bound
mixed_signal
```

### 4.5 SignalHypothesis

Not a trading command. A human-reviewable research hypothesis.

Fields:

```text
directional_view
curve_view
duration_bias
instrument_focus
reasoning
confidence
required_checks
```

### 4.6 RiskChecklist

Human reviewer checklist.

Fields:

```text
duration_risk
convexity_risk
liquidity_risk
policy_event_risk
supply_event_risk
data_quality_risk
model_simplification_risk
```

## 5. Module Design

Planned source package:

```text
src/ficc_rates_os/
```

### contracts.py

Purpose:

```text
Define data classes and validation helpers.
```

Objects:

```text
RatesEvent
YieldCurvePoint
YieldCurveSnapshot
CurveState
RatesScenario
SignalHypothesis
RiskChecklist
ResearchReport
```

### taxonomy.py

Purpose:

```text
Map event text into FICC / rates taxonomy.
```

MVP implementation:

```text
keyword-based classifier
```

Later:

```text
LLM-assisted classifier with citation and human review
```

### curve.py

Purpose:

```text
Build curve state from yield points.
```

Functions:

```text
parse_yield_curve_csv
compute_curve_state
compute_level_slope_curvature
```

### scenario.py

Purpose:

```text
Classify curve movement into rates scenarios.
```

Examples:

```text
front-end rally + long-end stable -> bull steepener
long-end selloff + front-end stable -> bear steepener
all tenors lower -> parallel rally
all tenors higher -> parallel selloff
```

### hypothesis.py

Purpose:

```text
Generate human-reviewable research hypotheses.
```

Examples:

```text
duration bias: cautious long duration
curve view: steepening risk
instrument focus: 5Y-10Y government bond curve
```

Important:

```text
The output is a hypothesis, not investment advice.
```

### risk.py

Purpose:

```text
Attach risk checklist to every hypothesis.
```

MVP risks:

```text
duration
convexity
liquidity
supply
policy
data quality
model simplification
```

### report.py

Purpose:

```text
Generate markdown report for human review.
```

Report sections:

```text
event summary
curve snapshot
curve state
scenario classification
signal hypothesis
risk checklist
human review questions
public-safe disclaimer
```

### pipeline.py

Purpose:

```text
Coordinate the end-to-end workflow.
```

Pipeline:

```text
load event
load curve
classify event
compute curve state
classify scenario
generate hypothesis
build risk checklist
write report
```

### cli.py

Purpose:

```text
Expose the workflow as a command-line demo.
```

Example:

```powershell
$env:PYTHONPATH = "src"
py -m ficc_rates_os.cli examples/sample_rates_events.csv examples/sample_yield_curve.csv --out outputs/sample_rates_report.md
```

## 6. MVP Input / Output

### 6.1 Input: sample_rates_events.csv

```text
date,time,source,text
2026-07-09,09:00,synthetic,"Central bank signals stable liquidity and moderate growth pressure."
```

### 6.2 Input: sample_yield_curve.csv

```text
date,tenor,yield_bps,change_1d_bps,change_5d_bps,change_20d_bps
2026-07-09,1Y,165,-2,-6,-10
2026-07-09,3Y,180,-3,-8,-14
2026-07-09,5Y,195,-4,-10,-18
2026-07-09,10Y,215,-6,-14,-22
2026-07-09,30Y,245,-5,-10,-15
```

### 6.3 Output: sample_rates_report.md

```text
# FICC Rates Research Report

## Event
...

## Curve State
...

## Scenario
parallel_rally / bull_flattener / ...

## Hypothesis
...

## Risk Checklist
...

## Human Review
...
```

## 7. System Design Principles

### Principle 1: Public-Safe First

No private source data, no internal bank logic, no client information.

### Principle 2: Research Before Trading

The system produces hypotheses and reports, not direct trading instructions.

### Principle 3: Human Review Is Mandatory

Every hypothesis must include:

```text
confidence
risk checklist
review questions
boundary note
```

### Principle 4: Data Contracts Over Ad Hoc Strings

Even in the MVP, event, curve, scenario, hypothesis, and report should have
clear schemas.

### Principle 5: Small Runnable Demo

The first public version should be simple enough to run in one command.

## 8. Relationship To Existing FICC Work

Existing public repo:

```text
ficc-event-signal-workflow
```

Position:

```text
macro / FICC event -> signal hypothesis
```

This repo:

```text
rates event + yield curve state -> rates scenario -> bond research hypothesis
```

Difference:

```text
ficc-event-signal-workflow is general FICC event-to-signal.
ficc-rates-bond-research-os is rates-bond specific and curve-aware.
```

## 9. Future Extensions

### v1: Runnable MVP

```text
synthetic CSV input
curve state
scenario classifier
hypothesis generator
risk checklist
markdown report
unit tests
```

### v2: Curve Analytics

```text
DV01
duration
convexity
carry
roll-down
```

### v3: RAG / Report Assistant

```text
public policy text
public macro notes
RAG citation
research memo generation
```

### v4: AI Harness

```text
task contract
tool policy
data policy
review checkpoint
audit log
```

## 10. Interview Narrative

Chinese:

```text
我设计了一个 public-safe 的利率债研究 OS。它不是实盘交易系统，而是把宏观/利率事件、收益率曲线状态、情景分类、研究假设和风险检查串成一个可复核的研究工作流。核心训练的是 FICC rates 里的 curve thinking、duration risk、scenario reasoning 和 human-in-the-loop research engineering。
```

English:

```text
I designed a public-safe FICC rates bond research OS. It is not a live trading
system. It connects macro/rates events, yield curve states, scenario
classification, research hypotheses, and risk checklists into a reviewable
research workflow. The core value is combining rates curve thinking, duration
risk, scenario reasoning, and human-in-the-loop research engineering.
```
