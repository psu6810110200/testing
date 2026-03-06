import unittest
import sys
import os

# Add the parent directory to the path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'coe_6810110200'))

from grid_challenge import gridChallenge


class TestGridChallenge(unittest.TestCase):
    """Test cases for the gridChallenge function."""

    def test_sample_case(self):
        """Test the sample case from the problem description."""
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        self.assertEqual(gridChallenge(grid), "YES")

    def test_empty_grid(self):
        """Test edge case with empty grid."""
        self.assertEqual(gridChallenge([]), "YES")

    def test_single_cell_grid(self):
        """Test with 1x1 grid."""
        grid = ['a']
        self.assertEqual(gridChallenge(grid), "YES")
        
        grid = ['z']
        self.assertEqual(gridChallenge(grid), "YES")

    def test_two_by_two_grid_yes(self):
        """Test 2x2 grid that should return YES."""
        grid = ['ab', 'cd']
        # After sorting rows: ['ab', 'cd']
        # Columns: a,c and b,d - both in order
        self.assertEqual(gridChallenge(grid), "YES")

    def test_two_by_two_grid_no(self):
        """Test 2x2 grid that should return NO."""
        grid = ['za', 'by']
        # After sorting rows: ['az', 'by']
        # Columns: a,b and z,y - z > y, so NO
        self.assertEqual(gridChallenge(grid), "NO")

    def test_already_sorted_grid(self):
        """Test grid that's already sorted in both rows and columns."""
        grid = ['abc', 'def', 'ghi']
        self.assertEqual(gridChallenge(grid), "YES")

    def test_unsorted_rows_grid(self):
        """Test grid with unsorted rows that can be sorted to meet condition."""
        grid = ['cba', 'fed', 'ihg']
        # After sorting rows: ['abc', 'def', 'ghi']
        # Columns are in order
        self.assertEqual(gridChallenge(grid), "YES")

    def test_columns_out_of_order(self):
        """Test grid where columns are out of order after row sorting."""
        grid = ['abc', 'dfe', 'ghi']
        # After sorting rows: ['abc', 'def', 'ghi']
        # All columns are in order
        self.assertEqual(gridChallenge(grid), "YES")
        
        # A case that should be NO
        grid = ['abc', 'xzy', 'def']
        # After sorting rows: ['abc', 'xyz', 'def']
        # Columns: a,x,d and b,y,e and c,z,f
        # x > a but d < x, so NO
        self.assertEqual(gridChallenge(grid), "NO")

    def test_no_case(self):
        """Test specific case that should return NO."""
        grid = ['mpxz', 'abcd', 'wlmf']
        # After sorting rows: ['mpxz', 'abcd', 'flmw']
        # Check columns:
        # Col 0: m,a,f - m > a, but f < m, so NO
        self.assertEqual(gridChallenge(grid), "NO")

    def test_three_by_three_yes(self):
        """Test 3x3 grid that should return YES."""
        grid = ['abc', 'def', 'ghi']
        self.assertEqual(gridChallenge(grid), "YES")
        
        grid = ['cba', 'fed', 'ihg']
        self.assertEqual(gridChallenge(grid), "YES")

    def test_three_by_three_no(self):
        """Test 3x3 grid that should return NO."""
        grid = ['abc', 'def', 'cba']
        # After sorting rows: ['abc', 'def', 'abc']
        # Columns: a,d,a and b,e,b and c,f,c
        # a<d but a<d is true, then d>a is false
        self.assertEqual(gridChallenge(grid), "NO")
        
        # Let me create a real NO case
        grid = ['abc', 'xzy', 'wvu']
        # After sorting rows: ['abc', 'xyz', 'uvw']
        # Columns: a,x,u and b,y,v and c,z,w
        # x > a but u < x, so NO
        self.assertEqual(gridChallenge(grid), "NO")

    def test_larger_grid(self):
        """Test with larger grid."""
        grid = [
            'ebacd',
            'fghij', 
            'olmkn',
            'trpqs',
            'xywuv'
        ]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_all_same_character(self):
        """Test grid with all same characters."""
        grid = ['aaa', 'aaa', 'aaa']
        self.assertEqual(gridChallenge(grid), "YES")

    def test_reverse_order(self):
        """Test grid with reverse alphabetical order."""
        grid = ['cba', 'fed', 'ihg']
        # After sorting: ['abc', 'def', 'ghi']
        self.assertEqual(gridChallenge(grid), "YES")

    def test_mixed_characters(self):
        """Test grid with mixed character patterns."""
        grid = ['zxv', 'ywu', 'tsr']
        # After sorting: ['vxz', 'uwy', 'rst']
        # Columns: v,u,r; x,w,s; z,y,t
        # v > u, so NO
        self.assertEqual(gridChallenge(grid), "NO")

    def test_single_row(self):
        """Test grid with single row."""
        grid = ['abcdef']
        # After sorting: 'abcdef'
        # No columns to check (only one row)
        self.assertEqual(gridChallenge(grid), "YES")

    def test_single_column(self):
        """Test grid with single column."""
        grid = ['a', 'b', 'c']
        # After sorting: ['a', 'b', 'c']
        # Columns: a,b,c - in order
        self.assertEqual(gridChallenge(grid), "YES")

    def test_identical_rows(self):
        """Test grid with identical rows."""
        grid = ['abc', 'abc', 'abc']
        # After sorting: ['abc', 'abc', 'abc']
        # Columns: a,a,a; b,b,b; c,c,c - in order
        self.assertEqual(gridChallenge(grid), "YES")

    def test_edge_case_characters(self):
        """Test with edge case characters (a and z)."""
        grid = ['az', 'by', 'cx', 'dw']
        # After sorting: ['az', 'by', 'cx', 'dw']
        # Columns: a,b,c,d and z,y,x,w
        # a<b<c<d and z>y>x>w - second column not in order
        self.assertEqual(gridChallenge(grid), "NO")

    def test_complex_valid_case(self):
        """Test a complex but valid case."""
        grid = [
            'hcd',
            'wag',
            'efg'
        ]
        # After sorting: ['cdh', 'agw', 'efg']
        # Columns: c,a,e; d,g,f; h,w,g
        # c>a, so NO
        self.assertEqual(gridChallenge(grid), "NO")

    def test_various_lengths(self):
        """Test grids of various sizes."""
        # 1x1
        self.assertEqual(gridChallenge(['a']), "YES")
        
        # 2x2
        self.assertEqual(gridChallenge(['ab', 'cd']), "YES")
        
        # 3x3
        self.assertEqual(gridChallenge(['abc', 'def', 'ghi']), "YES")
        
        # 4x4
        grid = ['abcd', 'efgh', 'ijkl', 'mnop']
        self.assertEqual(gridChallenge(grid), "YES")

    def test_real_no_case(self):
        """Test a case that should definitely return NO."""
        grid = ['abc', 'cba', 'def']
        # After sorting: ['abc', 'abc', 'def']
        # Columns: a,a,d; b,b,e; c,c,f - all in order
        self.assertEqual(gridChallenge(grid), "YES")
        
        # Let me create a proper NO case
        grid = ['abc', 'def', 'cba']
        # After sorting: ['abc', 'def', 'abc']
        # Columns: a,d,a; b,e,b; c,f,c
        # a<d but a<d? No, a<d is true, but a<d is true again
        # Actually, let me check: a<d (true), d>a (false at row 2->3)
        self.assertEqual(gridChallenge(grid), "NO")


if __name__ == '__main__':
    unittest.main()
