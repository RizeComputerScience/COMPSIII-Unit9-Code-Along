from api import ReqresAPIClient
from unittest.mock import patch

# Test class initialization
def test_client_init():
    '''Test the initialization of the ReqresAPIClient class'''
    client = ReqresAPIClient()
    assert client.base_url == "https://reqres.in/api"

def test_get_users():
    '''Test the get_users method of the ReqresAPIClient class'''
    client = ReqresAPIClient()
    users = client.get_users()
    assert users is not None

# Test get_users for status code that is not 200
def test_get_users_bad_status():
    '''Test the get_users method of the ReqresAPIClient class with a bad status code'''
    client = ReqresAPIClient()
    # Mock the requests.get method to return a status code of 404
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        users = client.get_users()
        assert users is None

def test_get_user_by_id():
    '''Test the get_user_by_id method of the ReqresAPIClient class'''
    client = ReqresAPIClient()
    user = client.get_user_by_id(2)
    assert user is not None
    assert user["id"] == 2

# Test get_user_by_id for status code that is not 200
def test_get_user_by_id_bad_status():
    '''Test the get_user_by_id method of the ReqresAPIClient class with a bad status code'''
    client = ReqresAPIClient()
    # Mock the requests.get method to return a status code of 404
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        user = client.get_user_by_id(2)
        assert user is None

def test_create_user():
    '''Test the create_user method of the ReqresAPIClient class'''
    client = ReqresAPIClient()
    new_user = client.create_user("Alice Smith", "Developer")
    assert new_user is not None
    assert new_user["name"] == "Alice Smith"
    assert new_user["job"] == "Developer"

# Test create_user for status code that is not 201
def test_create_user_bad_status():
    '''Test the create_user method of the ReqresAPIClient class with a bad status code'''
    client = ReqresAPIClient()
    # Mock the requests.post method to return a status code of 400
    with patch("requests.post") as mock_post:
        mock_post.return_value.status_code = 400
        new_user = client.create_user("Alice Smith", "Developer")
        assert new_user is None

def test_update_user():
    '''Test the create_user method of the ReqresAPIClient class'''
    client = ReqresAPIClient()
    new_user = client.update_user(3, "Alice Smith", "Developer")
    assert new_user is not None
    assert new_user["name"] == "Alice Smith"
    assert new_user["job"] == "Developer"

# Test update_user for status code that is not 200
@patch('api.requests.put')
def test_update_user_error(mock_put):
    '''Test the create_user method of the ReqresAPIClient class with an error response'''
    mock_put.return_value.status_code = 404
    client = ReqresAPIClient()
    new_user = client.update_user(3, "Alice Smith", "Developer")
    assert new_user is None

# Test delete_user
def test_delete_user():
    '''Test the delete_user method of the ReqresAPIClient class'''
    client = ReqresAPIClient()
    deleted = client.delete_user(3)
    assert deleted is True

# Test delete_user for status code that is not 204
@patch('api.requests.delete')
def test_delete_user_error(mock_delete):
    '''Test the delete_user method of the ReqresAPIClient class with an error response'''
    mock_delete.return_value.status_code = 404
    client = ReqresAPIClient()
    deleted = client.delete_user(3)
    assert deleted is False