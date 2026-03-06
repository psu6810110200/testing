import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'coe_6810110200'))

from funny_string import funnyString


class TestFunnyString(unittest.TestCase):
    def test_sample_cases(self):
        """Test the sample cases from the problem description."""
        # Test case 0: acxz should be Funny
        self.assertEqual(funnyString("acxz"), "Funny")
        
        # Test case 1: bcxz should be Not Funny
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_single_character(self):
        """Test edge case with single character."""
        # Single character should always be Funny (no differences to compare)
        self.assertEqual(funnyString("a"), "Funny")
        self.assertEqual(funnyString("z"), "Funny")

    def test_two_characters(self):
        """Test edge case with two characters."""
        # Two characters: only one difference, which will be the same when reversed
        self.assertEqual(funnyString("ab"), "Funny")
        self.assertEqual(funnyString("az"), "Funny")
        self.assertEqual(funnyString("zy"), "Funny")

    def test_palindrome_strings(self):
        """Test palindrome strings (should always be Funny)."""
        self.assertEqual(funnyString("aba"), "Funny")
        self.assertEqual(funnyString("racecar"), "Funny")
        self.assertEqual(funnyString("madam"), "Funny")

    def test_funny_strings(self):
        """Test strings that are known to be Funny."""
        self.assertEqual(funnyString("acxz"), "Funny")
        self.assertEqual(funnyString("abcba"), "Funny")
        self.assertEqual(funnyString("abcdcba"), "Funny")

    def test_not_funny_strings(self):
        """Test strings that are known to be Not Funny."""
        self.assertEqual(funnyString("bcxz"), "Not Funny")
        self.assertEqual(funnyString("abca"), "Not Funny")
        # abcdef is actually Funny (all consecutive differences are 1)
        self.assertEqual(funnyString("abcf"), "Not Funny")

    def test_all_same_characters(self):
        """Test strings with all same characters."""
        self.assertEqual(funnyString("aaaa"), "Funny")
        self.assertEqual(funnyString("bbbbbb"), "Funny")

    def test_ascending_sequence(self):
        """Test ascending character sequences."""
        self.assertEqual(funnyString("abc"), "Funny") 
        self.assertEqual(funnyString("xyz"), "Funny")  

    def test_descending_sequence(self):
        """Test descending character sequences."""
        self.assertEqual(funnyString("cba"), "Funny")  
        self.assertEqual(funnyString("zyx"), "Funny")  

    def test_mixed_case_sensitivity(self):
        """Test case sensitivity (ASCII values matter)."""
        # Lowercase and uppercase have different ASCII values
        # Single difference strings should be Funny
        self.assertEqual(funnyString("aA"), "Funny")
        self.assertEqual(funnyString("Aa"), "Funny")
        
        # Test with more characters to see case sensitivity effects
        self.assertEqual(funnyString("aAz"), "Not Funny")  # differences: [32, 25], reversed: [25, 32]

    def test_empty_string(self):
        """Test edge case with empty string."""
        # Empty string should be Funny (no characters to compare)
        self.assertEqual(funnyString(""), "Funny")

    def test_long_strings(self):
        """Test with longer strings."""
        # Long not funny string (verified actual behavior)
        self.assertEqual(funnyString("acdefghijkjihgfedcba"), "Not Funny")
        # Test with another long string that is Funny
        self.assertEqual(funnyString("abcdefghijklmnoponmlkjihgfedcba"), "Funny")

    def test_specific_ascii_differences(self):
        """Test strings with specific ASCII difference patterns."""
        # String where differences are not symmetric (verified actual behavior)
        self.assertEqual(funnyString("adgja"), "Not Funny")  # differences: [3, 3, 7, 3], reversed: [3, 7, 3, 3]
        
        # String where differences are not symmetric
        self.assertEqual(funnyString("adgjb"), "Not Funny")  # differences: [3, 3, 7, 4], reversed: [4, 7, 3, 3]

    def test_boundary_characters(self):
        """Test strings with boundary ASCII characters."""
        # Using 'a' (97) and 'z' (122)
        self.assertEqual(funnyString("az"), "Funny")  # difference: 25
        self.assertEqual(funnyString("za"), "Funny")  # difference: 25
        
        # Using boundary characters in longer strings
        self.assertEqual(funnyString("aza"), "Funny")
        self.assertEqual(funnyString("zaz"), "Funny")  

if __name__ == '__main__':
    unittest.main()
