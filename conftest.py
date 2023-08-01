import os

import pytest
from playwright.sync_api import Page

from api.github import GitHubAPI
from pages.gmail_login import GmailLoginPage
from utils.common import get_request_param_value_by_name


@pytest.fixture(scope="session")
def github_token():
    api = GitHubAPI()
    return api


@pytest.fixture(scope="function")
def github_api(request: pytest.FixtureRequest, github_token):
    params = getattr(request, "param", ())
    token = get_request_param_value_by_name(params, "token")
    github_token.set_token(token)
    yield github_token
    github_token.set_token()


@pytest.fixture(scope="function")
def clean_pull(github_token):
    pulls = []
    yield pulls
    for pull in pulls:
        response = github_token.remove_pull_request(**pull)
        if response.status_code != 200:
            raise Exception(response.text)


@pytest.fixture(scope="function")
def add_test_pull(github_token):
    data = {
        "title": "Test PR",
        "head": "develop_2",
        "base": "master",
        "body": "Some text"
    }
    response = github_token.add_pull_request('Krops', 'JoyreactorParser', data)
    if response.status_code != 201:
        raise Exception(response.text)
    return response.json()['number']


@pytest.fixture
def google_auth_page(base_url, page: Page) -> GmailLoginPage:
    sim_eng_page = GmailLoginPage(base_url, page)

    yield sim_eng_page


@pytest.fixture
def email(request: pytest.FixtureRequest) -> str:
    return request.param


@pytest.fixture
def password_by_user(email: str) -> str:
    get_password_by_user = {
        "andrekropes@gmail.com": os.environ.get("GMAIL_PASSWORD")
    }
    yield get_password_by_user.get(email)
