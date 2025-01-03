import unittest

from davidkhala.sql import SQL
from davidkhala.syntax import fs


class SQLParseTestCase(unittest.TestCase):
    def test_split(self):
        sql_content = fs.read('data/test.sql')
        s = SQL(sql_content)
        for statement in s.split():
            print(statement)


if __name__ == '__main__':
    unittest.main()
