import unittest
import sys
import os

# Add the parent directory to the path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'coe_6810110200'))

from alternating_characters import alternatingCharacters


class TestAlternatingCharacters(unittest.TestCase):
    """Test cases for the alternatingCharacters function."""

    def test_sample_cases(self):
        """Test the sample cases from the problem description."""
        # Test case 0: AAAA -> need to delete 3 characters to get "A"
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        
        # Test case 1: BBBBB -> need to delete 4 characters to get "B"
        self.assertEqual(alternatingCharacters("BBBBB"), 4)
        
        # Test case 2: ABABABAB -> already alternating, no deletions needed
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
        
        # Test case 3: BABABA -> already alternating, no deletions needed
        self.assertEqual(alternatingCharacters("BABABA"), 0)
        
        # Test case 4: AAABBB -> need to delete 2 A's and 2 B's
        self.assertEqual(alternatingCharacters("AAABBB"), 4)

    def test_empty_string(self):
        """Test edge case with empty string."""
        self.assertEqual(alternatingCharacters(""), 0)

    def test_single_character(self):
        """Test edge case with single character."""
        self.assertEqual(alternatingCharacters("A"), 0)
        self.assertEqual(alternatingCharacters("B"), 0)

    def test_two_characters(self):
        """Test edge case with two characters."""
        # Already alternating
        self.assertEqual(alternatingCharacters("AB"), 0)
        self.assertEqual(alternatingCharacters("BA"), 0)
        
        # Same characters, need to delete one
        self.assertEqual(alternatingCharacters("AA"), 1)
        self.assertEqual(alternatingCharacters("BB"), 1)

    def test_all_same_characters(self):
        """Test strings with all same characters."""
        self.assertEqual(alternatingCharacters("A"), 0)
        self.assertEqual(alternatingCharacters("AA"), 1)
        self.assertEqual(alternatingCharacters("AAA"), 2)
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("AAAAA"), 4)
        
        self.assertEqual(alternatingCharacters("B"), 0)
        self.assertEqual(alternatingCharacters("BB"), 1)
        self.assertEqual(alternatingCharacters("BBB"), 2)
        self.assertEqual(alternatingCharacters("BBBB"), 3)
        self.assertEqual(alternatingCharacters("BBBBB"), 4)

    def test_perfectly_alternating(self):
        """Test strings that are perfectly alternating."""
        self.assertEqual(alternatingCharacters("AB"), 0)
        self.assertEqual(alternatingCharacters("BA"), 0)
        self.assertEqual(alternatingCharacters("ABAB"), 0)
        self.assertEqual(alternatingCharacters("BABA"), 0)
        self.assertEqual(alternatingCharacters("ABABAB"), 0)
        self.assertEqual(alternatingCharacters("BABABA"), 0)
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
        self.assertEqual(alternatingCharacters("BABABABA"), 0)

    def test_mixed_patterns(self):
        """Test strings with mixed patterns."""
        # Starting with A
        self.assertEqual(alternatingCharacters("AAB"), 1)  # delete one A
        self.assertEqual(alternatingCharacters("ABB"), 1)  # delete one B
        self.assertEqual(alternatingCharacters("AABBB"), 3)  # delete one A and two B's
        self.assertEqual(alternatingCharacters("AAABB"), 3)  # delete two A's and one B
        
        # Starting with B
        self.assertEqual(alternatingCharacters("BBA"), 1)  # delete one B
        self.assertEqual(alternatingCharacters("BAA"), 1)  # delete one A
        self.assertEqual(alternatingCharacters("BBAAA"), 3)  # delete one B and two A's
        self.assertEqual(alternatingCharacters("BBBAA"), 3)  # delete two B's and one A

    def test_complex_patterns(self):
        """Test more complex patterns."""
        self.assertEqual(alternatingCharacters("AAABBBAA"), 5)  # delete 2 A's, 2 B's, 1 A
        self.assertEqual(alternatingCharacters("BBBBABBB"), 5)  # delete 3 B's, 1 A, 1 B
        self.assertEqual(alternatingCharacters("ABABABAA"), 1)  # delete one consecutive A
        self.assertEqual(alternatingCharacters("BABABABB"), 1)  # delete one consecutive B

    def test_long_strings(self):
        """Test with longer strings."""
        # Long alternating string
        long_alternating = "AB" * 50 + "A"  # 101 characters
        self.assertEqual(alternatingCharacters(long_alternating), 0)
        
        # Long string with consecutive characters
        long_consecutive = "A" * 50 + "B" * 50
        self.assertEqual(alternatingCharacters(long_consecutive), 98)  # delete 49 A's and 49 B's

    def test_alternating_with_interruptions(self):
        """Test alternating strings with occasional interruptions."""
        self.assertEqual(alternatingCharacters("ABABAAAB"), 2)  # delete two consecutive A's
        self.assertEqual(alternatingCharacters("BABABBBB"), 3)  # delete three consecutive B's
        self.assertEqual(alternatingCharacters("ABABBABA"), 1)  # delete one consecutive B
        self.assertEqual(alternatingCharacters("BABABABA"), 0)  # perfectly alternating

    def test_edge_cases(self):
        """Test various edge cases."""
        # Single character repeated many times
        self.assertEqual(alternatingCharacters("A" * 100), 99)
        self.assertEqual(alternatingCharacters("B" * 100), 99)
        
        # Perfectly alternating long strings
        self.assertEqual(alternatingCharacters("AB" * 50), 0)
        self.assertEqual(alternatingCharacters("BA" * 50), 0)
        
        # Mixed patterns at the end
        self.assertEqual(alternatingCharacters("ABABABAAA"), 2)
        self.assertEqual(alternatingCharacters("BABABABB"), 1)

    def test_specific_scenarios(self):
        """Test specific scenarios that might be tricky."""
        # Pattern: two same, then different
        self.assertEqual(alternatingCharacters("AAB"), 1)
        self.assertEqual(alternatingCharacters("BBA"), 1)
        
        # Pattern: different, then two same
        self.assertEqual(alternatingCharacters("ABB"), 1)
        self.assertEqual(alternatingCharacters("BAA"), 1)
        
        # Pattern: multiple groups
        self.assertEqual(alternatingCharacters("AAABBB"), 4)
        self.assertEqual(alternatingCharacters("BBBAAA"), 4)
        
        # Pattern: alternating with double at end
        self.assertEqual(alternatingCharacters("ABABAA"), 1)
        self.assertEqual(alternatingCharacters("BABABB"), 1)


if __name__ == '__main__':
    unittest.main()
