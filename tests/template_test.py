import unittest


class Sample(unittest.TestCase):
    def testFunc(self):  # starting with `test` is the convention
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
