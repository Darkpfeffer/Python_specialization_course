from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column
from sqlalchemy.types import String, Integer

engine = create_engine("mysql://cf-python:password@localhost/task_database")
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase) :
    pass

class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    cooking_time = Column(Integer)
    ingredients = Column(String(255))
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + " - " + self.name +", " +\
        "Difficulty: " + self.difficulty + ">"
    
    def __str__(self):
        return "\n" + "-"*20 + "\nRecipe name: " + self.name + "\tRecipe ID: " + str(self.id) +\
        "\n\nCooking time: " + str(self.cooking_time) + "\t\tDifficulty: " + self.difficulty +\
        "\n\nIngredients: " + self.ingredients + "\n" + "-"*20 + "\n"

    def calculate_difficulty(self, cooking_time, ingredients):
        short_cooking_time = cooking_time < 10
        long_cooking_time = cooking_time >= 10
        few_ingredients = len(ingredients.split(", ")) < 4
        numerous_ingredients = len(ingredients.split(", ")) >= 4

        if short_cooking_time and few_ingredients:
            self.difficulty =  "Easy"
        elif short_cooking_time and numerous_ingredients:
            self.difficulty =  "Medium"
        elif long_cooking_time and few_ingredients:
            self.difficulty =  "Intermediate"
        elif long_cooking_time and numerous_ingredients:
            self.difficulty =  "Hard"
        else:
            print("Difficulty could not be calculated.")

    def return_ingredients_as_list(self):
        if self.ingredients == "":
            return []
        else:
            return self.ingredients.split(", ")
    
Base.metadata.create_all(engine)

def create_recipe():
    name = input("Enter the name of the recipe (maximal 50 characters): ")
    if len(name) > 50:
        print("\n Error: Recipe name can only be 50 characters long. Returning to main menu.")
        return
    
    cooking_time = input("Enter cooking time in minutes (accepts only numbers): ")
    if not cooking_time.isnumeric():
        print("\nError: Cooking time can only contain numbers. Returning to main menu.")
        return
    
    ingredients = []
    
    number_of_ingredients = input("How many ingredients would you like to add? ")
    if not number_of_ingredients.isnumeric():
        print("\n Error: Ingredient number can contain only numbers. Returning to main menu.")
        return

    i = 0
    temporary_ingredients = ""

    while i < int(number_of_ingredients):
        ingredient_to_add = input("Enter the name of the ingredient: ")
        ingredients.append(ingredient_to_add.lower())

        temporary_ingredients = ", ".join(ingredients)
        print(temporary_ingredients)
        if i < int(number_of_ingredients) - 2:
            print("Remaining characters: " + str(255 - len(temporary_ingredients) - 2))
        elif i < int(number_of_ingredients) - 1:
            print("Remaining characters: " + str(255 - len(temporary_ingredients)))

        i += 1

    ingredients = ", ".join(ingredients)
    if len(ingredients) > 255:
        print("Error: ingredients accepts maximum 255 characters" + 
              " (Characters of ingredient + 2 at every ingredient). Returning to main menu.")
        return
    
    recipe_entry = Recipe(
        name = name,
        cooking_time = cooking_time,
        ingredients = ingredients
    )

    recipe_entry.calculate_difficulty(int(cooking_time), (ingredients))

    session.add(recipe_entry)
    session.commit()

def view_all_recipes():
    all_recipes = session.query(Recipe).all()

    if session.query(Recipe).count() == 0:
        print("There is no recipes in the database. Returning to main menu.")
        return None
    
    for recipe in all_recipes:
        print(recipe)
    
def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("There is no recipes in the database. Returning to main menu.")
        return None
    
    results = []
    
    for recipe in session.query(Recipe).all():
        results.extend(recipe.ingredients.split(", "))
  
    all_ingredients = []
  
    for ingredient in results:
        if not ingredient in all_ingredients:
            all_ingredients.append(ingredient)

    for ingredient in all_ingredients:
        print(all_ingredients.index(ingredient) + 1, "- " + ingredient)

    chosen_ingredient = input("Choose the indexes of the ingredients" + 
                               " you would like to search (separate them with a comma (,)" +
                                 " and a space ( ) ): ").split(", ")
    
    for index in chosen_ingredient:
        if not index.isnumeric():
            print("You can only input numbers. Returning to main menu.")
            return
        elif int(index) > len(all_ingredients):
            print("You can only select index numbers from the list. Returning to main menu.")
            return
    
    search_ingredients = []

    for index in chosen_ingredient:
        search_ingredients.append(all_ingredients[int(index)-1])

    conditions = []

    for ingredient in search_ingredients:
        like_term = "%" + ingredient + "%"
        conditions.append(like_term)
    for condition in conditions:
        for recipe in session.query(Recipe).filter(Recipe.ingredients.like(condition)).all():
            print(recipe)

