"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

lenght = int(input('Введите длину массива: '))
mass = [0] * lenght

for i in range(lenght):
  mass[i] = randint(0, 51) 
print(mass)

summ = 0
min = 0
max = 0

for i in range(1, lenght):
  if mass[i] < mass[min]:
    min = i
  elif mass[i] > mass[max]:
    max = i
print(f'минимум {mass[min]}, максимум {mass[max]}')

if min > max:
  min, max = max, min

for j in range(min+1, max):
  summ += mass[j]

print(f'Сумма между минимальным {min} и максимальным {max} значением элемента массива будет: {summ}')
