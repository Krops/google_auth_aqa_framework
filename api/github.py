import requests
import os
from utils.constants import GITHUB_USER_URL, GITHUB_REPO_URL, GITHUB_USER_REPOS_URL, GITHUB_REPO_BRANCHES_URL, \
    GITHUB_REPO_PULLS_URL, GITHUB_REPO_PULLS_NUM_URL, GITHUB_REPO_PULLS_NUM_REVIEWS_URL


class GitHubAPI:
    def __init__(self):
        self.set_token()

    def get_user(self):
        response = requests.get(GITHUB_USER_URL, headers=self.headers)
        return response

    def get_repo(self, owner, repo):
        response = requests.get(GITHUB_REPO_URL.format(owner=owner, repo=repo), headers=self.headers)
        return response

    def get_repos(self):
        response = requests.get(GITHUB_USER_REPOS_URL, headers=self.headers)
        return response

    def get_repo_branches(self, owner, repo):
        response = requests.get(GITHUB_REPO_BRANCHES_URL.format(owner=owner, repo=repo), headers=self.headers)
        return response

    def get_repo_pulls(self, owner, repo):
        response = requests.get(GITHUB_REPO_PULLS_URL.format(owner=owner, repo=repo), headers=self.headers)
        return response

    def get_repo_pulls_numb(self, owner, repo, pull_numb):
        response = requests.get(GITHUB_REPO_PULLS_NUM_URL.format(owner=owner, repo=repo, pull_numb=pull_numb),
                                headers=self.headers)
        return response

    def get_repo_pulls_numb_reviews(self, owner, repo, pull_numb):
        response = requests.get(GITHUB_REPO_PULLS_NUM_REVIEWS_URL.format(owner=owner, repo=repo, pull_numb=pull_numb),
                                headers=self.headers)
        return response

    def add_pull_request(self, owner, repo, data):
        response = requests.post(GITHUB_REPO_PULLS_URL.format(owner=owner, repo=repo), headers=self.headers, json=data)
        return response

    def remove_pull_request(self, owner, repo, pull_numb):
        response = requests.patch(GITHUB_REPO_PULLS_NUM_URL.format(owner=owner, repo=repo, pull_numb=pull_numb),
                                  json={"state": "closed"},
                                  headers=self.headers)
        return response

    def approve_pull_request(self, owner, repo, pull_numb, data):
        response = requests.post(GITHUB_REPO_PULLS_NUM_REVIEWS_URL.format(owner=owner, repo=repo, pull_numb=pull_numb),
                                 headers=self.headers, json=data)
        return response

    def set_token(self, token: str = ''):
        if not len(token):
            token = os.environ.get("GITHUB_TOKEN", "")
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
