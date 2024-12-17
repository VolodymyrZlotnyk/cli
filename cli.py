import os
import sys

def list_labs():
    labs_dir = "labs"
    if not os.path.exists(labs_dir):
        print("Каталог з лабораторними роботами не знайдено.")
        return

    labs = sorted([d for d in os.listdir(labs_dir) if os.path.isdir(os.path.join(labs_dir, d))])

    if not labs:
        print("Лабораторні роботи відсутні.")
        return

    print("Доступні лабораторні роботи:")
    for lab in labs:
        i = lab[3:]
        description = f"Лабораторна робота №{i}"
        print(f"{i} - {lab}: {description}")

def run_lab(lab_number):

    labs_dir = "labs"
    lab_folder = f"lab{lab_number}"
    lab_path = os.path.join(labs_dir, lab_folder, f"{lab_folder}.py")

    if not os.path.exists(lab_path):
        print(f"Лабораторну роботу {lab_number} не знайдено.")
        return

    print(f"Запуск лабораторної роботи {lab_number}...")
    os.system(f"python {lab_path}")


if len(sys.argv) < 2:
    print("Використання:")
    print("  python cli.py list")
    print("  python cli.py run <номер_лабораторної>")
else:
    command = sys.argv[1]

    if command == "list":
        list_labs()
    elif command == "run":
        if len(sys.argv) < 3:
            print("Будь ласка, вкажіть номер лабораторної роботи для запуску.")
        else:
            try:
                lab_number = int(sys.argv[2])
                run_lab(lab_number)
            except ValueError:
                print("Некоректний номер лабораторної. Введіть правильне ціле число.")
    else:
        print(f"Невідома команда: {command}")
        print("Використання:")
        print("  python cli.py list")
        print("  python cli.py run <номер_лабораторної>")

