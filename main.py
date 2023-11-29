numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

# You can also work with strings
name = "Mohana"
name_list = [n for n in name]
print(name_list)

# You can also work with ranges
range_list = [n*2 for n in range(1, 5)]
print(range_list)

# You can also add an if condition in lists comprehensions
names = ["Mohana", "Madhu", "Satya", "Kiran", "Sayonee", "Shreya"]
short_names = [name for name in names if len(name) < 6]
print(short_names)
capital_names = [name.upper() for name in names if len(name) > 5]
print(capital_names)

# Dictionary Comprehensions from lists
import random
new_list_names = ["Mohana", "Madhu", "Satya", "Kiran", "Sayonee", "Shreya"]
student_scores = {student: random.randint(80, 100) for student in names}
print(student_scores)

# Dictionary Comprehensions from existing dictionaries
passed_students = {student: score for (student, score) in student_scores.items() if score > 93}
print(passed_students)

# Looping through data frames
import pandas
student_dict = {
    "student": ["Mohana", "Kiran", "Sayonee"],
    "scores": [56, 89, 70]
}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through columns of the Data Frame
for (key, value) in student_data_frame.items():
    print(value)

# Loop through rows of the Data Frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)

