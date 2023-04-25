import unittest
import re


class MyTestCase(unittest.TestCase):
    def test_type_of(self):
        print(type('123'))
        print(type(123))
        print(type(0.7))

    def test_regex(self):
        assert re.match('www', 'www.runoob.com')  # 在起始位置匹配
        assert not re.match('com', 'www.runoob.com')  # 不在起始位置匹配

    def test_package_name(self):

        assert re.match('^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$', 'setuptools', re.IGNORECASE)


if __name__ == '__main__':
    unittest.main()
