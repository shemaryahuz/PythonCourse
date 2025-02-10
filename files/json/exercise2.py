import json

grades = {"English": 90, "Mathmatics": 95, "Python": 100}

with open("grades.json","w") as file:
    json.dump(grades, file)

with open("grades.json") as file:
    data = json.load(file)

is_sum = 0
counter = 0

for subject in data:
    counter += 1
    is_sum += data[subject]

print(f"The average of the grades is {is_sum/counter}")