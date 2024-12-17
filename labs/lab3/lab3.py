import os
import random

def create_student_files(groups, num_students):
    for group in groups:
        with open(f"labs/lab3/{group}.txt", "w", encoding="utf-8") as file:
            for i in range(num_students):
                name = f"Студент_{i + 1}"
                grade = round(random.uniform(0, 100), 2)
                file.write(f"{name}: {grade}\n")

def read_student_file(filename):
    with open(f"labs/lab3/{filename}", "r", encoding="utf-8") as file:
        for line in file:
            name, grade = line.strip().split(": ")
            print(f"Ім'я: {name}, Середній бал: {grade}")

def append_to_file(filename, name, grade):
    with open(f"labs/lab3/{filename}", "a", encoding="utf-8") as file:
        file.write(f"{name}: {grade}\n")

def search_files(directory, pattern):
    for file in os.listdir(directory):
        if pattern in file:
            print(file)

def search_data_in_file(filename, search_term):
    with open(f"labs/lab3/{filename}", "r", encoding="utf-8") as file:
        for line in file:
            if search_term in line:
                print(line.strip())

def sort_file(filename, reverse=False):
    with open(f"labs/lab3/{filename}", "r", encoding="utf-8") as file:
        lines = file.readlines()
    lines.sort(key=lambda x: float(x.split(": ")[1]), reverse=reverse)
    with open(f"labs/lab3/{filename}", "w", encoding="utf-8") as file:
        file.writelines(lines)

groups = ["Група_А", "Група_Б", "Група_В"]
create_student_files(groups, 10)
print("Вміст файлу 'Група_А.txt':")
read_student_file("Група_А.txt")
print("\nДодаємо нового студента:")
append_to_file("Група_А.txt", "Новий студент", 95)
read_student_file("Група_А.txt")
print("\nПошук файлів, що містять 'Група':")
search_files(".", "Група")
print("\nПошук тексту 'Новий' у файлі 'Група_А.txt':")
search_data_in_file("Група_А.txt", "Новий")
print("\nСортуємо файл 'Група_А.txt' у зворотному порядку:")
sort_file("Група_А.txt", reverse=True)
read_student_file("Група_А.txt")