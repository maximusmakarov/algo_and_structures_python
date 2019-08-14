"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

factory = {}
summ = 0
q_profit = 0
n = int(input("Количество заводов: "))
s = 0
for i in range(n):
    f_name = input(f'Имя {str(i + 1)}-го завода: ')
    for j in range(4):
        q_profit = float(input(f'прибыль за {j+1}-й квартал: '))
    factory[f_name] = q_profit
    summ += q_profit

av_profit = summ / n
print(f'\nСредняя прибыль за год всех предприятий: {av_profit}')
for k in factory:
    if factory[k] > av_profit:
        print(f'Предприятие с прибылью выше среднего: {k}')
    else:
        print(f'Предприятие с прибылью ниже среднего: {k}')

