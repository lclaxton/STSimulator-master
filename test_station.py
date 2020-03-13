import unittest
from base_station import BaseStation
import io
import contextlib
from typing import List


class TestStation(unittest.TestCase):

    def setUp(self) -> None:
        self.station_instance = BaseStation('base')

    def test_score(self):
        self.assertEqual(self.station_instance.score, 30)

    def test_max_crew(self):
        self.assertEqual(self.station_instance.max_crew, 6)

    def test_crew(self):
        self.assertEqual(self.station_instance.crew, 0)

    def test_name_sad(self):
        with self.assertRaises(ValueError) as cm:
            broken_name_instance = BaseStation(1)
        self.assertEqual(str(cm.exception), 'Station name should be a string')

    def test_crew_members(self):
        self.assertEqual(type(self.station_instance.crew_members), list)

    def test_str(self):
        string_output = str(self.station_instance)
        self.assertEqual(string_output, "Welcome to the {}".format(self.station_instance.name))

    def test_repr(self):
        repr_output = repr(self.station_instance)
        self.assertEqual(repr_output, "NHLC Enterprise base station")


if __name__ == '__main__':
    unittest.main()
