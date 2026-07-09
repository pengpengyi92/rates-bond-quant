"""Interest-rate shock scenarios."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RateScenario:
    """A parallel yield-shift scenario."""

    name: str
    yield_change: float
    description: str

    @property
    def bp(self) -> float:
        """Yield change in basis points."""

        return self.yield_change * 10_000


def parallel_shift(bp: float, name: str | None = None) -> RateScenario:
    """Create a parallel yield shift scenario from basis points."""

    yield_change = bp / 10_000
    if name is None:
        direction = "rate hike" if bp > 0 else "rate cut"
        name = f"{abs(bp):.0f}bp {direction}"
    return RateScenario(
        name=name,
        yield_change=yield_change,
        description="Parallel yield curve shift for educational scenario analysis.",
    )


def rate_cut(bp: float = 10.0) -> RateScenario:
    """Create a rate-cut scenario."""

    if bp <= 0:
        raise ValueError("bp must be positive for rate_cut")
    return parallel_shift(-bp, name=f"{bp:.0f}bp rate cut")


def rate_hike(bp: float = 10.0) -> RateScenario:
    """Create a rate-hike scenario."""

    if bp <= 0:
        raise ValueError("bp must be positive for rate_hike")
    return parallel_shift(bp, name=f"{bp:.0f}bp rate hike")
