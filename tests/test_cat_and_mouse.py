from coe_6810110200.cat_and_mouse import cat_and_mouse
import unittest

class CatAndMouseTest(unittest.TestCase):
    def test_cat_a_wins_example(self):
        result = cat_and_mouse(1, 5, 2)
        self.assertEqual(result, "Cat A")
        
    def test_cat_b_wins_example(self):
        result = cat_and_mouse(2, 5, 4)
        self.assertEqual(result, "Cat B")
        
    def test_mouse_escapes_equal_distance(self):
        result = cat_and_mouse(1, 3, 2)
        self.assertEqual(result, "Mouse C")
        
    def test_cat_a_wins_example_2(self):
        result = cat_and_mouse(1, 2, 3)
        self.assertEqual(result, "Cat B")
        
    def test_cat_a_closer_to_mouse(self):
        result = cat_and_mouse(10, 20, 12)
        self.assertEqual(result, "Cat A")
        
    def test_cat_b_closer_to_mouse(self):
        result = cat_and_mouse(5, 8, 7)
        self.assertEqual(result, "Cat B")
        
    def test_both_cats_same_position(self):
        result = cat_and_mouse(5, 5, 3)
        self.assertEqual(result, "Mouse C")
        
    def test_mouse_between_cats_equal_distance(self):
        result = cat_and_mouse(1, 5, 3)
        self.assertEqual(result, "Mouse C")
        
    def test_cat_a_at_mouse_position(self):
        result = cat_and_mouse(10, 20, 10)
        self.assertEqual(result, "Cat A")
        
    def test_cat_b_at_mouse_position(self):
        result = cat_and_mouse(10, 20, 20)
        self.assertEqual(result, "Cat B")
        
    def test_edge_case_minimum_values(self):
        result = cat_and_mouse(1, 1, 1)
        self.assertEqual(result, "Mouse C")
        
    def test_edge_case_maximum_values(self):
        result = cat_and_mouse(100, 1, 50)
        self.assertEqual(result, "Cat B")
