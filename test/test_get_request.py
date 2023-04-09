from utils.constants import GITHUB_REPO_PULLS_NUM_URL


def test_get_all_repositories(github_api):
    """Get all user repositories"""
    response = github_api.get_repos()
    assert response.status_code == 200, response.text
    assert len(response.json()) == 30, response.text


def test_get_all_branches(github_api):
    """Get all branches of a repository"""
    response = github_api.get_repo_branches('Krops', 'JoyreactorParser')
    assert response.status_code == 200, response.text
    assert len(response.json()) > 0, response.text
    assert response.json()[-1]['name'] == 'test_master', response.text


def test_get_all_pull_requests(github_api):
    """Get all pull requests of a repository"""
    response = github_api.get_repo_pulls('Krops', 'JoyreactorParser')
    assert response.status_code == 200, response.text
    assert len(response.json()) > 0, response.text
    assert response.json()[0]['url'] == GITHUB_REPO_PULLS_NUM_URL.format(owner='Krops', repo='JoyreactorParser',
                                                                         pull_numb=1)
