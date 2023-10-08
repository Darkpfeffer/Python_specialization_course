class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def __str__(self):
        output = "\nClass: Animal\nName: " + str(self.name) + \
        "\nAge: " + str(self.age)
        return output
    
class Cat(Animal):
    def speak(self):
        print("Meow")

    def __str__(self):
        output = "\nClass: Cat\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output
    
class Dog(Animal):
    def speak(self):
        print("Woof")

    def __str__(self):
        output = "\nClass: Dog\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output
    
class Human(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def add_friend(self, friend_name):
        self.friends.append(friend_name)

    def show_friends(self):
        for friend in self.friends:
            print(friend)

    def speak(self):
        print("Hello, my name's " + self.name + "!")
    
    def __str__(self):
        output = "\nClass: Human\nName: " + str(self.name) + \
            "\nAge: " + str(self.age) + "\nFriends list: \n"
        for friend in self.friends:
            output += friend + "\n"
        return output

class Car(object):
    id = 0
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.id = Car.id
        Car.id += 1

    def __str__(self):
        output = "\nID: " + str(self.id) + \
            "\nName: " + self.name + \
            "\nModel: " + self.model + \
            "\nYear: " + self.year
        return output
    
c0 = Car("Ford", "Shelby GT500", "2015")
c1 = Car("Toyota", "Corolla", "2012")
c2 = Car("BMW", "Z3", "2001")
c3 = Car("Audi", "A6", "2020")

print(c0)
print(c1)
print(c2)
print(c3)