"""
Author: Viktoriia Denys
Program: coupon_calculations.py
This program accepts the amount of the purchase,the cash coupon,
the percent coupon and it will calculate and return the total order item
"""

import unittest
from store import coupon_calculations as coupon


class MyTestCase(unittest.TestCase):

    # under_ten

    def test_under_ten_coupon1(self):
        self.assertAlmostEqual(9.77, coupon.calculate_price(9.00, 5, 10), 2)

    def test_under_ten_coupon2(self):
        self.assertAlmostEqual(6.84, coupon.calculate_price(5.99, 5, 15), 2)

    def test_under_ten_coupon3(self):
        self.assertAlmostEqual(9.30, coupon.calculate_price(8.95, 5, 20), 2)

    def test_under_ten_coupon4(self):
        self.assertAlmostEqual(4.04, coupon.calculate_price(8.00, 10, 10), 2)

    def test_under_ten_coupon5(self):
        self.assertAlmostEqual(5.72, coupon.calculate_price(9.75, 10, 15), 2)

    def test_under_ten_coupon6(self):
        self.assertAlmostEqual(3.98, coupon.calculate_price(7.68, 10, 20), 2)

    # between_ten_thirty
    def test_price_between_ten_thirty1(self):
        self.assertAlmostEqual(27.03, coupon.calculate_price(25.00, 5, 10), 2)

    def test_price_between_ten_thirty2(self):
        self.assertAlmostEqual(25.97, coupon.calculate_price(25.00, 5, 15), 2)

    def test_price_between_ten_thirty3(self):
        self.assertAlmostEqual(24.91, coupon.calculate_price(25.00, 5, 20), 2)

    def test_price_between_ten_thirty4(self):
        self.assertAlmostEqual(22.26, coupon.calculate_price(25.00, 10, 10), 2)

    def test_price_between_ten_thirty5(self):
        self.assertAlmostEqual(21.47, coupon.calculate_price(25.00, 10, 15), 2)

    def test_price_between_ten_thirty6(self):
        self.assertAlmostEqual(20.67, coupon.calculate_price(25.00, 10, 20), 2)

    # between_thirty_fifty

    def test_price_between_thirty_fifty1(self):
        self.assertAlmostEqual(53.93, coupon.calculate_price(49.00, 5, 10), 2)

    def test_price_between_thirty_fifty2(self):
        self.assertAlmostEqual(51.59, coupon.calculate_price(49.00, 5, 15), 2)

    def test_price_between_thirty_fifty3(self):
        self.assertAlmostEqual(49.26, coupon.calculate_price(49.00, 5, 20), 2)

    def test_price_between_thirty_fifty4(self):
        self.assertAlmostEqual(49.16, coupon.calculate_price(49.00, 10, 10), 2)

    def test_price_between_thirty_fifty5(self):
        self.assertAlmostEqual(47.09, coupon.calculate_price(49.00, 10, 15), 2)

    def test_price_between_thirty_fifty6(self):
        self.assertAlmostEqual(45.02, coupon.calculate_price(49.00, 10, 20), 2)

    # over_fifty

    def test_price_over_fifty1(self):
        self.assertAlmostEqual(66.78, coupon.calculate_price(75.00, 5, 10), 2)

    def test_price_over_fifty2(self):
        self.assertAlmostEqual(63.07, coupon.calculate_price(75.00, 5, 15), 2)

    def test_price_over_fifty3(self):
        self.assertAlmostEqual(59.36, coupon.calculate_price(75.00, 5, 20), 2)

    def test_price_over_fifty4(self):
        self.assertAlmostEqual(62.01, coupon.calculate_price(75.00, 10, 10), 2)

    def test_price_over_fifty5(self):
        self.assertAlmostEqual(58.56, coupon.calculate_price(75.00, 10, 15), 2)

    def test_price_over_fifty6(self):
        self.assertAlmostEqual(55.12, coupon.calculate_price(75.00, 10, 20), 2)


if __name__ == '__main__':
    unittest.main()


"""
In this program, I wrote a  function that accepts the amount of the purchase,
 the cash coupon,the percent coupon 
 and it  calculates and return the total order item. All tests provided above passed
"""