def edit_recipe():
    if session.query(Recipe).count() == 0:
        print("There is no recipes in the database. Returning to main menu.")
        return
    else:
        results = []
        for recipe in session.query(Recipe).all():
            results.append(str(recipe.id) + " - " + recipe.name)
        
        for recipe in results:
            print(recipe)

    chosen_recipe = input("Enter the ID of the recipe: ")

    if not chosen_recipe.isnumeric():
        print("You can only enter numbers. Returning to main menu.")
        return
    if not any(chosen_recipe in result for result in results):
        print("You can only enter numbers from the list. Returning to main menu.")
        return
    
    recipe_to_edit = session.query(Recipe).filter(Recipe.id.like("%" + chosen_recipe + "%")).one()

    print("\n" + "-"*20 + "\n1 - Recipe name: " + recipe_to_edit.name + "\n" + 
          "2 - Cooking time: " + str(recipe_to_edit.cooking_time) +
          "\n3 - Ingredients: ")
    
    for ingredient in recipe_to_edit.ingredients.split(", "):
        print("- " + ingredient) 
    
    print("\n" + "-" * 20)

    chosen_attribute = input("Enter the index of the recipe information you would like" + 
                             "to update: ")
    if not chosen_attribute.isnumeric():
        print("You can only enter numbers. Returning to main menu.")
        return
    if int(chosen_attribute) > 3 or int(chosen_attribute) < 1:
        print("You can only enter numbers from the list. Returning to main menu.")
        return
    
    if chosen_attribute == "1":
        new_name = input("Enter the new recipe name (maximal 50 characters): ")
        if len(new_name) > 50:
            print("The new name can only be maximal 50 characters long. Returning to main menu.")
            return
        else:
            session.query(Recipe).filter(Recipe.name == recipe_to_edit.name).update(\
                {Recipe.name: new_name})
    
    elif chosen_attribute == "2":
        new_cooking_time = input("Enter new cooking time in minutes (numbers only): ")
        if not new_cooking_time.isnumeric():
            print("The new cooking time must be a number. Returning to main menu.")
            return
        else:
            session.query(Recipe).filter(Recipe.name == recipe_to_edit.name).update(\
                {Recipe.cooking_time: int(new_cooking_time)})
            recipe_to_edit.calculate_difficulty(int(new_cooking_time), recipe_to_edit.ingredients)
    elif chosen_attribute == "3":
        new_ingredients = input("Enter the new recipe ingredients (maximal 255 characters)" + 
                                "(separate them with comma(,) and space ( )): ")
        if len(new_ingredients) > 255:
            print("The new name can only be maximal 255 characters long. Returning to main menu.")
            return
        else:
            session.query(Recipe).filter(Recipe.name == recipe_to_edit.name).update(\
                {Recipe.ingredients: new_ingredients})
            recipe_to_edit.calculate_difficulty(recipe_to_edit.cooking_time, new_ingredients)

    session.commit()

def delete_recipe():
    if session.query(Recipe).count() == 0:
        print("There is no recipes in the database. Returning to main menu.")
        return
    
    session.query(Recipe).all()

    recipe_to_delete = input("Enter the ID of the recipe you would like to delete (numbers only): ")

    if not recipe_to_delete.isnumeric():
        print("You can only enter numbers.")
        return
    else:
        delete_id = session.query(Recipe).filter(Recipe.id == int(recipe_to_delete)).one()

        if delete_id.count() == 0:
            print("Invalid recipe ID entered.")
            return
        else:
            delete_id

            validate_user_action = input("Are you sure you would like to delete this recipe?" + 
                                         "(enter yes or no): ")

            if validate_user_action.lower() == "yes":
                session.delete(delete_id)
                session.commit()
            elif validate_user_action == "no":
                print("\nReturning to main menu.")
                return
            else:
                print("Wrong word entered. Returning to main menu.")
                return

#Main Menu            
user_input = ""

while not user_input.lower() == "quit":
    print("\nChoose a menu:")
    print("1 - Create a new recipe")
    print("2 - View all recipes")
    print("3 - Search for recipes by ingredients")
    print("4 - Edit a recipe")
    print("5 - Delete a recipe")
    print("quit - Exit the application")

    user_input = input("\nEnter the index of a menu to continue: ")

    if user_input == "1":
        create_recipe()
    elif user_input == "2":
        view_all_recipes()
    elif user_input == "3":
        search_by_ingredients()
    elif user_input == "4":
        edit_recipe()
    elif user_input == "5":
        delete_recipe()
    elif user_input.lower() == "quit":
        print("\nClosing the application")
        session.close()
        engine.raw_connection().close()
    else:
        print("\n"+ "-"*20)
        print("Wrong choice entered. Try again!")
        print("-"*20)