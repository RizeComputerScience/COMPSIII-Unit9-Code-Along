from api import *

# Test outputs
client = ReqresAPIClient()

print("--- GET Requests ---")
users = client.get_users()

print(users)
print(users["data"][0]["first_name"])
specific_user = client.get_user_by_id(2)
print("Specific User:", specific_user)

# POST Demonstration
print("\n--- POST Requests ---")
new_user = client.create_user("Alice Smith", "Developer")
print("Created User:", new_user)