import unittest

from davidkhala.syntax import is_windows
from davidkhala.syntax.poetry import reconfigure_python


class ReconfigureTestCase(unittest.TestCase):

    def test_python_version(self):
        # if is_windows():
            reconfigure_python('3.13.2')

if __name__ == '__main__':
    unittest.main()