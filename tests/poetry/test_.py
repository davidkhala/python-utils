import unittest

from davidkhala.syntax import is_windows, is_linux, is_mac
from davidkhala.syntax.poetry import reconfigure_python


class ReconfigureTestCase(unittest.TestCase):

    def test_python_version(self):
        try:
            reconfigure_python('3.13.2')
        except FileNotFoundError as e:
            if is_windows():
                raise e
            elif is_linux():
                pass
            elif is_mac():
                raise e


if __name__ == '__main__':
    unittest.main()
