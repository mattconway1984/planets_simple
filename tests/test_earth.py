import unittest

from planets.earth import earth

class TestEarth(unittest.TestCase):

    def test_earth_population(self):
        self.assertEqual(earth.population, 8)



