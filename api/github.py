import requests
import os


class GitHubAPI:
    def __init__(self):
        self.set_token()

    def get_user(self):
        url = 'https://api.github.com/user'
        response = requests.get(url, headers=self.headers)
        return response

    def get_repo(self, owner, repo):
        url = f'https://api.github.com/repos/{owner}/{repo}'
        response = requests.get(url, headers=self.headers)
        return response

    def set_token(self, token: str = ''):
        if not len(token):
            token = os.environ.get("GITHUB_TOKEN", "")
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }