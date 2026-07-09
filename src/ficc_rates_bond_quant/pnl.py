"""Bond price-change and PnL estimation."""

from __future__ import annotations


def estimate_price_change(
    price: float,
    modified_duration_value: float,
    convexity_value: float,
    yield_change: float,
) -> dict[str, float]:
    """Estimate price impact from a yield change.

    Uses the duration-convexity approximation:

    dP / P ~= -D_mod * dy + 0.5 * Convexity * dy^2
    """

    if price <= 0:
        raise ValueError("price must be positive")

    relative_change = (
        -modified_duration_value * yield_change
        + 0.5 * convexity_value * yield_change**2
    )
    price_change = price * relative_change
    return {
        "relative_change": relative_change,
        "price_change": price_change,
        "new_price": price + price_change,
    }


def estimate_position_pnl(
    price: float,
    face_value: float,
    notional_face_value: float,
    modified_duration_value: float,
    convexity_value: float,
    yield_change: float,
) -> dict[str, float]:
    """Estimate PnL for a face-value notional position."""

    if face_value <= 0:
        raise ValueError("face_value must be positive")
    if notional_face_value == 0:
        raise ValueError("notional_face_value cannot be zero")

    price_impact = estimate_price_change(
        price, modified_duration_value, convexity_value, yield_change
    )
    units = notional_face_value / face_value
    pnl = units * price_impact["price_change"]
    market_value = units * price
    return {
        **price_impact,
        "market_value": market_value,
        "pnl": pnl,
        "pnl_bps_of_market_value": pnl / market_value * 10_000,
    }
