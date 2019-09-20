
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
