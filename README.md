# FICC Rates Bond Research OS

FICC Rates Bond Research OS is a public-safe research engineering demo for
interest-rate bond analysis, yield-curve scenario reasoning, and human-reviewed
FICC research workflows.

The first version focuses on system design:

```text
macro / rates event
-> rates taxonomy
-> yield curve state
-> scenario classification
-> signal hypothesis
-> risk checklist
-> reviewable research report
```

## Why This Project Exists

Interest-rate bond research is not just about predicting one yield number. A
useful research workflow should connect:

- macro events
- central bank and liquidity conditions
- bond supply and demand
- yield curve level / slope / curvature
- duration and convexity exposure
- carry / roll-down intuition
- risk and human review

This project turns that reasoning process into a small, inspectable, public-safe
engineering system.

## Public-Safe Boundary

This repository is designed for public portfolio use.

It will not contain:

- proprietary bank materials
- internal research documents
- client information
- private transaction records
- real position data
- confidential market views
- live trading instructions

The MVP will use synthetic examples and simplified public-domain-style data
schemas.

## Current Status

```text
v0: system design and repository architecture
```

See:

- `docs/system_design.md`
- `docs/public_private_boundary.md`
- `docs/mvp_plan.md`

## Planned Repository Structure

```text
ficc-rates-bond-research-os/
├─ README.md
├─ pyproject.toml
├─ examples/
│  ├─ sample_rates_events.csv
│  └─ sample_yield_curve.csv
├─ src/ficc_rates_os/
│  ├─ __init__.py
│  ├─ contracts.py
│  ├─ taxonomy.py
│  ├─ curve.py
│  ├─ scenario.py
│  ├─ hypothesis.py
│  ├─ risk.py
│  ├─ report.py
│  ├─ pipeline.py
│  └─ cli.py
├─ tests/
│  ├─ test_curve.py
│  ├─ test_scenario.py
│  └─ test_pipeline.py
└─ docs/
   ├─ system_design.md
   ├─ public_private_boundary.md
   └─ mvp_plan.md
```

## MVP Target

The first runnable version should produce:

```text
synthetic macro event
+ mock yield curve snapshot
+ scenario classification
+ rates signal hypothesis
+ risk checklist
+ markdown report
```

Example output:

```text
outputs/sample_rates_research_report.md
```

## Project Positioning

This is a research-engineering project, not a trading system.

Defensible claim:

```text
I designed and implemented a public-safe FICC rates research workflow that maps
macro/rates events and yield-curve states into scenario classifications,
candidate hypotheses, risk checks, and human-reviewable reports.
```

Do not claim:

```text
production rates trading system
live bond portfolio optimizer
bank internal research engine
validated real-money strategy
```

## License / Copyright

© 2026 Pengyi Peng. All rights reserved unless otherwise specified.
