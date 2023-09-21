class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        return "{} is now sitting".format(self.name)

    def roll_over(self):
        return "{} rolled over!".format(self.name)
