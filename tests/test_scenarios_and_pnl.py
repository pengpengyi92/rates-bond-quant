import unittest

from ficc_rates_bond_quant import (
    BondPosition,
    analyze_position,
    compare_maturities,
    rate_cut,
    rate_hike,
)


class TestScenariosAndPnl(unittest.TestCase):
    def test_rate_cut_increases_price(self):
        position = BondPosition("10Y", 10, 0.025, 0.025, 1_000_000)
        result = analyze_position(position, rate_cut(10))
        self.assertGreater(result["price_change"], 0)
        self.assertGreater(result["pnl"], 0)

    def test_rate_hike_decreases_price(self):
        position = BondPosition("10Y", 10, 0.025, 0.025, 1_000_000)
        result = analyze_position(position, rate_hike(10))
        self.assertLess(result["price_change"], 0)
        self.assertLess(result["pnl"], 0)

    def test_longer_maturity_has_higher_duration(self):
        rows = compare_maturities(maturities=[1, 30], scenario=rate_cut(10))
        self.assertGreater(rows[1]["modified_duration"], rows[0]["modified_duration"])


if __name__ == "__main__":
    unittest.main()
