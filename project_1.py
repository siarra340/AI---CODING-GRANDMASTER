class Robot:

    function = "assit humans and make tasks easier"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

    def hobby(self, hobby):
        return "{} likes to {} as a hobby".format(self.name, hobby)

robot = Robot("Julie", 10)

robot.intro()

print(f"{robot.name}'s function is to {robot.function}")

print(robot.hobby("read"))