try:
    n = int(input("Введіть кількість чисел: "))
    total = 0

    for i in range(n):
        num = float(input(f"Введіть число #{i + 1}: "))
        total += num

    average = total / n
    print(f"Середнє арифметичне: {average:.2f}")

except ValueError:
    print("Будь ласка, введіть коректні числа.")

