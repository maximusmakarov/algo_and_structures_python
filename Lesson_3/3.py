#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
from random import randint

lenght = int(input('Ведите длину массива: '))
mass = [0] * lenght

for i in range(lenght):
  mass[i] = randint(0, 101)
  print(f'{mass[i]}', end = '|')
print ('\n')

min = 0
max = 0
for i in range(lenght):
  if mass[i] < mass[min]:
    min = i
  elif mass[i] >mass[max]:
    max = i
print(f'mass[{min}]={mass[min]} mass[{max}]={mass[max]}')
print ('\n')

replace = mass[min]
mass[min] = mass[max]
mass[max] = replace

for i in range(lenght):
  print(f'{mass[i]}', end = '|')
