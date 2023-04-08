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
