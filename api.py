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



