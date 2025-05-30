import unittest

from davidkhala.poetry import reconfigure_python
from davidkhala.syntax import is_windows, is_mac


class ReconfigureTestCase(unittest.TestCase):

    def test_python_version(self):
        try:
            reconfigure_python('3.12.7')
        except FileNotFoundError as e:
            if is_windows() or is_mac():
                raise e


if __name__ == '__main__':
    unittest.main()
