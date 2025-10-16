import unittest

from davidkhala.utils.geo import as_of, xyz_of


class GeoTestCase(unittest.TestCase):
    def test_vector(self):
        lat =22.283
        lon =114.173
        print(as_of(lat, lon))
        print(xyz_of(lat, lon))


if __name__ == '__main__':
    unittest.main()
