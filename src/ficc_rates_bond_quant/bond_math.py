"""Core fixed-income math for coupon bonds.

The module uses simple deterministic formulas for educational purposes. It
assumes fixed coupons, flat yield-to-maturity, and discrete compounding.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Cashflow:
    """A dated cash flow represented by period index and time in years."""

    period: int
    time_years: float
    amount: float


def _validate_bond_inputs(
    face_value: float,
    coupon_rate: float,
    yield_to_maturity: float,
    maturity_years: float,
    frequency: int,
) -> None:
    if face_value <= 0:
        raise ValueError("face_value must be positive")
    if coupon_rate < 0:
        raise ValueError("coupon_rate cannot be negative")
    if yield_to_maturity <= -1:
        raise ValueError("yield_to_maturity must be greater than -100%")
    if maturity_years <= 0:
        raise ValueError("maturity_years must be positive")
    if frequency <= 0:
        raise ValueError("frequency must be positive")


def bond_cashflows(
    face_value: float = 100.0,
    coupon_rate: float = 0.03,
    maturity_years: float = 10.0,
    frequency: int = 2,
) -> list[Cashflow]:
    """Return fixed coupon bond cash flows."""

    if face_value <= 0:
        raise ValueError("face_value must be positive")
    if coupon_rate < 0:
        raise ValueError("coupon_rate cannot be negative")
    if maturity_years <= 0:
        raise ValueError("maturity_years must be positive")
    if frequency <= 0:
        raise ValueError("frequency must be positive")

    periods = int(round(maturity_years * frequency))
    if abs(periods / frequency - maturity_years) > 1e-9:
        raise ValueError("maturity_years must align with coupon frequency")

    coupon = face_value * coupon_rate / frequency
    flows: list[Cashflow] = []
    for period in range(1, periods + 1):
        amount = coupon
        if period == periods:
            amount += face_value
        flows.append(Cashflow(period=period, time_years=period / frequency, amount=amount))
    return flows


def bond_price(
    face_value: float = 100.0,
    coupon_rate: float = 0.03,
    yield_to_maturity: float = 0.03,
    maturity_years: float = 10.0,
    frequency: int = 2,
) -> float:
    """Price a fixed coupon bond with discrete compounding."""

    _validate_bond_inputs(
        face_value, coupon_rate, yield_to_maturity, maturity_years, frequency
    )
    discount_rate = yield_to_maturity / frequency
    return sum(
        cf.amount / (1.0 + discount_rate) ** cf.period
        for cf in bond_cashflows(face_value, coupon_rate, maturity_years, frequency)
    )


def macaulay_duration(
    face_value: float = 100.0,
    coupon_rate: float = 0.03,
    yield_to_maturity: float = 0.03,
    maturity_years: float = 10.0,
    frequency: int = 2,
) -> float:
    """Calculate Macaulay duration in years."""

    price = bond_price(
        face_value, coupon_rate, yield_to_maturity, maturity_years, frequency
    )
    discount_rate = yield_to_maturity / frequency
    weighted_pv = 0.0
    for cf in bond_cashflows(face_value, coupon_rate, maturity_years, frequency):
        pv = cf.amount / (1.0 + discount_rate) ** cf.period
        weighted_pv += cf.time_years * pv
    return weighted_pv / price


def modified_duration(
    face_value: float = 100.0,
    coupon_rate: float = 0.03,
    yield_to_maturity: float = 0.03,
    maturity_years: float = 10.0,
    frequency: int = 2,
) -> float:
    """Calculate modified duration in years."""

    mac_dur = macaulay_duration(
        face_value, coupon_rate, yield_to_maturity, maturity_years, frequency
    )
    return mac_dur / (1.0 + yield_to_maturity / frequency)


def convexity(
    face_value: float = 100.0,
    coupon_rate: float = 0.03,
    yield_to_maturity: float = 0.03,
    maturity_years: float = 10.0,
    frequency: int = 2,
) -> float:
    """Calculate standard discrete-compounding convexity in years squared."""

    price = bond_price(
        face_value, coupon_rate, yield_to_maturity, maturity_years, frequency
    )
    discount_rate = yield_to_maturity / frequency
    convexity_sum = 0.0
    for cf in bond_cashflows(face_value, coupon_rate, maturity_years, frequency):
        convexity_sum += (
            cf.amount
            * cf.period
            * (cf.period + 1)
            / (frequency**2)
            / (1.0 + discount_rate) ** (cf.period + 2)
        )
    return convexity_sum / price
