import unittest

from planets.mars import mars

class TestMars(unittest.TestCase):

    def test_mars_population(self):
        self.assertEqual(mars.population, 0)

