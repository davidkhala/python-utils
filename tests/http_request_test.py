import unittest

from davidkhala.http_request import Request

http_bin = 'https://httpbin.org/'


class TestHttpBin(unittest.TestCase):
    def test_your_ip(self):
        url = http_bin + 'ip'
        request = Request(url)
        response = request.get()
        print('Your IP is {0}'.format(response['origin']))

    def test_basic_auth(self):
        username = 'username'
        password = 'password'
        url = http_bin + f'basic-auth/{username}/{password}'
        auth = {
            'username': username,
            'password': password
        }

        request = Request(url, auth)
        response = request.get()
        assert response['authenticated'] == True
        assert response['user'] == username

    def test_bearer(self):
        url = http_bin + 'bearer'
        token = 'YW55'
        auth = {
            'bearer': token
        }
        request = Request(url, auth)
        response = request.get()
        assert response['authenticated'] == True
        assert response['token'] == token

    def test_get_with_load(self):
        url = http_bin + 'get'
        request = Request(url)
        payload = {'things': 2, 'total': 25}
        r = request.get(payload)
        print(r)

    def test_post(self):
        url = http_bin + 'post'
        request = Request(url)
        payload = {'username': 'Olivia', 'password': '123'}
        r = request.post(payload)
        print(r)

    def test_upload(self):
        url = http_bin + 'post'

        with open('tests/data/dummy.txt') as f:
            files = {'file': f.read()}
        request = Request(url)
        r = request.post(None, files)
        print(r)


if __name__ == '__main__':
    unittest.main()
