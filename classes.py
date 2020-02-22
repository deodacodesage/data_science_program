class Human (object):
    """
    Class that defines human beings
    """
    def __init__ (self, name, age, race, gender, religion):
        self.name = name
        self.age = age
        self.race = race
        self.gender = gender
        self.religion = religion

    def __person(self):
        profile = """
        The name of the guy is {}, \n
        {} is {} years old. \n
        {} is an {} and practices {} .\n
        {} is an {} {} so we have to deport the motherF***ker
        """.format(self.name, self.name, self.age, self.name, self.race, self.religion, self.name, self.race, self.gender)

        print(profile)

    def grow(self, value):
        new_age = int(self.age) + int(value)
        self.age = new_age
        print("Sola is now", self.age ,"after serving his time") 

sola = Human("Sola", "28", "African", "Man","Christianity")
sola.__person()
"""
class Swimmer(Human):
    def swim(self):
        print(self.name, "is a swimmer now")           

sola = Human("Sola", "28", "African", "Man","Christianity")
sola.person()
sola.grow(15)

career = Swimmer ("Sola", "28", "African", "Man", "Christianity")
career.swim()
"""
