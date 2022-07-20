import requests


def get(url, params=None):
    return requests.get(url, params).json()


def post(url, json=None, data=None):
    return requests.post(url, data, json).json()
