# MVP Plan

## Goal

Build the smallest runnable public-safe FICC rates bond research demo.

```text
synthetic event CSV
+ synthetic yield curve CSV
-> scenario classification
-> rates research hypothesis
-> risk checklist
-> markdown report
```

## Repository Tasks

### Step 1: Data Contracts

Create:

```text
src/ficc_rates_os/contracts.py
```

Objects:

```text
RatesEvent
YieldCurvePoint
CurveState
RatesScenario
SignalHypothesis
RiskChecklist
ResearchReport
```

### Step 2: Synthetic Examples

Create:

```text
examples/sample_rates_events.csv
examples/sample_yield_curve.csv
```

### Step 3: Curve Analyzer

Create:

```text
src/ficc_rates_os/curve.py
```

Functions:

```text
load_yield_curve
compute_level
compute_slope
compute_curvature
compute_curve_state
```

### Step 4: Scenario Classifier

Create:

```text
src/ficc_rates_os/scenario.py
```

Rules:

```text
parallel rally
parallel selloff
bull steepener
bull flattener
bear steepener
bear flattener
range bound
mixed signal
```

### Step 5: Hypothesis Generator

Create:

```text
src/ficc_rates_os/hypothesis.py
```

Output:

```text
duration bias
curve view
instrument focus
reasoning
confidence
```

### Step 6: Risk Checklist

Create:

```text
src/ficc_rates_os/risk.py
```

Checklist:

```text
duration risk
convexity risk
liquidity risk
supply risk
policy event risk
data quality risk
model simplification risk
```

### Step 7: Report Generator

Create:

```text
src/ficc_rates_os/report.py
```

Output:

```text
outputs/sample_rates_research_report.md
```

### Step 8: CLI

Create:

```text
src/ficc_rates_os/cli.py
```

Command:

```powershell
$env:PYTHONPATH = "src"
py -m ficc_rates_os.cli examples/sample_rates_events.csv examples/sample_yield_curve.csv --out outputs/sample_rates_research_report.md
```

### Step 9: Tests

Create:

```text
tests/test_curve.py
tests/test_scenario.py
tests/test_pipeline.py
```

Run:

```powershell
$env:PYTHONPATH = "src"
py -m unittest discover -s tests
```

## MVP Definition Of Done

The MVP is done when:

- CLI runs with sample files.
- A markdown report is generated.
- Tests pass.
- README explains the public/private boundary.
- No private data or employer material is included.

