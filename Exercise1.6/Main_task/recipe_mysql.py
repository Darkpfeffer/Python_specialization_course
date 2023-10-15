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

    def search_recipe(conn, cursor):
        print("\nSearching a recipe...\n")

    def update_recipe(conn, cursor):
        print("\nUpdating a recipe...\n")

    def delete_recipe(conn, cursor):
        print("\nDeleting a recipe...\n")

    while(choice != 'quit'):
        print("\nWhat would you like to do? Pick a choice!")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an exisitng recipe")
        print("4. Delete a recipe")
        print("Type 'quit' to exit the program.\n")
        choice = input("Your choice: ")

        if choice == '1':
            create_recipe('conn', 'cursor')

        elif choice == '2':
            search_recipe('conn', 'cursor')

        elif choice == '3':
            update_recipe('conn', 'cursor')

        elif choice == '4':
            delete_recipe('conn', 'cursor')

        elif choice == 'quit':
            print('Exiting the program...')

        else:
            print('\nWrong input entered. Returning to main menu...\n')

main_menu(conn, cursor)