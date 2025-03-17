from api import *

# Test outputs
client = ReqresAPIClient()

# PUT Demonstration
print("\n--- PUT Requests ---")
updated_user = client.update_user(2, "Alice Johnson", "Designer")
print("Updated User:")
print(updated_user)

# DELETE Demonstration
print("\n--- DELETE Requests ---")
deleted = client.delete_user(2)
print("User Deleted:", deleted)