import unittest
from base_station import *
import io
import contextlib
from typing import List

class TestCommandStation(unittest.TestCase):

    def setUp(self) -> None:
        self.command_station_instance = CommandStation('command') 

    def test_name_sad(self):
        with self.assertRaises(ValueError) as cm:
            broken_name_instance = CommandStation(1)
        self.assertEqual(str(cm.exception), 'Command Station name should be a string')

    def test_str(self):
        string_output = str(self.station_instance)
        self.assertEqual(string_output, "Welcome to the {}".format(self.station_instance.name))

    def test_repr(self):
        repr_output = repr(self.station_instance)
        self.assertEqual(repr_output, "NHLC Enterprise Command Station")

if __name__ == '__main__':
    unittest.main()
