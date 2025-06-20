from api import DummyJSONClient
from unittest.mock import patch

# Test class initialization
def test_client_init():
    '''Test the initialization of the DummyJSONClient class'''
    client = DummyJSONClient()
    assert client.base_url == "https://dummyjson.com/recipes"

def test_get_recipes():
    '''Test the get_users method of the DummyJSONClient class'''
    client = DummyJSONClient()
    recipes = client.get_recipes()
    assert recipes is not None

# Test get_users for status code that is not 200
def test_get_recipe_bad_status():
    '''Test the get_users method of the DummyJSONClient class with a bad status code'''
    client = DummyJSONClient()
    # Mock the requests.get method to return a status code of 404
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        recipes = client.get_recipes()
        assert recipes is None

def test_get_single_recipe():
    '''Test the get_single_recipe method of the DummyJSONClient class'''
    client = DummyJSONClient()
    recipes = client.get_single_recipe(2)
    assert recipes is not None
    assert recipes["id"] == 2

# Test get_user_by_id for status code that is not 200
def test_get_single_recipe_bad_status():
    '''Test the get_single_recipe method of the DummyJSONClient class with a bad status code'''
    client = DummyJSONClient()
    # Mock the requests.get method to return a status code of 404
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        recipe = client.get_single_recipe(2)
        assert recipe is None

def test_create_recipe():
    '''Test the create_recipe method of the DummyJSONClient class'''
    client = DummyJSONClient()
    data = {
        "name": "Chocolate Chip Pancakes",
        "ingredients": ["flour", "milk", "eggs", "chocolate chips"],
        "instructions": "Mix ingredients, cook on skillet until golden brown.",
        "prepTimeMinutes": 10,
        "cookTimeMinutes": 5,
        "cuisine": "American",
        "mealType": ["breakfast"]
    }
    new_recipe = client.create_recipe(data)
    assert new_recipe is not None
    assert new_recipe["name"] == "Chocolate Chip Pancakes"
    assert new_recipe["cuisine"] == "American"

# Test create_recipe for status code that is not 201
def test_create_recipe_bad_status():
    '''Test the create_recipe method of the DummyJSONClient class with a bad status code'''
    client = DummyJSONClient()
    data = {
        "name": "Chocolate Chip Pancakes",
        "ingredients": ["flour", "milk", "eggs", "chocolate chips"],
        "instructions": "Mix ingredients, cook on skillet until golden brown.",
        "prepTimeMinutes": 10,
        "cookTimeMinutes": 5,
        "cuisine": "American",
        "mealType": ["breakfast"]
    }
    # Mock the requests.post method to return a status code of 400
    with patch("requests.post") as mock_post:
        mock_post.return_value.status_code = 400
        new_recipe = client.create_recipe(data)
        assert new_recipe is None

def test_update_recipe():
    '''Test the create_user method of the DummyJSONClient class'''
    client = DummyJSONClient()
    update_data = {
        "name": "Updated Pancake Recipe",
        "prepTimeMinutes": 15
    }
    new_recipe = client.update_recipe(update_data, 3)
    assert new_recipe is not None
    assert new_recipe["name"] == "Updated Pancake Recipe"
    assert new_recipe["prepTimeMinutes"] == 15

# Test update_user for status code that is not 200
@patch('api.requests.put')
def test_update_recipe_error(mock_put):
    '''Test the create_user method of the DummyJSONClient class with an error response'''
    mock_put.return_value.status_code = 404
    client = DummyJSONClient()
    update_data = {
        "name": "Updated Pancake Recipe",
        "prepTimeMinutes": 15
    }
    new_recipe = client.update_recipe(update_data, 3)
    assert new_recipe is None

# Test delete_recipe
def test_delete_recipe():
    '''Test the delete_recipe method of the DummyJSONClient class'''
    client = DummyJSONClient()
    deleted = client.delete_recipe(3)
    assert deleted is True

# Test delete_user for status code that is not 200
@patch('api.requests.delete')
def test_delete_recipe_error(mock_delete):
    '''Test the delete_user method of the DummyJSONClient class with an error response'''
    mock_delete.return_value.status_code = 404
    client = DummyJSONClient()
    deleted = client.delete_recipe(3)
    assert deleted is False