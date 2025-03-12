import os
import unittest


class WorkflowTestCase(unittest.TestCase):
    def test_env(self):
        self.assertEqual('true', os.environ.get('CI'))


if __name__ == '__main__':
    unittest.main()
