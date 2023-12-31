import pickle

def display_recipe(single_recipe):
    print("Name: " + single_recipe['name'])
    print("Cooking time (minutes): "+ str(single_recipe['cooking_time']))
    print("Difficulty: " + single_recipe['difficulty'])
    print("Ingredients: ")
    for ingredient in single_recipe['ingredients']:
        print(ingredient)

def search_ingredient(data):
    #Adding index numbers to the ingredients
    all_ingredients = list(enumerate(data['all_ingredients']))
    for ingredient in all_ingredients:
        print(ingredient)

    try:
        picked_index = int(input("Choose an ingredient (Write it's index number): "))
        ingredient_searched = all_ingredients[picked_index]

    except ValueError:
        print("Input only accepts numbers. Please try again!")

    except IndexError: 
        print("Wrong index number given. Please try again!")
    
    except:
        print("Something went wrong.")

    else:
        for recipe in data['recipes_list']:
            for ingredient in recipe['ingredients']:
                if ingredient_searched[1] == ingredient.lower():
                    print("----------------------------------------")
                    #Prints every detail of the recipe
                    display_recipe(recipe)
                    print("----------------------------------------")

                else:
                    continue

user_file = input("Enter storage file name (with '.bin' extension): ")

try:
    with open(user_file, 'rb') as recipe_storage:
        data = pickle.load(recipe_storage)
except FileNotFoundError:
        print("File has not been found. Please try again!")
except:
    print("Something went wrong.")
else:
    search_ingredient(data)