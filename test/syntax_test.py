from enum import auto

from syntax import Package, NameEnum, fs, for_each
import unittest
import re

from syntax.format import JSONReadable, Serializable, SQL
from syntax.js import Array


class LanguageTestCase(unittest.TestCase):
    def test_map(self):
        def square(x):
            return x ** 2

        def sum(x, y):
            return x + y

        # List of numbers
        numbers = Array([1, 2, 3, 4, 5])

        # Use map to apply the function
        squared_numbers = numbers.map(square)

        # Use reduce to sum the squared numbers
        total_sum = squared_numbers.reduce(sum)

        # Print the result
        self.assertEqual(total_sum, 55)

    def test_class(self):
        class A:
            const = "value"

        a = A()
        a.const = ""
        self.assertEqual(a.const, "")
        self.assertNotEqual(a.const, A.const)

    def test_type_of(self):
        self.assertEqual(type('123').__name__, 'str')
        self.assertEqual(type(123).__name__, 'int')
        self.assertEqual(type(0.7).__name__, 'float')

    def test_string_literal(self):
        project_id = 'davidkhala'
        self.assertEqual(f"projects/{project_id}", 'projects/davidkhala')

    def test_regex(self):
        self.assertRegex('www.runoob.com', 'www')  # 在起始位置匹配
        self.assertRegex('www.runoob.com', 'com')  # 不在起始位置匹配
        self.assertTrue(re.match('^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$', 'setuptools', re.IGNORECASE))

    def test_enum(self):
        class Ordinal(NameEnum):
            NORTH = auto()
            SOUTH = auto()
            EAST = auto()
            WEST = auto()

        self.assertEqual(f"{Ordinal.NORTH}", 'Ordinal.NORTH', "print(Ordinal.NORTH) output == 'Ordinal.NORTH'")
        self.assertEqual(Ordinal.NORTH.value, 'NORTH')

    def test_switch(self):
        match 1:
            case 1:
                return
            case 2:
                assert False
            case _:
                assert False

    def test_for_each(self):
        def f(i, value):
            self.assertEqual(value, i + 1)

        for_each([1, 2, 3], f)

    def test_dict(self):

        key = "a"
        value = "b"
        _dict = {
            key: value
        }
        self.assertEqual(_dict[key], "b")
        self.assertEqual(_dict[("%s" % key)], "b")


class FileTestCase(unittest.TestCase):
    def test_read(self):
        content = fs.read('.env')
        self.assertRegex(content, 'domain=')

    def test_write(self):
        fs.write('.env', 'domain=example.org\n')
        fs.write('.noexist', '')

    def test_append(self):
        fs.append('.env', 'Org=github\n')

    def test_resolve(self):
        path = fs.resolve(__file__)
        self.assertEqual(__file__, path)

    def test_write_json(self):
        data = '.afda'
        fs.write_json(data)

        class S(Serializable):
            def __str__(self):
                return 's'

            def as_dict(self) -> dict:
                return {"name": "G"}

        fs.write_json(S())


class JSONTest(unittest.TestCase):
    def test_json(self):
        r = JSONReadable({'4': 5, '6': 7})
        JSONReadable(['b', 'c'])
        JSONReadable("[]")
        fs.write('artifacts/test.json', r)


class PackageTestCase(unittest.TestCase):
    def test_name(self):
        Package('http_request')
        Package('http-request')
        self.assertRaises(AssertionError, Package, '@davidkhala/http')


class SQLParseTestCase(unittest.TestCase):
    def test_split(self):
        sql_content = fs.read('data/test.sql')
        s = SQL(sql_content)
        for statement in s.split():
            print(statement)


if __name__ == '__main__':
    unittest.main()
