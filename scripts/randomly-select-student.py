""" Print a randomly-selected student from our CSV of all students
"""
import csv
import random

STUDENT_FILE = 'students.csv'

with open(STUDENT_FILE, 'r') as f:
    csv_data = csv.reader(f)
    students = [el[0] for el in list(csv_data)]

print(random.choice(students))
