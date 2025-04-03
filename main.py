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

# PUT Demonstration
print("\n--- PUT Requests ---")
updated_user = client.update_user(2, "Alice Johnson", "Designer")
print("Updated User:")
print(updated_user)

# DELETE Demonstration
print("\n--- DELETE Requests ---")
deleted = client.delete_user(2)
print("User Deleted:", deleted)