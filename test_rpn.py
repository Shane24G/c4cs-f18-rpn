#import unittest
#import rpn
#
#class TestBasics(unittest.TestCase):
#    def test_add(self):
#        result = rpn.calculate('1 1 +')
#        self.assertEqual(2, result)
#    
#    def test_sub(self):
#       result = rpn.calculate('4 3 -') 
#       self.assertEqual(1, result)
#
#    def test_mul(self):
#         result = rpn.calculate('3 7 *')
#         self.assertEqual(21, result)
#
#    def test_div(self):
#        result = rpn.calculate('4 2 /')
#        self.assertEqual(2, result)
#
#    def test_chain(self):
#        result = rpn.calculate('1 1 + 2 *')
#        self.assertEqual(4, result)
#
import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_carat(self):
        result = rpn.calculate("2 4 ^")
        self.assertEqual(16, result)
