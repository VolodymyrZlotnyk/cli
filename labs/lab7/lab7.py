import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import string
import re

try:
    zavd = int(input("Введіть номер завдання (1-3): ")) 

    if zavd < 1 or zavd > 3:
        print("Ви ввели некоректний номер завдання!")
    else:

        if zavd == 1:
            def plot_function(func_str, x_range, filename):
                x = np.linspace(*x_range, 1000)
                y = eval(func_str)
                plt.figure(figsize=(8, 6))
                plt.plot(x, y)
                plt.xlabel('x')
                plt.ylabel('y')
                plt.title(f'Графік функції: {func_str}')
                plt.grid(True)
                plt.savefig("labs/lab7/" + filename)
                plt.show()

            functions = [
                ('x*np.sin(5*x)', (-2, 5)),
                ('1/x*np.sin(5*x)', (-5, 5)),
            ]

            for i, (func_str, x_range) in enumerate(functions):
                filename = f'plot_{i+1}.png'
                plot_function(func_str, x_range, filename)

        elif zavd == 2:
            text = "Це приклад тексту для аналізу. Мета - зобразити гістограму частоти появи літер у цьому тексті."
            text = text.translate(str.maketrans('', '', string.punctuation)).lower()
            letter_counts = Counter(text)

            if ' ' in letter_counts:
                del letter_counts[' ']

            plt.bar(letter_counts.keys(), letter_counts.values())
            plt.xlabel('Літери')
            plt.ylabel('Частота')
            plt.title('Гістограма частоти появи літер')
            plt.savefig('labs/lab7/letter_frequency_histogram.png')
            plt.show()

        elif zavd == 3:
            text = """
            Це звичайне речення. А це питання? Ось це окличне речення! Речення з трикрапкою...
            Ще одне звичайне речення. Інше питання? І знову окличне речення! І знову речення з трикрапкою...
            """

            ordinary_sentences = len(re.findall(r'\.\s', text))
            question_sentences = len(re.findall(r'\?\s', text))
            exclamation_sentences = len(re.findall(r'!\s', text))
            ellipsis_sentences = len(re.findall(r'\.\.\.\s', text))

            types_of_sentences = ['Звичайні', 'Питальні', 'Окличні', 'Трикрапка']
            frequency = [ordinary_sentences, question_sentences, exclamation_sentences, ellipsis_sentences]

            plt.bar(types_of_sentences, frequency)
            plt.xlabel('Типи речень')
            plt.ylabel('Частота')
            plt.title('Гістограма частоти речень')
            plt.savefig('labs/lab7/sentence_type_histogram.png')
            plt.show()

except ValueError:
    print("Вводьте числа!")
