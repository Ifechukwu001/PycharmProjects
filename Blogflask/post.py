import requests


class Post:

    def __init__(self, url):
        self.post_url = url
        self.response = requests.get(self.post_url)
        self.response_data = self.response.json()

