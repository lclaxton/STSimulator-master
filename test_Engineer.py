import unittest
from base_station import *
import io
import contextlib
from typing import List


class TestEngineerStation(unittest.TestCase):

    def setUp(self) -> None:
        self.Engineer_station_instance = EngineerStation('Engineer')

    def test_name_sad(self):
        with self.assertRaises(ValueError) as cm:
            broken_name_instance = BaseStation(1)
        self.assertEqual(str(cm.exception), 'Station name should be a string')

    def test_str(self):
        string_output = str(self.Engineer_station_instance)
        self.assertEqual(string_output, "Welcome to the {}".format(self.Engineer_station_instance.name))

    def test_repr(self):
        repr_output = repr(self.Engineer_station_instance)
        self.assertEqual(repr_output, "NHLC Enterprise Engineer Station")


if __name__ == '__main__':
    unittest.main()
