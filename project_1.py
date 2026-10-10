import os

science_notes = [
    "Plants need sunlight and water\n",
    "The Earth moves around the sun\n",
    "Water can change into ice and steam\n"
]

maths_notes =[
    "Addition means finding the total\n",
    "Subtraction means taking away\n",
    "Multiplication is repeated addition\n"
]

with open('science-notes.txt', 'w') as f:
    f.writelines(science_notes)

with open('maths-notes.txt', 'w') as f:
    f.writelines(maths_notes)

with open('science-notes.txt', 'r') as f:
    for line in f:
        print(line.strip())

with open('maths-notes.txt', 'r') as f:
    for line in f:
        word = line.split()
        print(len(word), 'words->', line.strip())

merged_file = "all-study-notes.txt"

if os.path.exists('merged_file'):
    print(merged_file, 'already exists.')
else:
    print(merged_file, "does not exist yet.")

if os.path.exists('merged-file'):
    os.remove('merged-file')
    print("Old merged file removed.")
else:
    print("No old merged file to remove.")

with open(merged_file, 'w') as output:
    output.write("=== SCIENCE NOTES ===\n")

    with open('science-notes.txt', 'r') as science:
        output.write(science.read())

    output.write("=== MATH NOTES ===\n")

    with open('maths-notes.txt', 'r') as math:
        output.write(math.read())

print("Science and Maths notes merged successfully.")

print("Merged Study Notes:")

with open(merged_file, 'r') as f:
    for line in f:
        print(line.strip())







