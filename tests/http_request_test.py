import unittest

from davidkhala.http_request import Request

http_bin = 'https://httpbin.org/'


class TestHttpBin(unittest.TestCase):
    def test_your_ip(self):
        url = http_bin + 'ip'
        request = Request()
        response = request.request(url, 'GET')
        print('Your IP is {0}'.format(response['origin']))

    def test_basic_auth(self):
        username = 'username'
        password = 'password'
        url = http_bin + f'basic-auth/{username}/{password}'
        auth = {
            'username': username,
            'password': password
        }

        request = Request(auth)
        response = request.request(url, 'GET')
        assert response['authenticated'] == True
        assert response['user'] == username

    def test_bearer(self):
        url = http_bin + 'bearer'
        token = 'YW55'
        auth = {
            'bearer': token
        }
        request = Request(auth)
        response = request.request(url, 'GET')
        assert response['authenticated'] == True
        assert response['token'] == token

    def test_get_with_query_params(self):
        url = http_bin + 'get'
        request = Request()
        payload = {'things': 2, 'total': 25}
        r = request.request(url, 'GET', payload)
        print(r)

    def test_post(self):
        url = http_bin + 'post'
        request = Request()
        payload = {'username': 'Olivia', 'password': '123'}
        r = request.request(url, 'POST', payload)
        print(r)

    def test_upload(self):
        url = http_bin + 'post'

        with open('tests/data/dummy.txt') as f:
            files = {'file': f.read()}
        request = Request()
        r = request.request(url, 'POST', data=files)
        print(r)


if __name__ == '__main__':
    unittest.main()
