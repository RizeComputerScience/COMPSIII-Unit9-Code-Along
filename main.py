from api import *

# Test outputs
client = DummyJSONClient()

print("--- GET Requests ---")
recipes = client.get_recipes()
print(recipes["recipes"][0]["name"])

specific_recipe = client.get_single_recipe(2)
print(specific_recipe['ingredients'])

# # POST Demonstration
print("\n--- POST Requests ---")
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
print("Created Recipe:", new_recipe)

# PUT Demonstration
print("\n--- PUT Requests ---")
update_data = {
    "name": "Updated Pancake Recipe",
    "prepTimeMinutes": 15
}
updated_recipe = client.update_recipe(update_data, 2)
print("Updated Recipe:")
print(updated_recipe)

# # DELETE Demonstration
print("\n--- DELETE Requests ---")
deleted = client.delete_recipe(2)
print("Recipe Deleted:", deleted)