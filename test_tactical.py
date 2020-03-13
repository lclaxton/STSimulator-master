import unittest
from base_station import *
import io
import contextlib
from typing import List

class TestTacticalStation(unittest.TestCase):

    def setUp(self) -> None:
        self.tactical_station_instance = TacticalStation('Tactical')

    def test_name_sad(self):
        with self.assertRaises(ValueError) as cm:
            broken_name_instance = TacticalStation(1)
        self.assertEqual(str(cm.exception), 'Station name should be a string')

    def test_str(self):
        string_output = str(self.tactical_station_instance)
        self.assertEqual(string_output, "Welcome to the {}".format(self.tactical_station_instance.name))

    def test_repr(self):
        repr_output = repr(self.tactical_station_instance)
        self.assertEqual(repr_output, "NHLC Enterprise Tactical Station")

if __name__ == '__main__':
    unittest.main()
