import mysql.connector;

conn = mysql.connector.connect(host = 'localhost',\
                               user = 'cf-python',\
                               password= 'password')

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute(''' CREATE TABLE IF NOT EXISTS Recipes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)              
)''')

def main_menu(conn, cursor):
    choice = ""

    def create_recipe(conn, cursor):
        print("\nCreating a recipe...\n")

        name = input("Name of the Recipe: ")
        cooking_time = input("Cooking Time (in minutes, input integers only): ")
        try:
            int(cooking_time)
        except ValueError:
            print("Your can enter only integers for cooking time.")
            create_recipe(conn, cursor)
        else:
            cooking_time = int(cooking_time)

            ingredients = input(\
                "Ingredients of the recipe (separate them with comma(,) and space ( ): "\
                    ).split(", ")
            
            difficulty = calculate_difficulty(cooking_time, ingredients)

            ingredients_string = ", ".join(ingredients)

            sql_input = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)" +\
            " VALUES ('" + name + "', '" + ingredients_string +"', '" + str(cooking_time) +\
            "', '" + difficulty + "')"

            cursor.execute(sql_input)

            print("\n Recipe " + name + " is successfully created.")
            
            conn.commit()
        
    def search_recipe(conn, cursor):
        print("\nSearching a recipe...\n")

        cursor.execute("SELECT ingredients FROM Recipes;")
        results = cursor.fetchall()

        all_ingredients = []

        for reicpe in results:
            for ingredients in reicpe:
                ingredient_list = ingredients.split(", ")
                for ingredient in ingredient_list:
                    lowercase_ingredient = ingredient.lower() 
                    if not lowercase_ingredient in all_ingredients:
                        all_ingredients.append(lowercase_ingredient)

        for ingredient in all_ingredients:
            print(all_ingredients.index(ingredient), ingredient)

        search_ingredient = input(\
            "Choose the index of the ingredient you are looking for: ")
        try:
            search_ingredient = int(search_ingredient)
        except ValueError:
            print("You can input only numbers here. Try again.")
        else:
            cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE '%" +\
                           all_ingredients[search_ingredient] + "%'")
            results = cursor.fetchall()
            for recipe in results:
                print("-------------------------------")
                print("\nRecipe name:", recipe[1])
                print("Cooking time (in minutes):", recipe[3])
                print("Difficulty:", recipe[4])
                ingredient_list = recipe[2].split(", ")
                print("Ingredients:")
                for ingredient in ingredient_list:
                    print(ingredient)
                print("-------------------------------")

    def update_recipe(conn, cursor):
        print("\nUpdating a recipe...\n")

        cursor.execute("SELECT * FROM Recipes")
        results = cursor.fetchall()
        
        for recipe in results:
            print("---------------------------")
            print('Recipe ID:', recipe[0])
            print('Recipe name:', recipe[1])
            print('Cooking Time (in minutes):', recipe[3])
            print("Difficulty:", recipe[4])
            ingredient_list = recipe[2].split(", ")
            print("Ingredients:")
            for ingredient in ingredient_list:
                print(ingredient)
            print("-------------------------------")

        recipe_to_update = input("\nInput the ID of the recipe to update: ")

        try:
            int(recipe_to_update)
        except ValueError:
            print("Only numbers are allowed. Try again!")
        else:
            print('1. name')
            print('2. cooking_time')
            print('3. ingredients')
            column_to_update = input(\
                "\nWrite the index of the column you would like to update: ")
            
            try:
                column_to_update = int(column_to_update)
            except ValueError:
                ("\nYou can input only numbers here. Try again!")
            else:
                if column_to_update == 1:
                    change_value = input(\
                        "\nWrite the new recipe name: ")
                    cursor.execute("UPDATE Recipes SET name = '" +\
                                   change_value + "' WHERE id = " +\
                                   recipe_to_update)
                    print("\n Recipe name is successfully updated.")

                elif column_to_update == 2:
                    change_value = input(\
                        "\nWrite the new cooking time: ")
                    
                    try:
                        int(change_value)

                    except ValueError:
                        ("\nYou can input only numbers here. Try again!")

                    else:
                        cursor.execute("SELECT * FROM Recipes WHERE id = " +\
                                       recipe_to_update)
                        results = cursor.fetchall()
                        ingredient_list = []
                        for recipe in results:
                            ingredient_list = recipe[2].split(", ")
                        difficulty = \
                            calculate_difficulty(int(change_value), ingredient_list)

                        cursor.execute("UPDATE Recipes SET cooking_time = '" +\
                                   change_value + "', difficulty = '" + difficulty +\
                                    "' WHERE id = " +\
                                   recipe_to_update)
                        
                        print("\nRecipe cooking time is successfully updated.")

                elif column_to_update == 3:
                    change_value = input(\
                        "\nWrite the new ingredients (separate them with comma(,)" +\
                            "and space ( )): ")
                    cursor.execute("SELECT * FROM Recipes WHERE id = " +\
                                       recipe_to_update)
                    cooking_time = ""
                    results = cursor.fetchall()

                    for recipe in results:
                        cooking_time = recipe[3]

                    ingredient_list = change_value.split(", ")
                    
                    difficulty = calculate_difficulty(int(cooking_time), ingredient_list)

                    cursor.execute("UPDATE Recipes SET ingredients = '" +\
                                   change_value + "', difficulty = '" + difficulty +\
                                    "' WHERE id = " +\
                                   recipe_to_update)
                    
                    print("\n Recipe ingredients are successfully updated.")
                else:
                    print("\nInvalid index has been inputted. Try again!")
                    
                conn.commit()
                
    def delete_recipe(conn, cursor):
        print("\nDeleting a recipe...\n")

        cursor.execute("SELECT * FROM Recipes")
        results = cursor.fetchall()
        
        for recipe in results:
            print("---------------------------")
            print('Recipe ID:', recipe[0])
            print('Recipe name:', recipe[1])
            print('Cooking Time (in minutes):', recipe[3])
            print("Difficulty:", recipe[4])
            ingredient_list = recipe[2].split(", ")
            print("Ingredients:")
            for ingredient in ingredient_list:
                print(ingredient)
            print("-------------------------------")

        recipe_to_delete = input("\nInput the ID of the recipe to delete: ")

        try:
            int(recipe_to_delete)
        except ValueError:
            print("Only numbers are allowed. Try again!")
        else:
            cursor.execute("DELETE FROM Recipes WHERE id = '" + recipe_to_delete + "'")

            print("\nRecipe ID "+ recipe_to_delete +" is successfully deleted.")

            conn.commit()

        

    def calculate_difficulty(cooking_time, ingredients):
        short_cooking_time = cooking_time < 10
        long_cooking_time = cooking_time >= 10
        few_ingredients = len(ingredients) < 4
        numerous_ingredients = len(ingredients) >= 4

        if short_cooking_time and few_ingredients:
            return "Easy"
        elif short_cooking_time and numerous_ingredients:
            return "Medium"
        elif long_cooking_time and few_ingredients:
            return "Intermediate"
        elif long_cooking_time and numerous_ingredients:
            return "Hard"
        else:
            print("Difficulty could not been calculated.")


    while(choice != 'quit'):
        print("\nWhat would you like to do? Pick a choice!")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an exisitng recipe")
        print("4. Delete a recipe")
        print("Type 'quit' to exit the program.\n")
        choice = input("Your choice: ")

        if choice == '1':
            create_recipe(conn, cursor)

        elif choice == '2':
            search_recipe(conn, cursor)

        elif choice == '3':
            update_recipe(conn, cursor)

        elif choice == '4':
            delete_recipe(conn, cursor)

        elif choice == 'quit':
            print('Exiting the program...')
            conn.close()

        else:
            print('\nWrong input entered. Returning to main menu...\n')

main_menu(conn, cursor)