import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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
