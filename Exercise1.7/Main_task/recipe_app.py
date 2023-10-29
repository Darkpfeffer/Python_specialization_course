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
        return "<Recipe ID: " + self.id + " - " + self.name +", " + self.difficulty + ">"
    
    def __str__(self):
        print("\n" + "-"*20)
        print("Recipe Name: " + self.name + "\tRecipe ID: " + self.id)
        print("Cooking Time: " + self.cooking_time + "\nDifficulty: " + self.difficulty)
        print("Ingredients: ")
        for ingredient in self.ingredients.split(", "):
            print("- " + ingredient)
        print("-"*20 + "\n")

    def calculate_difficulty(self, cooking_time, ingredients):
        short_cooking_time = cooking_time < 10
        long_cooking_time = cooking_time >= 10
        few_ingredients = len(ingredients) < 4
        numerous_ingredients = len(ingredients) >= 4

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