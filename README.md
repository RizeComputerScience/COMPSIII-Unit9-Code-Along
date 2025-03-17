# COMPS III: Unit 8 Code Along

## Overview

In the last unit, we built a Reqres class that could send GET and POST requests to the [Reqres API](https://reqres.in/). We were able to build a class that could get all users, get a user for a specific ID, and send information to create a new user. However, this is only half of the CRUD functionality that we need because we also need to be able to modify and delete users as well.

By the end of this code along, our `Reqres` class will have full CRUD functionality to perform `GET`, `POST`, `PUT`, and DELETE `requests`.


# Local Terminal
1. In your terminal run the command:
```bash
pip install requests
```

# VS Code - `api.py`
2. At the top of `api.py`, import the `requests` library.
3. Inside the `ReqresAPIClient`, create an `update_user(self, user_id, name, job)` method that does the following: 
    - Create a dictionary with the name and the job in the format 
    ```python
    {
        “name”: VALUE_OF_NAME, 
        “job”: VALUE_OF_JOB
    }
    ```
    - Make a `PUT` request to the users endpoint with the data. The updated url to send your request to should look like `{base_url}/users/{user_id}`. 
    - Return the JSON response if the status code is 200. Otherwise, return `None`.
4. Run the tests! `test_update_user` and `test_update_user_error` tests should now be passing.

# VS Code - `main.py`
5. Create an instance of the `ReqresAPIClient`. Call `update_user` and observe the outputs.

# VS Code - `api.py`
6. Inside the `ReqresAPIClient`, create a `delete_user(self, user_id)` method that does the following: 
    - Make a `DELETE` request to the user endpoint with the specified user ID in the format `{base_url}/users/{user_id}`.
    - Return `True` if the status code is 204 (i.e. no content). Otherwise, return `False`.
7. Run the tests! `test_delete_user` and `test_delete_user_error` tests should now be passing.

# VS Code - `main.py`
8. Create an instance of the `ReqresAPIClient`. Call `delete_user` and observe the outputs.