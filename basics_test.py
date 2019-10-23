
import unittest
import get_column_stats as gcs
import random
import os
import statistics as st

class TestGetColumnStats(unittest.TestCase):

    def test_mean_constant(self):
        self.assertEqual(gcs.mean([1,2,3,4]),st.mean([1,2,3,4]))


    def test_stdev_constant(self):
        self.assertEqual(gcs.stdev([1,2,3,4]),st.pstdev[1,2,3,4])


    def test_non_numerical(self):
        self.assertRaises(ValueError,gcs.mean,[1,2,x,3])


    def test_stdev_random(self):
        for i in range(0,100):
            V=[]
            V.append(random.randint(-100,100))
        self.assertEqual(round(gcs.stdev(V),2),round(st.pstdev(V),2)

    def test_mean_random(self):
        for i in range(0,100):
            V=[]
            V.append(random.randint(-100,100))
        self.assertEqual(gcs.mean(V),st.mean(V))
