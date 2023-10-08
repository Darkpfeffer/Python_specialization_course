class Recipe():
    all_ingredients = []
    def __init__(self, name, cooking_time):
        self._name = str(name)
        self._cooking_time = int(cooking_time)
        self.ingredients = []
        self._difficulty = ""
        self.calculate_difficulty()

    @property
    def name(self):
        return self._name

    @property
    def cooking_time(self):
        return self._cooking_time
    
    def get_ingredients(self):
        output = ", ".join(self.ingredients)
        return output

    @property
    def difficulty(self):
        if len(self._difficulty) < 1:
            self.calculate_difficulty()
        return self._difficulty

        

    def add_ingredients(self, ingredient_list):
        for ingredient in ingredient_list:
            if not ingredient.lower() in self.ingredients:
                self.ingredients.append(ingredient.lower())

        self.calculate_difficulty()
            
        self.update_all_ingredients()
    
    def calculate_difficulty(self):
        short_cooking_time = self._cooking_time < 10
        long_cooking_time = self._cooking_time >= 10
        few_ingredients = len(self.ingredients) < 4
        numerous_ingredients = len(self.ingredients) >= 4

        if short_cooking_time and few_ingredients:
            self._difficulty = "Easy"
        elif short_cooking_time and numerous_ingredients:
            self._difficulty = "Medium"
        elif long_cooking_time and few_ingredients:
            self._difficulty = "Intermediate"
        elif long_cooking_time and numerous_ingredients:
            self._difficulty = "Hard"

    def search_ingredient(self, ingredient):
        if ingredient.lower() in self.ingredients:
            return True
        else:
            return False

    @cooking_time.setter
    def cooking_time(self, new_cooking_time):
        self._cooking_time = int(new_cooking_time)
        self.calculate_difficulty()

    @name.setter
    def name(self, name):
        self._name = str(name)

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if not ingredient in self.all_ingredients:
                self.all_ingredients.append(ingredient)

    def recipe_search(data, search_term):
        printed_recipes= []
        for recipe in data:
            for search_item in search_term:
                if recipe.search_ingredient(search_item.lower()) == True:
                    print(recipe)
                    printed_recipes.append(recipe.name)
                    break          

        if len(printed_recipes) < 1:
            print("No recipes found.")

    def __str__(self):
        output = "\nRecipe: "+ self.name + \
                    "\nCooking Time (in minutes): " + str(self.cooking_time) + \
                    "\nDifficulty: " + self.difficulty + \
                    "\nIngredients: \n" + self.get_ingredients()
        return output

recipe1 = Recipe('Tea', 5)
recipe1.add_ingredients(("Tea Leaves", "Sugar", "Water"))
print(recipe1)

recipe2 = Recipe('Coffee', 5)
recipe2.add_ingredients(("Coffee Powder", "Sugar", "Water"))
print(recipe2)

recipe3 = Recipe('Cake', 50)
recipe3.add_ingredients(("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour",\
                          "Baking Powder", "Milk"))
print(recipe3)

recipe4 = Recipe('Banana Smoothie', 5)
recipe4.add_ingredients(("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"))
print(recipe4)

recipes_list = [recipe1, recipe2, recipe3, recipe4]
search_criteria = ["Water", "Sugar", "Bananas"]

print("--------------------------------")
print("Searching for recipes: ")

Recipe.recipe_search(recipes_list, search_criteria)