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
            for column in results:
                print("-------------------------------")
                print("\nRecipe name:", column[1])
                print("Cooking time (in minutes):", column [3])
                print("Difficulty:", column[4])
                ingredient_list = column[2].split(", ")
                print("Ingredients:")
                for ingredient in ingredient_list:
                    print(ingredient)
                print("-------------------------------")

    def update_recipe(conn, cursor):
        print("\nUpdating a recipe...\n")

    def delete_recipe(conn, cursor):
        print("\nDeleting a recipe...\n")

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