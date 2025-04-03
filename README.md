# COMPS III: Unit 8 Code Along

## Overview
Over the next 2 weeks, we’ll be building a class that can execute GET, POST, PUT, and DELETE requests to a specified endpoint. We will use the [Reqres API](https://reqres.in/) for our requests because it is a simple API that is designed specifically for practicing your API skills! 

By the end of this code along, our `Reqres` class will have full CRUD functionality to perform `GET`, `POST`, `PUT`, and `DELETE` requests.

# Local Terminal
1. In your terminal run the command:
```bash
pip install requests
```

# VS Code - `api.py`
2. At the top of `api.py`, import the `requests` library.
3. Create a class to encapsulate the API client called `ReqresAPIClient`. We are using a class to encapsulate the related methods and maintain state (base URL).
4. The `ReqresAPIClient` has the following attributes set by the consturctor:
    - `base_url`: The endpoint for the request. Initialized with a value of "https://reqres.in/api" if no value is provided.
5. Run the tests! The `test_client_init` test should now be passing.
6. Inside the `ReqresAPIClient` you created, declare a `get_users(self, page=1)` method that does the following:
    - Make a `GET` request to the `base_url` endpoint and the specified `page`. The updated url to send your request to should look like `{base_url}/users?page={page}`.
    - Return the JSON response if the status code is `200`. Otherwise, return `None`
7. Run the tests! The `test_get_users` and  `test_get_users_bad_status` tests should now be passing.

# VS Code - `main.py`
8. Create an instance of the `ReqresAPIClient` class.
9. Call `get_users` and print the output to your terminal to observe the response.

# VS Code - `api.py`
10. Inside the `ReqresAPIClient` you created, declare a `get_user_by_id(self, user_id)` method that does the following:
    - Make a `GET` request to the user endpoint with the specified user `user_id`. The updated url to send your request to should look like `{base_url}/users/{user_id}`.
    - Return the JSON response if the status code is 200. Otherwise, return None
11. Run the tests! The `test_get_user_by_id` and `test_get_user_by_id_bad_status` should now be passing.

# VS Code - `main.py`
12. For your instance of the `ReqresAPIClient` class, call `get_user_by_id` for an id of your choice. Print the output to the terminal.

# VS Code - `api.py`
13. Inside the `ReqresAPIClient` you created, declare a `create_user(self, name, job)` method that does the following:
    - Create a dictionary with the name and the job in the format
    ```python
    {
        "name": VALUE_OF_NAME,
        "job": VALUE_OF_JOB
    }
    ```
    - Make a `POST` request to the users endpoint with the data. The updated url to send your request to should look like `{base_url}/users/`.
    - Return the JSON response if the status code is 201. Otherwise, return None.
14. Run the tests! The `test_create_user` and `test_create_user_bad_status` should now be passing.

# VS Code - `main.py`
15. For your instance of the `ReqresAPIClient` class, call `create_user` for a user of your choice. Print the output to the terminal.


## VS Code - `api.py`
16. Inside the `ReqresAPIClient`, create an `update_user(self, user_id, name, job)` method that does the following: 
    - Create a dictionary with the name and the job in the format 
    ```python
    {
        “name”: VALUE_OF_NAME, 
        “job”: VALUE_OF_JOB
    }
    ```
    - Make a `PUT` request to the users endpoint with the data. The updated url to send your request to should look like `{base_url}/users/{user_id}`. 
    - Return the JSON response if the status code is 200. Otherwise, return `None`.
17. Run the tests! `test_update_user` and `test_update_user_error` tests should now be passing.

## VS Code - `main.py`
18. Create an instance of the `ReqresAPIClient`. Call `update_user` and observe the outputs.

## VS Code - `api.py`
19. Inside the `ReqresAPIClient`, create a `delete_user(self, user_id)` method that does the following: 
    - Make a `DELETE` request to the user endpoint with the specified user ID in the format `{base_url}/users/{user_id}`.
    - Return `True` if the status code is 204 (i.e. no content). Otherwise, return `False`.
20. Run the tests! `test_delete_user` and `test_delete_user_error` tests should now be passing.

## VS Code - `main.py`
21. Create an instance of the `ReqresAPIClient`. Call `delete_user` and observe the outputs.