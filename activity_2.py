class student:
    grade = 10
    name = "Penguin"

    def intro(self):
        print("Hi I am a student")

    def details(self):
        print("My name is", self.name)
        print("My grade is", self.grade)

ob = student()
ob.intro
ob.details