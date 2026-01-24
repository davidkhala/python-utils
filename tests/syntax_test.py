import os
import re
import unittest
from enum import auto
from pathlib import Path

from davidkhala.utils.syntax import fs, path
from davidkhala.utils.syntax.env import Version, is_windows
from davidkhala.utils.syntax.format import JSONReadable, Package
from davidkhala.utils.syntax.interface import Serializable, SupportsClose, Closeable
from davidkhala.utils.syntax.js import Array
from davidkhala.utils.syntax.time import runtime_of
from davidkhala.utils.syntax.typing import NameEnum


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
        self.assertIsInstance('123', str)
        self.assertIsInstance(123, int)
        self.assertIsInstance(0.7, float)

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

    def test_subprocess(self):
        import subprocess

        subprocess.run(["ls"])

    def test_context_manager(self):
        class Context:
            def __exit__(self, exc_type, exc_value, traceback):
                print("退出上下文，若无异常，参数全None")
                assert exc_type is None, "异常类型"
                assert exc_value is None, "异常实例"
                assert traceback is None, "追踪信息"

        Context()

    def test_close_wrapper(self):
        from contextlib import closing
        class O(SupportsClose):
            ...

        with closing(O()) as o:
            ...

        class O2(Closeable):
            ...

        with O2().context as o2:
            ...

    def test_decorator(self):
        from davidkhala.utils.syntax.compat import deprecated
        @deprecated("Use new_function() instead.")
        def old_function():
            return

        old_function()


class PathTestCase(unittest.TestCase):
    def test_current_file(self):
        self.assertIsInstance(__file__, str)
        self.assertEqual(__file__, path.join(__file__))
        self.assertEqual(__file__, str(path.resolve(__file__)))

    def test_resolve(self):
        self.assertEqual(str(Path.home()), path.homedir())

        print("\n", path.home_resolve('.databrickscfg'))
        if is_windows():
            print('APPDATA=', os.environ.get('APPDATA'))
            print('LocalAppData=', os.environ.get('LOCALAPPDATA'))


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
        from davidkhala.utils.syntax.network import ip
        self.assertNotEqual(ip, '127.0.0.1')
        self.assertNotEqual(ip, 'localhost')
        print('ip=', ip)


class TimeTestcase(unittest.TestCase):
    def test_runtime(self):
        def func():
            import time
            time.sleep(1)

        t, _ = runtime_of(func)
        self.assertGreater(t, 1.0)


class PackageTestCase(unittest.TestCase):
    def test_name(self):
        Package('http_request')
        Package('http-request')
        self.assertRaises(AssertionError, Package, '@davidkhala/http')

    def test_import(self):
        import importlib

        _ = importlib.import_module('davidkhala.utils.syntax.format')
        self.assertEqual(_.Package, Package)


from davidkhala.utils.syntax.log import get_logger, LevelBasedStreamHandler, file_handler


class LoggingTestCase(unittest.TestCase):
    def test_logging(self):
        logger = get_logger()
        logger.addHandler(LevelBasedStreamHandler())
        logger.addHandler(file_handler('logs/test.log'))
        logger.info('info')
        logger.debug('debug')
        logger.error('error')


class FunctionTestCase(unittest.TestCase):
    def test_variadic_parameters(self):
        def f(*data, option):
            pass

        f('a', option=True)


if __name__ == '__main__':
    unittest.main()
