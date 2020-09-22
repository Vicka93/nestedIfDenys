import unittest
from store import coupon_calculations as coupon


class MyTestCase(unittest.TestCase):

    def test_under_ten_coupon1(self):
        self.assertAlmostEqual(9.77, coupon.calculate_price(9.00, 5, 10), 2)

    def test_under_ten_coupon2(self):
        self.assertAlmostEqual(6.84, coupon.calculate_price(5.99, 5, 15), 2)

    def test_under_ten_coupon3(self):
        self.assertAlmostEqual(9.30, coupon.calculate_price(8.95, 5, 20), 2)

    def test_under_ten_coupon4(self):
        self.assertAlmostEqual(5.95, coupon.calculate_price(8.00, 10, 10), 2)

    def test_under_ten_coupon5(self):
        self.assertAlmostEqual(5.95, coupon.calculate_price(9.00, 10, 15), 2)

    def test_under_ten_coupon6(self):
        self.assertAlmostEqual(5.95, coupon.calculate_price(10.00, 10, 20), 2)


if __name__ == '__main__':
    unittest.main()
