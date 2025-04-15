# https://github.com/ellianak/lab10-EK-JT
# Partner 1: Elliana Kirby
# Partner 2: Joseph Torchio

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5, 7), 12)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, 10), 5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5,7), -2)
        self.assertEqual(subtract(-2,-1), -1)
        self.assertEqual(subtract(10,3), 7)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 2),4)
        self.assertEqual(mul(-3, 4),-12)
        self.assertEqual(mul(-5, -7),35)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(2, 3),3/2)
        self.assertAlmostEqual(div(-4, -5),5/4)
        self.assertAlmostEqual(div(5, -4),-4/5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 0)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(32.0, 2.0), 5.0)
        self.assertAlmostEqual(logarithm(1000, 10), 3.0)
        self.assertAlmostEqual(logarithm(9, 3), 2.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, 0)
        with self.assertRaises(ValueError):
            logarithm(2, 1)
        with self.assertRaises(ValueError):
            logarithm(2, -1)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(4, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertTrue(hypotenuse(2, 2))
        self.assertTrue(hypotenuse(-3, 4))
        self.assertTrue(hypotenuse(-5, -7))

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        with self.assertRaises(ValueError):
            square_root(-4)
        # Test basic function
        self.assertTrue(square_root(2))
        self.assertTrue(square_root(4))
        self.assertTrue(square_root(99))
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
