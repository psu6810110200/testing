import unittest
import sys
import os

# Add the parent directory to the path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'coe_6810110200'))

from caesar_cipher import caesarCipher


class TestCaesarCipher(unittest.TestCase):
    """Test cases for the caesarCipher function."""

    def test_sample_case(self):
        """Test the sample case from the problem description."""
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")

    def test_no_rotation(self):
        """Test with k=0 (no rotation)."""
        self.assertEqual(caesarCipher("abcXYZ", 0), "abcXYZ")
        self.assertEqual(caesarCipher("Hello-World!", 0), "Hello-World!")

    def test_full_rotation(self):
        """Test with k=26 (full rotation, should return original)."""
        self.assertEqual(caesarCipher("abcXYZ", 26), "abcXYZ")
        self.assertEqual(caesarCipher("Hello-World!", 26), "Hello-World!")

    def test_large_rotation(self):
        """Test with k > 26 (should wrap around)."""
        # k=52 is equivalent to k=0 (52 % 26 = 0)
        self.assertEqual(caesarCipher("abcXYZ", 52), "abcXYZ")
        # k=27 is equivalent to k=1 (27 % 26 = 1)
        self.assertEqual(caesarCipher("abcXYZ", 27), "bcdYZA")
        # k=28 is equivalent to k=2 (28 % 26 = 2)
        self.assertEqual(caesarCipher("abcXYZ", 28), "cdeZAB")

    def test_basic_lowercase(self):
        """Test basic lowercase letter rotation."""
        self.assertEqual(caesarCipher("abc", 1), "bcd")
        self.assertEqual(caesarCipher("abc", 2), "cde")
        self.assertEqual(caesarCipher("abc", 3), "def")
        self.assertEqual(caesarCipher("xyz", 2), "zab")
        self.assertEqual(caesarCipher("xyz", 3), "abc")

    def test_basic_uppercase(self):
        """Test basic uppercase letter rotation."""
        self.assertEqual(caesarCipher("ABC", 1), "BCD")
        self.assertEqual(caesarCipher("ABC", 2), "CDE")
        self.assertEqual(caesarCipher("ABC", 3), "DEF")
        self.assertEqual(caesarCipher("XYZ", 2), "ZAB")
        self.assertEqual(caesarCipher("XYZ", 3), "ABC")

    def test_mixed_case(self):
        """Test with mixed case letters."""
        self.assertEqual(caesarCipher("aBcDeF", 1), "bCdEfG")
        self.assertEqual(caesarCipher("HelloWorld", 5), "MjqqtBtwqi")
        self.assertEqual(caesarCipher("HeLLoWoRLD", 3), "KhOOrZrUOG")

    def test_non_alphabetic_characters(self):
        """Test that non-alphabetic characters remain unchanged."""
        self.assertEqual(caesarCipher("123-456", 5), "123-456")
        self.assertEqual(caesarCipher("!@#$%^&*()", 10), "!@#$%^&*()")
        self.assertEqual(caesarCipher("a-b_c.d", 2), "c-d_e.f")
        self.assertEqual(caesarCipher("Hello, World!", 1), "Ifmmp, Xpsme!")

    def test_empty_string(self):
        """Test edge case with empty string."""
        self.assertEqual(caesarCipher("", 5), "")

    def test_single_character(self):
        """Test single character strings."""
        self.assertEqual(caesarCipher("a", 1), "b")
        self.assertEqual(caesarCipher("Z", 1), "A")
        self.assertEqual(caesarCipher("1", 5), "1")
        self.assertEqual(caesarCipher("!", 10), "!")

    def test_wrapping_around(self):
        """Test wrapping around the alphabet."""
        # Lowercase wrapping
        self.assertEqual(caesarCipher("z", 1), "a")
        self.assertEqual(caesarCipher("y", 2), "a")
        self.assertEqual(caesarCipher("x", 3), "a")
        
        # Uppercase wrapping
        self.assertEqual(caesarCipher("Z", 1), "A")
        self.assertEqual(caesarCipher("Y", 2), "A")
        self.assertEqual(caesarCipher("X", 3), "A")

    def test_maximum_rotation(self):
        """Test with k=25 (maximum rotation)."""
        self.assertEqual(caesarCipher("abc", 25), "zab")
        self.assertEqual(caesarCipher("ABC", 25), "ZAB")
        self.assertEqual(caesarCipher("xyz", 25), "wxy")
        self.assertEqual(caesarCipher("XYZ", 25), "WXY")

    def test_complex_strings(self):
        """Test with complex strings containing various characters."""
        test_string = "The quick brown fox jumps over the lazy dog! 123"
        expected = "Bpm ycqks jzwev nwf rcuxa wdmz bpm tihg lwo! 123"
        self.assertEqual(caesarCipher(test_string, 8), expected)
        
        # Test with punctuation and numbers
        self.assertEqual(caesarCipher("Caesar Cipher 123!", 3), "Fdhvdu Flskhu 123!")
        
        # Test with mixed characters
        self.assertEqual(caesarCipher("A1b2C3d4", 2), "C1d2E3f4")

    def test_edge_cases_with_k(self):
        """Test edge cases with different k values."""
        # k=1
        self.assertEqual(caesarCipher("a", 1), "b")
        
        # k=25
        self.assertEqual(caesarCipher("a", 25), "z")
        
        # k=26 (should be same as k=0)
        self.assertEqual(caesarCipher("a", 26), "a")
        
        # k=27 (should be same as k=1)
        self.assertEqual(caesarCipher("a", 27), "b")
        
        # k=52 (should be same as k=0)
        self.assertEqual(caesarCipher("a", 52), "a")
        
        # k=53 (should be same as k=1)
        self.assertEqual(caesarCipher("a", 53), "b")

    def test_special_characters(self):
        """Test with various special characters."""
        self.assertEqual(caesarCipher("a\nb\tc", 1), "b\nc\td")
        self.assertEqual(caesarCipher("a b c", 2), "c d e")
        self.assertEqual(caesarCipher("a:b;c", 3), "d:e;f")

    def test_all_letters(self):
        """Test with all letters of the alphabet."""
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        # Test rotation by 1
        self.assertEqual(caesarCipher(lowercase, 1), "bcdefghijklmnopqrstuvwxyza")
        self.assertEqual(caesarCipher(uppercase, 1), "BCDEFGHIJKLMNOPQRSTUVWXYZA")
        
        # Test rotation by 13 (ROT13)
        self.assertEqual(caesarCipher(lowercase, 13), "nopqrstuvwxyzabcdefghijklm")
        self.assertEqual(caesarCipher(uppercase, 13), "NOPQRSTUVWXYZABCDEFGHIJKLM")

    def test_rot13(self):
        """Test specific ROT13 case (k=13)."""
        # ROT13 is its own inverse
        original = "Hello, World!"
        encrypted = caesarCipher(original, 13)
        decrypted = caesarCipher(encrypted, 13)
        self.assertEqual(original, decrypted)
        
        # Test with some ROT13 examples
        self.assertEqual(caesarCipher("NOVA", 13), "ABIN")
        self.assertEqual(caesarCipher("ABIN", 13), "NOVA")

    def test_boundary_values(self):
        """Test boundary values for k."""
        # Test with very large k values
        self.assertEqual(caesarCipher("a", 100), caesarCipher("a", 100 % 26))
        self.assertEqual(caesarCipher("Z", 1000), caesarCipher("Z", 1000 % 26))
        self.assertEqual(caesarCipher("Hello", 12345), caesarCipher("Hello", 12345 % 26))


if __name__ == '__main__':
    unittest.main()
