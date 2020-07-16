'''
Created on 2020/05/17

@author: seal0
'''
import unittest
import knapsack

class Test(unittest.TestCase):


    def test_knapsack(self):
        w = [1,2,3,5,6]
        v = [2,3,4,8,9]
        b = 5
        ans1 = 8
        ans2 = [4]
        self.assertEqual((ans1, ans2), knapsack.solve_knapsack(w, v, b))
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_knapsack']
    unittest.main()