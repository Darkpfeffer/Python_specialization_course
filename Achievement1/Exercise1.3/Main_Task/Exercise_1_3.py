recipes_list = []
ingredients_list = []

def take_recipe():
    name = str(input("Enter the name of the recipe: "))
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input( \
        "Enter the ingredients' name (separate the items with commas and space): "\
            ).split(", ")

    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    for ingredient in recipe["ingredients"]:
        if ingredient.lower() in ingredients_list:
            continue
        else:
            ingredients_list.append(ingredient.lower())

    recipe_time = recipe["cooking_time"] 
    recipe_length = len(recipe["ingredients"])

    if (recipe_time < 10) and (recipe_length < 4):
        recipe.update({'difficulty': 'Easy'})

    elif (recipe_time < 10) and (recipe_length >= 4):
        recipe.update({'difficulty': 'Medium'})

    elif (recipe_time >= 10) and (recipe_length < 4):
        recipe.update({'difficulty': 'Intermediate'})

    elif (recipe_time >= 10) and (recipe_length >= 4):
        recipe.update({'difficulty': 'Hard'})

    else:
        print("something went wrong")
    
    recipes_list.append(recipe)

n = int(input("How many recipes would you like to add?: "))

for recipe in range(n):
    take_recipe()

for recipe in recipes_list:
    print("------------------------------")
    print("Recipe: " + recipe["name"])
    print("Cooking Time (min): " + str(recipe["cooking_time"]))
    print("Ingredients: ")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty level: " + recipe["difficulty"])
    print("------------------------------")

ingredients_list.sort()

print("Ingredients Available Across All Recipes")
print("----------------------------------------")
for ingredient in ingredients_list:
    print(ingredient)
print("----------------------------------------")