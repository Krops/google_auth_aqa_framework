def test_create_pull_request(github_api, clean_pull):
    """Create a pull request"""
    data = {
        "title": "Test PR",
        "head": "develop_2",
        "base": "master",
        "body": "Some text"
    }
    response = github_api.add_pull_request('Krops', 'JoyreactorParser', data)
    assert response.status_code == 201, response.text
    clean_pull.append({"owner": "Krops", "repo": "JoyreactorParser", 'pull_numb': response.json()['number']})


def test_delete_pull_request(github_api, add_test_pull):
    """Delete a pull request"""
    pull_request_number = add_test_pull
    response = github_api.remove_pull_request('Krops', 'JoyreactorParser', pull_request_number)
    assert response.status_code == 200, response.text


def test_approve_pull_request(github_api, add_test_pull, clean_pull):
    """ Approve a pull request"""
    pull_request_number = add_test_pull  # replace with the actual pull request number
    data = {
        "event": "APPROVE"
    }
    response = github_api.approve_pull_request('Krops', 'JoyreactorParser', pull_request_number, data)
    clean_pull.append({"owner": "Krops", "repo": "JoyreactorParser", 'pull_numb': pull_request_number})
    assert response.status_code == 422, response.text

