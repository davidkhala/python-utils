import unittest


class PackageTestCase(unittest.TestCase):
    def test_name(self):
        from syntax import Package
        assert Package('http_request')
        assert Package('http-request')
        self.assertRaises(AssertionError, Package, '@davidkhala/http')


if __name__ == '__main__':
    unittest.main()
