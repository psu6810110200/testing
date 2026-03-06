from coe_6810110200.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    
    def test_give_empty_list_returns_true(self):
        empty_list = []
        is_prime = is_prime_list(empty_list)
        self.assertTrue(is_prime)
    
    def test_give_single_prime_number_returns_true(self):
        prime_list = [7]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    
    def test_give_single_composite_number_returns_false(self):
        composite_list = [4]
        is_prime = is_prime_list(composite_list)
        self.assertFalse(is_prime)
    
    def test_give_mixed_primes_and_composites_returns_false(self):
        mixed_list = [2, 3, 4, 5]
        is_prime = is_prime_list(mixed_list)
        self.assertFalse(is_prime)
    
    def test_give_all_composite_numbers_returns_false(self):
        composite_list = [4, 6, 8, 9, 10]
        is_prime = is_prime_list(composite_list)
        self.assertFalse(is_prime)