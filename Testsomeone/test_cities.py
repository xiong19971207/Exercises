import unittest

from Testsomeone.city_functions import read_city


class CityandCountryTest(unittest.TestCase):

    def test_city_country(self):
        testname = read_city('city', 'country', 5000)
        self.assertEqual(testname, 'CityCountry-5000')


unittest.main()
