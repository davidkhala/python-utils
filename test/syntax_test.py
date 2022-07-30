import unittest


class MyTestCase(unittest.TestCase):
    def test_type_of(self):
        print(type('123'))
        print(type(123))
        print(type(0.7))


if __name__ == '__main__':
    unittest.main()
