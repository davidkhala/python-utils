import os
import unittest


class Sample(unittest.TestCase):
    def testFunc(self):  # starting with `test` is the convention
        self.assertTrue(True)
class GithubWorkflowTestCase(unittest.TestCase):
    def test_env(self):
        self.assertEqual('true', os.environ.get('CI'))

if __name__ == '__main__':
    unittest.main()
