from functools import lru_cache
from pympler import asizeof
from memory_profiler import profile

"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов 100
"""

k = 1
number = 100

# Через список
'''Через список аналогичная ситуация как и в примере с циклом. Также выделяется 13.9 Мб на выполнение памяти и 
asizeof (summa1) функции 24 байта'''


@lru_cache(maxsize=None)
@profile
def summa1(k):
    a = list() * number
    for i in range(number):
        a.append(k)
        k /= -2
    return sum(a)


print(asizeof.asizeof(summa1(k)))

if __name__ == '__main__':
    summa1(k)
