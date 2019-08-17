"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import defaultdict
from functools import reduce


numbers = defaultdict(list)

for i in range(2):
    ff = input(f'Введите {i+1} -е шестнадцатиричное число: ')
    numbers[f'{i+1}, {ff}'] = list(ff)
    print(numbers)

sum_numbers = sum([int(''.join(i), 16) for i in numbers])
print(f'сумма: ', list(f'{sum_numbers:X}'))
'''%X - Число в шестнадцатеричной системе счисления (буквы в верхнем регистре).'''

mult_numbers = reduce(lambda x, y: x * y, [int(''.join(i), 16) for i in numbers])
print(f'произведение: ', list('%X' % mult_numbers))
