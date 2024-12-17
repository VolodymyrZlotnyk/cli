import math
try:
    zavd = int(input("Введіть номер завдання (1-3): ")) 

    if zavd < 1 or zavd > 3:
        print("Ви ввели некоректний номер завдання!")
    else:

        if zavd == 1:
            x_value = float(input("Введіть значення x: "))

            if x_value > 45:
                result = -x_value ** 0.5
            else:
                result = math.sin(2 * x_value)

            print("Значення y_z при x =", x_value, "дорівнює", result)

        elif zavd == 2:
            r = input("Введіть число r: ")
            if r.isdigit():
                r = int(r)
                if r >= 0:
                    fib_prev, fib_curr = 1, 1
                    while fib_curr <= r:
                        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
                    print(f"Перше число Фібоначчі, більше {r}, це {fib_curr}")
                else:
                    print("Будь ласка, введіть додатнє число.")
            else:
                print("Будь ласка, введіть коректне ціле число.")

        elif zavd == 3:
            array = [int(x) for x in input("Введіть елементи масиву через пробіл: ").split()]

            max_element = max(array)
            print("Максимальний елемент:", max_element)
            arithmetic_mean = sum(array) / len(array)
            print("Середнє арифметичне елементів:", arithmetic_mean)

            reversed_array = array[::-1]
            print("Масив у зворотному порядку:", reversed_array)

except ValueError:
    print("Вводьте числа!")