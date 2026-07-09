# FICC Rates Bond Quant Demo

FICC Rates Bond Quant Demo is an educational Python project for fixed-income
interest-rate bond analytics.

It focuses on the core mechanics of rates-bond quant work:

```text
bond cash flows
-> bond pricing
-> Macaulay duration
-> modified duration
-> convexity
-> rate-cut / rate-hike scenario
-> PnL estimation
-> multi-maturity comparison
```

This is a public-safe GitHub project. It uses simplified examples and synthetic
inputs to demonstrate the mechanics, not proprietary trading views.

## Why This Project Exists

Interest-rate bonds are one of the most important areas in FICC. Before talking
about strategy, portfolio construction, or AI research agents, we need a clean
understanding of:

- how coupon bond prices are computed
- why bond prices move opposite to yields
- why duration approximates first-order rate sensitivity
- why convexity matters for larger rate moves
- why long-maturity bonds are more sensitive to rate changes
- how portfolio PnL responds to rate-cut and rate-hike scenarios

This repo turns those ideas into a small, runnable Python demo.

## Repository Structure

```text
ficc-rates-bond-quant-demo/
├─ README.md
├─ pyproject.toml
├─ src/ficc_rates_bond_quant/
│  ├─ __init__.py
│  ├─ bond_math.py
│  ├─ pnl.py
│  ├─ scenarios.py
│  └─ portfolio.py
├─ tests/
├─ demos/
├─ notes/
├─ assets/
├─ docs/
└─ outputs/
```

## Quick Start

Run the demo:

```powershell
$env:PYTHONPATH = "src"
py demos/run_demo.py
```

Run tests:

```powershell
$env:PYTHONPATH = "src"
py -m unittest discover -s tests
```

## What The Demo Shows

The demo compares 1Y, 3Y, 5Y, 10Y, and 30Y coupon bonds under:

```text
10bp rate cut
10bp rate hike
50bp rate cut
50bp rate hike
```

It estimates:

```text
price
Macaulay duration
modified duration
convexity
estimated price change
estimated portfolio PnL
```

## Example Interpretation

A long-duration bond has higher interest-rate sensitivity.

For the same rate cut:

```text
30Y bond price impact > 10Y bond price impact > 1Y bond price impact
```

A rate cut usually increases bond prices, while a rate hike usually decreases
bond prices.

Convexity improves the approximation when the yield move becomes larger.

## Educational Scope

This project covers:

```text
interest-rate bonds
cash-flow discounting
bond pricing
Macaulay duration
modified duration
convexity
yield-change scenario analysis
portfolio PnL estimation
multi-maturity comparison
```

It does not cover:

```text
credit bonds
default risk
derivatives
swaps
options
high-frequency trading
live trading
real portfolio optimization
```

## Public-Safe Boundary

This repo does not include:

- proprietary bank materials
- internal research documents
- client information
- real trading positions
- private market views
- live trading instructions

## Positioning

This is a research-engineering project, not a trading system.

Defensible claim:

```text
I built an educational FICC rates bond quant demo that implements bond pricing,
duration, convexity, rate-shock scenarios, PnL estimation, and multi-maturity
comparison in Python.
```

Do not claim:

```text
production rates trading system
live bond portfolio optimizer
bank internal research engine
validated real-money strategy
```

## Notes

See:

- `notes/ficc_rates_intro.md`
- `notes/duration_convexity.md`
- `docs/system_design.md`
- `docs/public_private_boundary.md`

## License / Copyright

© 2026 Pengyi Peng. All rights reserved unless otherwise specified.
