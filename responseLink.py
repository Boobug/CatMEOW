import requests


def get_response(legends_url):
    response = requests.get(legends_url)
    return response.url



