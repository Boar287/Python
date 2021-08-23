#!usr/bin/env python3
from RationalNumber import RationalNumber
import unittest


class RationalNumberTest(unittest.TestCase):
    def test_init1(self):
        self.assertRaises(TypeError, RationalNumber, -3.45, 5.34)

    def test_init2(self):
        self.assertRaises(ValueError, RationalNumber, 4, 0)

    def test_add1(self):
        test_num1 = RationalNumber(1, 3)
        test_num2 = RationalNumber(2, 3)
        self.assertEqual(test_num1 + test_num2, 1)

    def test_add2(self):
        test_num1 = RationalNumber(7, 3)
        test_num2 = RationalNumber(2, 6)
        self.assertEqual(test_num1 + test_num2, RationalNumber(8, 3))

    def test_add3(self):
        test_num1 = RationalNumber(7, 3)
        test_num2 = 2
        self.assertEqual(test_num1 + test_num2, RationalNumber(13, 3))

    def test_add4(self):
        test_num1 = RationalNumber(-5, 3)
        test_num2 = RationalNumber(2, 3)
        self.assertEqual(test_num1 + test_num2, RationalNumber(-3, 3))

    def test_sub1(self):
        test_num1 = RationalNumber(8, 5)
        test_num2 = RationalNumber(3, 2)
        self.assertEqual(test_num1 - test_num2, RationalNumber(1, 10))

    def test_sub2(self):
        test_num1 = RationalNumber(4, 3)
        test_num2 = RationalNumber(1, 3)
        self.assertEqual(test_num1 - test_num2, 1)

    def test_sub3(self):
        test_num1 = RationalNumber(4, 3)
        test_num2 = 1
        self.assertEqual(test_num1 - test_num2, RationalNumber(1, 3))

    def test_sub4(self):
        test_num1 = RationalNumber(1, 3)
        test_num2 = RationalNumber(2, 3)
        self.assertEqual(test_num1 - test_num2, RationalNumber(-1, 3))

    def test_mul1(self):
        test_num1 = RationalNumber(5, 3)
        test_num2 = RationalNumber(2, 3)
        self.assertEqual(test_num1 * test_num2, RationalNumber(10, 9))

    def test_mul2(self):
        test_num1 = RationalNumber(-1, 3)
        test_num2 = RationalNumber(2, 3)
        self.assertEqual(test_num1 * test_num2, RationalNumber(-2, 9))

    def test_mul3(self):
        test_num1 = RationalNumber(1, 3)
        test_num2 = RationalNumber(2, 3)
        self.assertEqual(test_num1 * test_num2, test_num2 * test_num1)

    def test_div1(self):
        test_num1 = RationalNumber(7, 3)
        test_num2 = RationalNumber(1, 2)
        self.assertEqual(test_num1 / test_num2, RationalNumber(14, 3))

    def test_div2(self):
        test_num1 = RationalNumber(3, 4)
        test_num2 = RationalNumber(-1, 5)
        self.assertEqual(test_num1 / test_num2, RationalNumber(-15, 4))

    def test_div3(self):
        test_num1 = RationalNumber(-1, 3)
        test_num2 = RationalNumber(-2, 3)
        self.assertEqual(test_num1 / test_num2, RationalNumber(1, 2))

    def test_equality1(self):
        self.assertTrue(RationalNumber(2, 3) == RationalNumber(4, 6))

    def test_equality2(self):
        self.assertTrue(RationalNumber(2, 3) < RationalNumber(4, 5))

    def test_equality3(self):
        self.assertTrue(RationalNumber(0, 3) > RationalNumber(-4, 6))

    def test_sort(self):
        test_num1 = RationalNumber(0, 4)
        test_num2 = RationalNumber(5, 4)
        test_num3 = RationalNumber(-1, 5)
        sorted_list = [test_num3, test_num2, test_num1]
        self.assertTrue(RationalNumber.sort(test_num1,test_num2,test_num3), sorted_list)


if __name__ == "main":
    unittest.main()
