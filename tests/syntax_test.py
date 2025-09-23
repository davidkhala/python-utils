import os
import re
import unittest
from enum import auto
from ipaddress import IPv4Address
from pathlib import Path

from davidkhala.poetry import reconfigure_python
from davidkhala.syntax import Package, NameEnum, fs, path, is_windows
from davidkhala.syntax.format import JSONReadable
from davidkhala.syntax.interface import Serializable
from davidkhala.syntax.js import Array


class LanguageTestCase(unittest.TestCase):
    def test_array(self):
        def sum(x, y):
            return x + y

        numbers = Array([1, 2, 3, 4, 5])

        squared_numbers = numbers.map(lambda x: x ** 2)

        total_sum = squared_numbers.reduce(sum)

        self.assertEqual(total_sum, 55)

        def f(value, i, _):
            self.assertEqual(value, i + 1)

        numbers.forEach(f)

    def test_class(self):
        """
        Class Variables are shared among all instances of the class.
        They are defined at the class level and are not tied to any specific instance.
        """

        class A:
            const = "value"  # This is Class Variable

        a = A()
        a.const = ""
        self.assertEqual(a.const, "")
        self.assertNotEqual(a.const, A.const)

        class B:
            const: str

        B.const = "class"
        b = B()
        b.const = 'value'

        self.assertEqual('value', b.const)
        self.assertEqual('class', B.const)

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
        """
        Added in python 3.10
        match 1:
            case 1:
                return
            case 2:
                assert False
            case _:
                assert False
        """

    def test_dict(self):
        key = "a"
        value = "b"
        _dict = {
            key: value
        }
        self.assertEqual(_dict[key], "b")
        self.assertEqual(_dict[("%s" % key)], "b")

    def test_version(self):
        from davidkhala.syntax.env import Version
        import sys
        v = Version()
        self.assertEqual(str(sys.version_info.major), v.major)
        self.assertEqual(str(sys.version_info.minor), v.minor)
        self.assertEqual(str(sys.version_info.micro), v.micro)

    def test_generator(self):
        sq = (x * x for x in range(1, 6))
        from typing import Generator
        self.assertIsInstance(sq, Generator)

    def test_bool(self):
        self.assertTrue(True == 1 and False == 0)
        self.assertEqual(2, True + 1)
        self.assertEqual(2, 1 + True)
        self.assertEqual(1, 1 + False)
        self.assertIsInstance(True, int)


class PathTestCase(unittest.TestCase):
    def test_current_file(self):
        self.assertIsInstance(__file__, str)
        self.assertEqual(__file__, path.resolve(__file__))

    def test_resolve(self):

        self.assertEqual(str(Path.home()), path.homedir())

        print("\n", path.home_resolve('.databrickscfg'))
        if is_windows():
            print('APPDATA=', os.environ.get('APPDATA'))
            print('LocalAppData=', os.environ.get('LOCALAPPDATA'))

    def test_poetry(self):
        if is_windows() and not os.environ.get('ci'):
            reconfigure_python('3.13.2')


class FileTestCase(unittest.TestCase):
    def test_read(self):
        content = fs.read('tests/data/.env')
        self.assertRegex(content, 'domain=')

    def test_write(self):
        fs.write('tests/data/.env', 'domain=example.org\n')
        fs.write('.noexist', '')

    def test_append(self):
        fs.append('tests/data/.env', 'Org=github\n')

    def test_write_json(self):
        data = '.afda'
        fs.write_json(data)
        from dataclasses import dataclass
        @dataclass
        class S(Serializable):
            name: str = 'G'

        fs.write_json(S(), 's')


class JSONTest(unittest.TestCase):
    def test_json(self):
        r = JSONReadable({'4': 5, '6': 7})
        JSONReadable(['b', 'c'])
        JSONReadable("[]")
        fs.write('tests/artifacts/test.json', r)


class NetworkTestcase(unittest.TestCase):
    def test_ip(self):
        from davidkhala.syntax.network import ip
        self.assertNotEqual(ip, '127.0.0.1')
        self.assertNotEqual(ip, 'localhost')
        print('ip=', ip)


class PackageTestCase(unittest.TestCase):
    def test_name(self):
        Package('http_request')
        Package('http-request')
        self.assertRaises(AssertionError, Package, '@davidkhala/http')

    def test_import(self):
        import importlib
        from davidkhala.syntax import Package
        _ = importlib.import_module('davidkhala.syntax')
        self.assertEqual(_.Package, Package)


if __name__ == '__main__':
    unittest.main()
