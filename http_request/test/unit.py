import unittest
from http_request import get, post


class TestHttpBin(unittest.TestCase):
    def test_your_ip(self):
        response = get('https://httpbin.org/ip')
        print('Your IP is {0}'.format(response['origin']))

    def test_get_with_load(self):
        payload = {'things': 2, 'total': 25}
        r = get('https://httpbin.org/get', payload)
        print(r)

    def test_post(self):
        payload = {'username': 'Olivia', 'password': '123'}
        r = post('https://httpbin.org/post', payload)
        print(r)


if __name__ == '__main__':
    unittest.main()
