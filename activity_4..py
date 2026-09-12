class Parrot:

    food = "pizza"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def food(self):
        return "{} loves to eat {}".format(self.name, self.food)

    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

blu = Parrot("Blu", 10)

print(blu.sing("'Happy'"))
print(blu.dance())
