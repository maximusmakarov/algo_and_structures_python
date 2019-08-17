"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections

factory = {}
q_profit = 0
# a = 1
n = int(input("Количество заводов: "))
for i in range(n):
    f_name = input(f'Имя {str(i + 1)}-го завода: ')
    quart = input(f'прибыль за 4 квартала через пробел: ')
    q_profit = quart.split(' ')
    factory[f_name] = q_profit
    print()

fac = collections.Counter(factory)
summ_all = 0
for i in fac:
    summ = 0
    for j in fac[i]:
        summ += int(j)
    fac[i] = summ
    summ_all += summ
av_profit = summ_all / n

print(f'\nСредняя прибыль за год всех предприятий: {av_profit}')
for k in factory:
    if fac[k] > av_profit:
        print(f'Предприятие с прибылью выше среднего: {k}')
    else:
        print(f'Предприятие с прибылью ниже среднего: {k}')
