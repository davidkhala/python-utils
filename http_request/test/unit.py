import unittest
from http_request import Request


class TestHttpBin(unittest.TestCase):
    def test_your_ip(self):
        url = 'https://httpbin.org/ip'
        request = Request(url)
        response = request.get()
        print('Your IP is {0}'.format(response['origin']))

    def test_basic_auth(self):
        #     /basic-auth/{user}/{passwd}
        url = 'https://httpbin.org/basic-auth/username/password'
        auth = {
            'username': 'username',
            'password': 'password'
        }

        request = Request(url, auth)
        response = request.get()
        print(response)

    def test_get_with_load(self):
        url = 'https://httpbin.org/get'
        request = Request(url)
        payload = {'things': 2, 'total': 25}
        r = request.get(payload)
        print(r)

    def test_post(self):
        url = 'https://httpbin.org/post'
        request = Request(url)
        payload = {'username': 'Olivia', 'password': '123'}
        r = request.post(payload)
        print(r)


if __name__ == '__main__':
    unittest.main()
