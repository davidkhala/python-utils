import os
import unittest
from dotenv import load_dotenv

from davidkhala.utils.syntax import is_mac, is_linux, is_windows
from davidkhala.utils.syntax.env import USER, Version


class EnvTestCase(unittest.TestCase):
    def test_load(self):
        load_dotenv(dotenv_path="tests/data/.env")
        domain = os.getenv("domain")

        self.assertEqual(domain, "example.org")

    def test_env_cannot_overwrite(self):
        os.putenv("domain", "overwrite")
        load_dotenv(override=False, dotenv_path="tests/data/.env")
        domain = os.getenv("domain")

        self.assertEqual(domain, "example.org")

    def test_user(self):
        if os.environ.get("CI") == "true":
            if is_mac():
                self.assertEqual('runner', USER)
                self.assertEqual('root', os.getlogin())
            elif is_linux():
                version = Version()

                match version.minor:
                    case '10' | '11':
                        expectedError = r"\[Errno 25\] Inappropriate ioctl for device"
                    case _:  # default
                        expectedError = r"\[Errno -25\] Unknown error -25"
                self.assertRaisesRegex(OSError, expectedError, os.getlogin)
            elif is_windows():
                self.assertEqual(USER, os.getlogin())
        else:
            self.assertEqual(USER, os.getlogin())

    def test_env_list_all(self):
        for name, value in os.environ.items():
            print("{0}: {1}".format(name, value))

class PoetryTestCase(unittest.TestCase):
    def test_reconfigure(self):
        from davidkhala.utils.poetry import reconfigure_python
        if is_windows() and not os.environ.get('ci'):
            reconfigure_python('3.13.2')



if __name__ == "__main__":
    unittest.main()
