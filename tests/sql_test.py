import unittest

from davidkhala.utils.sql import SQL
from davidkhala.utils.syntax import fs


class SQLParseTestCase(unittest.TestCase):
    def test_split(self):
        sql_content = fs.read('tests/data/test.sql')
        s = SQL(sql_content)
        for statement in s.split():
            print(statement)


if __name__ == '__main__':
    unittest.main()
