"""Portfolio and multi-maturity comparison helpers."""

from __future__ import annotations

from dataclasses import dataclass

from .bond_math import bond_price, convexity, macaulay_duration, modified_duration
from .pnl import estimate_position_pnl
from .scenarios import RateScenario, rate_cut


@dataclass(frozen=True)
class BondPosition:
    """A simple fixed-rate bond position."""

    name: str
    maturity_years: float
    coupon_rate: float
    yield_to_maturity: float
    notional_face_value: float
    face_value: float = 100.0
    frequency: int = 2


def analyze_position(position: BondPosition, scenario: RateScenario) -> dict[str, float | str]:
    """Analyze one bond position under one yield-shift scenario."""

    price = bond_price(
        position.face_value,
        position.coupon_rate,
        position.yield_to_maturity,
        position.maturity_years,
        position.frequency,
    )
    mac_dur = macaulay_duration(
        position.face_value,
        position.coupon_rate,
        position.yield_to_maturity,
        position.maturity_years,
        position.frequency,
    )
    mod_dur = modified_duration(
        position.face_value,
        position.coupon_rate,
        position.yield_to_maturity,
        position.maturity_years,
        position.frequency,
    )
    conv = convexity(
        position.face_value,
        position.coupon_rate,
        position.yield_to_maturity,
        position.maturity_years,
        position.frequency,
    )
    pnl = estimate_position_pnl(
        price=price,
        face_value=position.face_value,
        notional_face_value=position.notional_face_value,
        modified_duration_value=mod_dur,
        convexity_value=conv,
        yield_change=scenario.yield_change,
    )
    return {
        "name": position.name,
        "scenario": scenario.name,
        "maturity_years": position.maturity_years,
        "price": price,
        "macaulay_duration": mac_dur,
        "modified_duration": mod_dur,
        "convexity": conv,
        **pnl,
    }


def compare_maturities(
    maturities: list[float] | None = None,
    coupon_rate: float = 0.025,
    yield_to_maturity: float = 0.025,
    notional_face_value: float = 1_000_000_000.0,
    scenario: RateScenario | None = None,
) -> list[dict[str, float | str]]:
    """Compare rate sensitivity across maturities."""

    if maturities is None:
        maturities = [1, 3, 5, 10, 30]
    if scenario is None:
        scenario = rate_cut(10)

    rows: list[dict[str, float | str]] = []
    for maturity in maturities:
        position = BondPosition(
            name=f"{maturity:g}Y bond",
            maturity_years=float(maturity),
            coupon_rate=coupon_rate,
            yield_to_maturity=yield_to_maturity,
            notional_face_value=notional_face_value,
        )
        rows.append(analyze_position(position, scenario))
    return rows
