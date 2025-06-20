# Code from last unit
import requests

class DummyJSONClient:
    def __init__(self, base_url="https://dummyjson.com/recipes"):
        self.base_url = base_url
    
    def get_recipes(self):
        response = requests.get(f"{self.base_url}/")
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def get_single_recipe(self, recipe_id):
        response = requests.get(f"{self.base_url}/{recipe_id}")
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def create_recipe(self, data):
        response = requests.post(f"{self.base_url}/add", data)
        print(response.status_code)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    # Create an update_recipe method that updates the recipe with the specified ID
    def update_recipe(self, data, id):
        # Make a PUT request to the recipes endpoint with the data
        response = requests.put(f"{self.base_url}/{id}", json=data)
        if response.status_code == 200:
            return response.json() 
        else: 
            None

    # Create a delete_user method that deletes the user with the specified ID
    def delete_recipe(self, recipe_id):
        # Make a DELETE request to the user endpoint with the specified user ID
        response = requests.delete(f"{self.base_url}/{recipe_id}")
        # Return True if the status code is 200 (No Content). Otherwise, return False
        
        if response.status_code == 200:
            return True
        else:
            return False