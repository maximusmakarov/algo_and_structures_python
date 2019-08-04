"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

# Ряд чисел состоит из элементов, где каждый последующий меньше по модулю в 2 раза
number = int(input('Введите количество элементов ряда: '))

k = 1  # Первый элемент последовательности
summ = 0  # Начальная сумма элементов ряда

for n in range(number):
    summ += k
    k /= 2
print(f'Сумма {number} элементов ряда: {summ}')
