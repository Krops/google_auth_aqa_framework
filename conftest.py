import pytest
from api.github import GitHubAPI
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