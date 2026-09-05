student_profile = ("Aarav", "Grade 6", "Section A", 6)

print(f"Student Profile: {student_profile}")

student_name = student_profile[0]
grade = student_profile[1]
section = student_profile[2]
total_subjects = student_profile[3]

print("\nStudent Name:", student_name)
print(f"Grade: {grade}")
print(f"Section: {section}")
print("Total Subjects:", total_subjects)

print("First two details: ", student_profile[0:2])

#SETS

monday_subjects = {"Math", "Science", "English", "Computer", "Art"}
tuesday_subjects = {"Math", "History", "English", "Sports", "Music"}

print("\nMonday Subjects:", monday_subjects)
print("Tuesday Subjects:", tuesday_subjects)

monday_subjects.add("Library")
print("\nAfter adding Library to Monday:", monday_subjects)

monday_subjects.discard("Art")
print("After removing Art from Monday:", monday_subjects)

tuesday_subjects.add("Computer")
print("After adding Computer to Tuesday:", tuesday_subjects)

tuesday_subjects.discard("Music")
print("After remvoing Music from Tuesday:", tuesday_subjects)

all_subjects = monday_subjects.union(tuesday_subjects)
common_subjects = monday_subjects.intersection(tuesday_subjects)
only_monday = monday_subjects.difference(tuesday_subjects)
only_tuesday = tuesday_subjects.difference(monday_subjects)
different_subjects = monday_subjects.symmetric_difference(tuesday_subjects)

print("\nAll Subjects:", all_subjects)
print("Common Subjects:", common_subjects)
print("Only Monday Subjects:", only_monday)
print("Only Tuesday Subjects:", tuesday_subjects)
print("Different Subjects:", different_subjects)

print("\n================================")
print("SCHOOL SUBJECT PLANNER SUMMARY")
print("================================")
print("Student:", student_name)
print("Grade", grade)
print(f"Monday Subjects: {monday_subjects}")
print(f"Tuesday Subjects: {tuesday_subjects}")
print("Subjects on Both Days:", common_subjects)
print(f"All Unique Subjects:", all_subjects)
print("==============================")