#!/usr/bin/python
from bar_chart_water import bar_chart_water
import unittest

class TestBarChart(unittest.TestCase):

    def test_standard(self):
        b = bar_chart_water([1,2,3,4,5,1,2,3,4,1,2,3,4,5,1,2,3,4,3,3,3])
        self.assertEqual(b.run(), 26)

    def test_bug(self):
        b = bar_chart_water([5,4,3,4,3,2,1,0])
        self.assertEqual(b.run(), 1)

    def test_bug2(self):
        b = bar_chart_water([3,2,1,2,1,0,1,0])
        self.assertEqual(b.run(), 2)

    def test_internet_example(self):
        b = bar_chart_water([0,1,0,2,1,0,1,3,2,1,2,1])
        self.assertEqual(b.run(), 6)

    def test_zero(self):
        b = bar_chart_water([0,0,0])
        self.assertEqual(b.run(), 0)

    def test_edge_case1(self):
        b = bar_chart_water([0,1,0])
        self.assertEqual(b.run(), 0)
    
    def test_edge_case2(self):
        b = bar_chart_water([1,0,0])
        self.assertEqual(b.run(), 0)
    
    def test_edge_case3(self):
        b = bar_chart_water([0,0,1])
        self.assertEqual(b.run(), 0)

    def test_edge_case4(self):
        b = bar_chart_water([1,0,1])
        self.assertEqual(b.run(), 1)

    def test_edge_case5(self):
        b = bar_chart_water([1,0,1,0,1])
        self.assertEqual(b.run(), 2)

    def test_edge_case6(self):
        b = bar_chart_water([1,1,1])
        self.assertEqual(b.run(), 0)

if __name__ == '__main__':
    unittest.main()