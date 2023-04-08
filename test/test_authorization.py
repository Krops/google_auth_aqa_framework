import pytest


@pytest.mark.parametrize(
    "github_api",
    [
        ({"token": " "},
         {"token": "ghp_Ap6hxigjMlo059NsSUmRMmoJwPGrFe0FGEMF"},),
    ],
    indirect=True,
)
def test_not_authorized(github_api):
    """
    Test 1: Unauthorized request
    Test 2: Invalid token"""
    response = github_api.get_user()
    assert response.status_code == 401


def test_valid_token(github_api):
    """Test 3: Valid token"""
    response = github_api.get_user()
    assert response.status_code == 200
    assert response.json()['login'] == 'Krops'


def test_access_to_repo(github_api):
    """Test 4: Access private repo with valid token"""
    response = github_api.get_repo('Krops', 'JoyreactorParser')
    assert response.status_code == 200


@pytest.mark.parametrize(
    "github_api",
    [
        ({"token": "ghp_Ap6hxigjMlo059NsSUmRMmoJwPGrFe0FGEMF"},),
    ],
    indirect=True,
)
def test_access_to_repo_invalid_token(github_api):
    """Test 5: Access private repo with invalid token"""
    response = github_api.get_repo('Krops', 'JoyreactorParser')
    assert response.status_code == 401


def test_access_non_existent_repo(github_api):
    """Test 6: Access non-existent repo with valid token"""
    response = github_api.get_repo('Krops', 'JoyreactorParsers')
    assert response.status_code == 404
