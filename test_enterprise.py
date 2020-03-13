import unittest
from enterprise import Enterprise
import io
import contextlib


class TestEnterprise(unittest.TestCase):

    def setUp(self):
        self.enterprise_instance = Enterprise("test_name")

    def test_max_power_level(self):
        self.assertEqual(self.enterprise_instance.max_power_level, 1000)

    def test_power_level(self):
        self.assertEqual(self.enterprise_instance.power_level, 1000)

    def test_max_population(self):
        self.assertEqual(self.enterprise_instance.max_population, 30)

    def test_population(self):
        self.assertEqual(self.enterprise_instance.population, 0)

    def test_max_shield_level(self):
        self.assertEqual(self.enterprise_instance.max_shield_level, 100)

    def test_shield_level(self):
        self.assertEqual(self.enterprise_instance.shield_level, 100)

    def test_str(self):
        string_output = str(self.enterprise_instance)
        self.assertEqual(string_output, "Welcome to the {}".format(self.enterprise_instance.name))

    def test_repr(self):
        repr_output = repr(self.enterprise_instance)
        self.assertEqual(repr_output, "NHLC Enterprise")

    def test_name_sad(self):
        with self.assertRaises(ValueError) as cm:
            broken_name_instance = Enterprise(1)
        self.assertEqual(str(cm.exception), 'Enterprise name should be a string')


if __name__ == '__main__':
    unittest.main()
