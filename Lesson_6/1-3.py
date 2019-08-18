from functools import lru_cache

from memory_profiler import profile
from pympler import asizeof

# С рекурсией
'''Через рекурсию получается самый медленный и неэффективный по расходованию памяти алгоритм. 
Выделяется Mem usage = 14,7 Мб, Increment = 13.7 Мб на выполнение памяти и asizeof (summa1) функции 24 байта
Increment = 0.4 MiB     в строке  if k == number: до момента когда это условие выполняется и Increment = 0 MiB
когда глубина рекурсии достигает максимального значения и Mem usage = Increment = 14,7 Мб
Самое занятное что при использовании кэша Increment в строке if k == number: за все итерации равен 0.1 MiB, а 
суммарное его значение снижается до 13.7 Мб
После удаления k после if k == number: память суммарно уменьшилась на 0.2 MiB и прибавилось в строке return 
summ_rec(k + 1, l / -2, number, summ + l) на 0.1 MiB , Mem usage = 14,5 Мб'''

k = 1
summ = 0
number = 100
l = 1


# @lru_cache(maxsize=None)
@profile
def summ_rec(k, l, number, summ):
    if k == number:
        del k
        return summ
    elif k < number:
        return summ_rec(k + 1, l / -2, number, summ + l)


print(asizeof.asizeof(summ_rec(k, l, number, summ)))


if __name__ == '__main__':
    summ_rec(k, l, number, summ)
