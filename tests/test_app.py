from unittest.mock import patch
from api import ReqresAPIClient

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