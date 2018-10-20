#!/usr/bin/python
from bar_chart_water import bar_chart_water
import unittest

class TestBarChart(unittest.TestCase):

    def test_standard(self):
        a = [1,2,3,4,5,1,2,3,4,1,2,3,4,5,1,2,3,4,3,3,3]
        self.assertEqual(bar_chart_water(a), 26)

    def test_internet_example(self):
        a = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(bar_chart_water(a), 6)

    def test_zero(self):
        a = [0,0,0]
        self.assertEqual(bar_chart_water(a), 0)

    def test_edge_case1(self):
        a = [0,1,0]
        self.assertEqual(bar_chart_water(a), 0)
    
    def test_edge_case2(self):
        a = [1,0,0]
        self.assertEqual(bar_chart_water(a), 0)
    
    def test_edge_case3(self):
        a = [0,0,1]
        self.assertEqual(bar_chart_water(a), 0)

    def test_edge_case4(self):
        a = [1,0,1]
        self.assertEqual(bar_chart_water(a), 1)

    def test_edge_case5(self):
        a = [1,0,1,0,1]
        self.assertEqual(bar_chart_water(a), 2)

    def test_edge_case6(self):
        a = [1,1,1]
        self.assertEqual(bar_chart_water(a), 0)

if __name__ == '__main__':
    unittest.main()