import unittest
import sys
import os

# Add the parent directory to the path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'coe_6810110200'))

from two_characters import alternate, is_alternating


class TestTwoCharacters(unittest.TestCase):
    """Test cases for the alternate and is_alternating functions."""

    def test_sample_case(self):
        """Test the sample case from the problem description."""
        self.assertEqual(alternate("beabeefeab"), 5)

    def test_is_alternating_helper(self):
        """Test the is_alternating helper function."""
        self.assertTrue(is_alternating([]))
        self.assertTrue(is_alternating(['a']))
        self.assertTrue(is_alternating(['a', 'b']))
        self.assertTrue(is_alternating(['a', 'b', 'a', 'b']))
        self.assertTrue(is_alternating(['b', 'a', 'b', 'a']))

        self.assertFalse(is_alternating(['a', 'a']))
        self.assertFalse(is_alternating(['a', 'b', 'b', 'a']))
        self.assertFalse(is_alternating(['a', 'b', 'a', 'a']))
        self.assertFalse(is_alternating(['b', 'b', 'a', 'b']))

    def test_empty_string(self):
        """Test edge case with empty string."""
        self.assertEqual(alternate(""), 0)

    def test_single_character_string(self):
        """Test edge case with single character."""
        self.assertEqual(alternate("a"), 0)
        self.assertEqual(alternate("aaaa"), 0)
        self.assertEqual(alternate("bbbbbb"), 0)

    def test_two_character_string(self):
        """Test with exactly two different characters."""
        # Already alternating
        self.assertEqual(alternate("ab"), 2)
        self.assertEqual(alternate("ba"), 2)
        self.assertEqual(alternate("abab"), 4)
        self.assertEqual(alternate("baba"), 4)
        
        # Not alternating
        self.assertEqual(alternate("aa"), 0)
        self.assertEqual(alternate("bb"), 0)
        self.assertEqual(alternate("aabb"), 0)
        self.assertEqual(alternate("bbaa"), 0)

    def test_three_character_string(self):
        """Test with three different characters."""
        self.assertEqual(alternate("abc"), 2)  # can form "ab" or "bc" or "ac"
        self.assertEqual(alternate("aba"), 3)  # can form "aba"
        self.assertEqual(alternate("abcabc"), 4)  # can form "abab" or "bcbc" or "acac"

    def test_already_alternating(self):
        """Test strings that are already alternating."""
        self.assertEqual(alternate("ababab"), 6)
        self.assertEqual(alternate("bababa"), 6)
        self.assertEqual(alternate("ab"), 2)
        self.assertEqual(alternate("ba"), 2)

    def test_no_valid_alternating(self):
        """Test strings where no valid alternating string can be formed."""
        self.assertEqual(alternate("aaa"), 0)
        self.assertEqual(alternate("bbb"), 0)
        self.assertEqual(alternate("aaaaabbbbb"), 0)
        self.assertEqual(alternate("abcde"), 2)  # can only form pairs like "ab", "bc", etc.

    def test_complex_patterns(self):
        """Test with complex patterns."""
        # From the problem description example
        self.assertEqual(alternate("beabeefeab"), 5)  # forms "babab"
        
        # Other complex cases
        self.assertEqual(alternate("aabbccdd"), 0)  # no valid alternating pairs
        self.assertEqual(alternate("abacabadabacaba"), 3)  # can form "aba"
        self.assertEqual(alternate("xxyyzz"), 0)  # no valid alternating pairs

    def test_max_length_cases(self):
        """Test cases that should return maximum possible length."""
        # Long alternating string
        long_alternating = "ab" * 100
        self.assertEqual(alternate(long_alternating), 200)
        
        # Long string with many characters but limited alternating possibilities
        mixed = "a" * 50 + "b" * 50 + "c" * 50 + "d" * 50
        self.assertEqual(alternate(mixed), 0)  # no valid alternating pairs due to consecutive groups

    def test_edge_cases_with_repetition(self):
        """Test edge cases with various repetition patterns."""
        self.assertEqual(alternate("aaaaabbbbb"), 0)
        self.assertEqual(alternate("aaabbbccc"), 0)  # no valid alternating pairs
        self.assertEqual(alternate("abcabcabc"), 6)  # can form "ababab" or "bcbcbc" etc.

    def test_specific_character_pairs(self):
        """Test specific character pair combinations."""
        # Test with specific pairs
        self.assertEqual(alternate("ababa"), 5)  # only 'a' and 'b'
        self.assertEqual(alternate("ababac"), 5)  # can form "ababa" using 'a' and 'b'
        self.assertEqual(alternate("xyzxyzx"), 5)  # can form "xyxyx" using 'x' and 'y'

    def test_strings_with_special_characters(self):
        """Test strings with non-alphabetic characters."""
        self.assertEqual(alternate("123123"), 4)  # can form "1212" using '1' and '2'
        self.assertEqual(alternate("!@!@!@"), 6)  # can form "!@!@!@" using '!' and '@'
        self.assertEqual(alternate("a1b2a1b2"), 4)  # can form "abab" using 'a' and 'b'

    def test_all_same_character(self):
        """Test strings with all same character."""
        self.assertEqual(alternate("aaaaaaaaaa"), 0)
        self.assertEqual(alternate("bbbbbbbbbb"), 0)
        self.assertEqual(alternate("1111111111"), 0)

    def test_two_unique_chars_only(self):
        """Test strings that contain exactly two unique characters."""
        # Valid alternating
        self.assertEqual(alternate("abababab"), 8)
        self.assertEqual(alternate("babababa"), 8)
        
        # Invalid alternating
        self.assertEqual(alternate("aabb"), 0)
        self.assertEqual(alternate("bbaa"), 0)
        self.assertEqual(alternate("aaabbb"), 0)
        self.assertEqual(alternate("bbbaaa"), 0)

    def test_optimal_pair_selection(self):
        """Test that the algorithm selects the optimal pair of characters."""
        # String where some pairs work better than others
        s = "abacabadabacaba"
        # The best we can do is "aba" using 'a' and 'b'
        self.assertEqual(alternate(s), 3)

    def test_mixed_case_sensitivity(self):
        """Test case sensitivity."""
        # Different cases should be treated as different characters
        self.assertEqual(alternate("aAaAaA"), 6)  # 'a' and 'A' alternate
        self.assertEqual(alternate("AbAbAb"), 6)  # 'A' and 'b' alternate
        self.assertEqual(alternate("aBcDeF"), 2)  # can form pairs like "aB", "cD", etc.


if __name__ == '__main__':
    unittest.main()
