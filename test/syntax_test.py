import unittest
import re


class ScriptTestCase(unittest.TestCase):
    def test_type_of(self):
        self.assertEqual(type('123').__name__, 'str')
        self.assertEqual(type(123).__name__, 'int')
        self.assertEqual(type(0.7).__name__, 'float')

    def test_string_literal(self):
        project_id = 'davidkhala'
        self.assertEqual(f"projects/{project_id}", 'projects/davidkhala')

    def test_regex(self):
        self.assertRegex('www', 'www.runoob.com')  # 在起始位置匹配
        self.assertRegex('com', 'www.runoob.com')  # 不在起始位置匹配

    def test_package_name(self):
        self.assertTrue(re.match('^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$', 'setuptools', re.IGNORECASE))


class PackageTestCase(unittest.TestCase):
    def test_name(self):
        from syntax import Package
        Package('http_request')
        Package('http-request')
        self.assertRaises(AssertionError, Package, '@davidkhala/http')


if __name__ == '__main__':
    unittest.main()
