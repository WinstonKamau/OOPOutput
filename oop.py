class Pets(object):
    # The variables for pets are encapsulated
    def __init__(self, price=0, quantity=0):
        self.__price = price
        self.__quantity = quantity
        

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price
    
    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def get_pet_value(self):
        value = self.__price * self.__quantity
        return value

    def pet_type(self, name=None):
        if name is not None:
            print ("Pet Type is:", name )
        else:
            print ("Pet type not given")

# The class Dogs inherits from Pets
class Dogs(Pets):
    # The variables for dogs are encapsulated
    def __init__(self, name=None, breed=None, gender=None, colors=None, age=None):
        self.__name = name
        self.__breed = breed
        self.__gender = gender
        self.__colors = colors
        self.__age = age

    # Abstraction. The variables are private but can be updated if the object uses the methods below
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_breed(self, breed):
        self.__breed = breed

    def get_breed(self):
        return self.__breed

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_colors(self, colors):
        self.__colors = colors

    def get_colors(self):
        return self.__colors

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

# The class bird inherits from Pets
class Birds(Pets):
    # The variables for birds are encapsulated
    def __init__(self, name=None, breed=None, gender=None, colors=None, age=None):
        self.__name = name
        self.__breed = breed
        self.__gender = gender
        self.__colors = colors
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_breed(self, breed):
        self.__breed = breed

    def get_breed(self):
        return self.__breed

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_colors(self, colors):
        self.__colors = colors

    def get_colors(self):
        return self.__colors

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

# Inheritance of methods and variables

dog_inheritance = Dogs("", "german shepherd", "female", "black", 4 )
bird_inheritance = Birds("", "buzzard", "female", "black", 2)

dog_inheritance.set_price(25000)
dog_inheritance.set_quantity(20)
bird_inheritance.set_price(2500)
bird_inheritance.set_quantity(10)

print("Dog value: ", dog_inheritance.get_pet_value())
print("Bird value:", bird_inheritance.get_pet_value())



# Polymorphism with functions
dog_1 = Dogs("Bucky", "rottweiler", "male", "black", 4 )
bird_1 = Birds("Float", "falcon", "male", "black and white", 2)

def pet_names(pet_type):
    name = pet_type.get_name()
    print("Name:", name)
    
def pet_ages(pet_type):
    age = pet_type.get_age()
    print("Age:", age)

def pet_colors(pet_type):
    colors = pet_type.get_colors()
    print("Color:", colors)

pet_names(dog_1)
pet_names(bird_1)
pet_ages(dog_1)
pet_ages(bird_1)
pet_colors(dog_1)
pet_colors(bird_1)


# Polymorphism with Classes

pets = [ Dogs("Buch", "dobermann", "female", "black and brown", 2 ), Birds("Parry", "parrot", "male", "blue-yellow", 1) ]

for pet in pets:
    print ( "Name:{0} Breed:{1} Gender:{2} Color:{3} Age:{4}".format(pet.get_name(), pet.get_breed(), pet.get_gender(), pet.get_colors(), pet.get_age()) )


# Method overloading

pet = Pets()
pet.pet_type()
pet.pet_type("domesticated")