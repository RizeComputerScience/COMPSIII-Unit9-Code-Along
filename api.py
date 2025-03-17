# Code from last unit
import requests

class ReqresAPIClient:
    def __init__(self, base_url="https://reqres.in/api"):
        self.base_url = base_url
    
    def get_users(self, page=1):
        response = requests.get(f"{self.base_url}/users?page={page}")
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def get_user_by_id(self, user_id):
        response = requests.get(f"{self.base_url}/users/{user_id}")
        if response.status_code == 200:
            return response.json()['data']
        else:
            return None
    
    def create_user(self, name, job):
        data = {
            "name": name,
            "job": job
        }
        response = requests.post(f"{self.base_url}/users", data)
        if response.status_code == 201:
            return response.json()
        else:
            return None
    # End of code from last unit

    # Start your code for this unit here
     # Create an update_user method that updates the user with the specified ID
    def update_user(self, user_id, name, job):
        # Create a dictionary with the name and job
        data = {
            "name": name,
            "job": job
        }
        # Make a PUT request to the users endpoint with the data
        response = requests.put(f"{self.base_url}/users/{user_id}", data)
        # Return the JSON response if the status code is 200 (OK). Otherwise, return None
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    # Create a delete_user method that deletes the user with the specified ID
    def delete_user(self, user_id):
        # Make a DELETE request to the user endpoint with the specified user ID
        response = requests.delete(f"{self.base_url}/users/{user_id}")
        # Return True if the status code is 204 (No Content). Otherwise, return False
        if response.status_code == 204:
            return True
        else:
            return False