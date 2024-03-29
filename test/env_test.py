import os
import unittest
from dotenv import load_dotenv


class EnvTestCase(unittest.TestCase):
    def test_load(self):
        load_dotenv()
        domain = os.getenv('domain')

        self.assertEqual(domain, 'example.org')

    def test_env_cannot_overwrite(self):
        os.putenv('domain', 'overwrite')
        load_dotenv(override=False)
        domain = os.getenv('domain')

        self.assertEqual(domain, 'example.org')

    def test_env_list_all(self):
        for name, value in os.environ.items():
            print("{0}: {1}".format(name, value))


if __name__ == '__main__':
    unittest.main()
