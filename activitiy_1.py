classmates = ["Aarav", "Priya", "Rahul", "Sneha", "Dev"]
print("Class List:", classmates)

print("Total Students:", len(classmates))
print(f"First Student: {classmates[0]}")
print(f"Last Student: {classmates[-1]}")
print("First Three:", classmates[:3] )

classmates.append("Meera")
print("\nAfter adding Meera:", classmates)
classmates.remove("Dev")
print("After removing Dev", classmates)
classmates.sort()
print("Sorted alphabetically:", classmates)
classmates.reverse()
print("Reversed:", classmates)

teacher = {"name": "Mr. Sharma", "subject": "Python", "experience": 5}

print("Subject:", teacher["subject"])
print("Experience:", teacher.get("experience", "Not found"))
teacher["experience"]= 6
teacher["email"]= "sharma@school.com"
teacher.pop("subject")
print("Updated teacher profile:", teacher)

roll_numbers = [1, 2, 3, 4, 5]
names = ["Aarav", "Priya", "Rahul", "Sneha", "Meera"]
student_directory = dict(zip(roll_numbers, names))
print("\nStudent Directory:", student_directory)
print("Student at Roll 3:", student_directory[3])