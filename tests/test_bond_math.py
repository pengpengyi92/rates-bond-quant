import unittest

from ficc_rates_bond_quant.bond_math import (
    bond_price,
    convexity,
    macaulay_duration,
    modified_duration,
)


class TestBondMath(unittest.TestCase):
    def test_zero_coupon_price(self):
        price = bond_price(
            face_value=100,
            coupon_rate=0,
            yield_to_maturity=0.05,
            maturity_years=2,
            frequency=1,
        )
        self.assertAlmostEqual(price, 100 / 1.05**2, places=8)

    def test_zero_coupon_macaulay_duration_equals_maturity(self):
        duration = macaulay_duration(
            face_value=100,
            coupon_rate=0,
            yield_to_maturity=0.05,
            maturity_years=2,
            frequency=1,
        )
        self.assertAlmostEqual(duration, 2.0, places=8)

    def test_modified_duration_formula(self):
        mac = macaulay_duration(100, 0.03, 0.04, 5, 2)
        mod = modified_duration(100, 0.03, 0.04, 5, 2)
        self.assertAlmostEqual(mod, mac / (1 + 0.04 / 2), places=10)

    def test_convexity_positive(self):
        self.assertGreater(convexity(100, 0.03, 0.04, 10, 2), 0)


if __name__ == "__main__":
    unittest.main()
