from coe_6810110200.fizzbuzz import fizzbuzz
import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_divisible_by_both_3_and_5_returns_fizzbuzz(self):
        result = fizzbuzz(15)
        self.assertEqual(result, "FizzBuzz")
        
    def test_divisible_by_3_returns_fizz(self):
        result = fizzbuzz(6)
        self.assertEqual(result, "Fizz")
        
    def test_divisible_by_5_returns_buzz(self):
        result = fizzbuzz(10)
        self.assertEqual(result, "Buzz")
        
    def test_not_divisible_by_3_or_5_returns_number_as_string(self):
        result = fizzbuzz(7)
        self.assertEqual(result, "7")
        
    def test_zero_returns_fizzbuzz(self):
        result = fizzbuzz(0)
        self.assertEqual(result, "FizzBuzz")
        
    def test_negative_number_divisible_by_3_returns_fizz(self):
        result = fizzbuzz(-3)
        self.assertEqual(result, "Fizz")
        
    def test_negative_number_divisible_by_5_returns_buzz(self):
        result = fizzbuzz(-5)
        self.assertEqual(result, "Buzz")
        
    def test_negative_number_divisible_by_both_returns_fizzbuzz(self):
        result = fizzbuzz(-15)
        self.assertEqual(result, "FizzBuzz")
        
    def test_negative_number_not_divisible_returns_string(self):
        result = fizzbuzz(-7)
        self.assertEqual(result, "-7")
