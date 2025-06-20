# COMPS III: Unit 9 Code Along

## Overview

We’ll be building a class that can execute GET, POST, PUT, and DELETE requests to an endpoint that provides users with various recipes. We will use the [Dummy JSON Recipe API](https://dummyjson.com/docs/recipes) for our requests because it is a simple API that is designed specifically for practicing your API skills! 

By the end of this code along, our `DummyJSONClient` class will have full CRUD functionality to perform `GET`, `POST`, `PUT`, and `DELETE` requests.

### Local Terminal
1. In your terminal run the command:
```bash
pip install requests
```

### VS Code - `api.py`
2. At the top of `api.py`, import the `requests` library.
3. Create a class to encapsulate the API client called `DummyJSONClient`. We are using a class to encapsulate the related methods and maintain state (base URL).
4. The `DummyJSONClient` has the following attributes set by the constructor:
    - `base_url`: The endpoint for the request. Initialized with a value of "https://dummyjson.com/recipes" if no value is provided.
5. Run the tests! The `test_client_init` test should now be passing.
6. Inside the `DummyJSONClient` you created, declare a `get_recipes(self)` method that does the following:
    - Make a `GET` request to the `base_url` endpoint.
    - Return the JSON response if the status code is `200`. Otherwise, return `None`
7. Run the tests! The `test_get_recipes` and  `test_get_recipes_bad_status` tests should now be passing.

### VS Code - `main.py`
8. Create an instance of the `DummyJSONClient` class.
9. Call `get_recipes` and print the output to your terminal to observe the response.

### VS Code - `api.py`
10. Inside the `DummyJSONClient` you created, declare a `get_single_recipe(self, recipe_id)` method that does the following:
    - Make a `GET` request to the recipe endpoint with the specified recipe `recipe_id`. The updated url to send your request to should look like `{base_url}/{recipe_id}`.
    - Return the JSON response if the status code is 200. Otherwise, return None
11. Run the tests! The `test_get_single_recipe` and `test_get_single_recipe_bad_status` should now be passing.

### VS Code - `main.py`
12. For your instance of the `DummyJSONClient` class, call `get_single_recipe` for an id of your choice. Print the output to the terminal.

### VS Code - `api.py`
13. Inside the `DummyJSONClient` you created, declare a `create_recipe(self, data)` method that does the following:
    - Accepts `data` to be sent formatted as a dictionary as an argument. An example dictionary is shown below.
    ```python
    {
        "name": "Chocolate Chip Pancakes",
        "ingredients": ["flour", "milk", "eggs", "chocolate chips"],
        "instructions": "Mix ingredients, cook on skillet until golden brown.",
        "prepTimeMinutes": 10,
        "cookTimeMinutes": 5,
        "cuisine": "American",
        "mealType": ["breakfast"]
    }
    ```
    - Make a `POST` request to the recipes endpoint with the data. The updated url to send your request to should look like `{base_url}/add`.
    - Return the JSON response if the status code is 200. Otherwise, return None.
14. Run the tests! The `test_create_recipe` and `test_create_recipe_bad_status` should now be passing.

### VS Code - `main.py`
15. For your instance of the `DummyJSONClient` class, call `create_recipe` for a recipe of your choice or the data provided above. Print the output to the terminal.


### VS Code - `api.py`
16. Inside the `DummyJSONClient`, create an `update_recipe(self, data, id)` method that does the following: 
    - Accepts `data` to be sent formatted as a dictionary as an argument. An example dictionary is shown below.
    ```python
    {
        "name": "Updated Pancake Recipe",
        "prepTimeMinutes": 15
    }
    ```
    - Make a `PUT` request to the recipes endpoint with the data. The updated url to send your request to should look like `{base_url}/{id}`. Be sure to pass the data as JSON.
    - Return the JSON response if the status code is 200. Otherwise, return `None`.
17. Run the tests! `test_update_recipe` and `test_update_recipe_error` tests should now be passing.

### VS Code - `main.py`
18. Create an instance of the `DummyJSONClient`. Call `update_recipe` using the data above and observe the outputs.

### VS Code - `api.py`
19. Inside the `DummyJSONClient`, create a `delete_recipe(self, recipe_id)` method that does the following: 
    - Make a `DELETE` request to the recipe endpoint with the specified recipe ID in the format `{base_url}/{recipe_id}`.
    - Return `True` if the status code is 200. Otherwise, return `False`.
20. Run the tests! `test_delete_recipe` and `test_delete_recipe_error` tests should now be passing.

### VS Code - `main.py`
21. Create an instance of the `DummyJSONClient`. Call `delete_recipe` and observe the outputs.