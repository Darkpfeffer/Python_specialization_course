import pickle

with open('recipe_binary.bin', 'rb') as my_file: 
    recipe = pickle.load(my_file)
    
print('Recipe: ' + recipe['Name'])
print('Cooking Time: ' + recipe['Cooking Time'])
print('Ingredients: ')
for Ingredient in recipe['Ingredients']:
    print(Ingredient)
print('Difficulty: ' + recipe['Difficulty'])