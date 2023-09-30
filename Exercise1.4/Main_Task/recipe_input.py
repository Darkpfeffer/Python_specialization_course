import pickle
import os

def take_recipe():
    recipe_name = str(input("Enter the name of the recipe: "))
    cooking_time = int(input\
        ("Enter the cooking time in minutes (accepts only numbers): "))
    ingredients = str(input("Enter the ingredients of the recipe "\
                "(Separate the ingredients with a comma(,) and space): ")).split(", ")
    
    #checking recipe difficulty
    def calc_difficulty():
        short_cooking_time = cooking_time < 10
        long_cooking_time = cooking_time >= 10
        few_ingredients = len(ingredients) < 4
        numerous_ingredients = len(ingredients) >= 4

        if short_cooking_time and few_ingredients:
            return 'Easy'
        
        elif short_cooking_time and numerous_ingredients:
            return 'Medium'
        
        elif long_cooking_time and few_ingredients:
            return 'Intermediate'
        
        elif long_cooking_time and numerous_ingredients:
            return 'Hard'
    
    #Creating a dictionary from the inputs
    recipe = {
        'name': recipe_name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        #checks and adds the difficulty
        'difficulty': calc_difficulty()
    }

    return recipe

#user inputs the desired file name
user_file = input("Enter the name of the file: ")

#a new data variable will be created after error occurence 
new_data = {
        'recipes_list': [],
        'all_ingredients': []
    }

try:
    with open(user_file, 'rb') as my_file:
        data = pickle.load(my_file)
    print(data)

except FileNotFoundError:
    print("File is not found")
    data = new_data

except:
    print("Some error occured")
    data = new_data

else:
    my_file.close()

finally:
    recipes_list = [] 
    recipes_list.extend(data['recipes_list'])

    all_ingredients = []
    all_ingredients.extend(data['all_ingredients'])

recipe_counter = input("How many recipes would you like to add?: ")

i = 0
while i < int(recipe_counter):
    print("----------------------------------------")
    #Clear the recipe variable
    recipe = {}

    recipe = take_recipe()

    recipes_list.append(recipe)

    #Add ingredients to the all_ingredient list,
    #if the ingredient is not already present.
    for ingredient in recipe['ingredients']:
        if ingredient.lower() in all_ingredients:
            continue
        else:
            all_ingredients.append(ingredient.lower())

    i += 1

#Updating the data variable with the new lists
data = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
}

#Adding the new data variable to the storage file
with open(user_file, 'wb') as my_file:
    pickle.dump(data, my_file)
    print("----------------------------------------")
    print("The recipes are added to the file.")