import unittest
from base_station import *
import io
import contextlib
from typing import List

class TestScienceStation(unittest.TestCase):

    def setUp(self) -> None:
        self.science_station_instance = ScienceStation('science')

    def test_name_sad(self):
        with self.assertRaises(ValueError) as cm:
            broken_name_instance = ScienceStation(1)
        self.assertEqual(str(cm.exception), 'Station name should be a string')

    def test_str(self):
        string_output = str(self.science_station_instance)
        self.assertEqual(string_output, "Welcome to the {}".format(self.science_station_instance.name))

    def test_repr(self):
        repr_output = repr(self.science_station_instance)
        self.assertEqual(repr_output, "NHLC Enterprise Science Station")

if __name__ == '__main__':
    unittest.main()
