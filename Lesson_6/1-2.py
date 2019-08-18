from functools import lru_cache
from pympler import asizeof
from memory_profiler import profile

"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов 100
"""

k = 1
number = 100

# Через массив
'''Через массив аналогичная ситуация как и в примере с циклом. Выделяется 13.8 Мб на выполнение памяти и 
asizeof (summa1) функции 24 байта'''


@lru_cache(maxsize=None)
@profile
def summa1(k):
    a = [0] * number
    for i in range(number):
        a.append(k)
        k /= -2
    return sum(a)


print(asizeof.asizeof(summa1(k)))

if __name__ == '__main__':
    summa1(k)
