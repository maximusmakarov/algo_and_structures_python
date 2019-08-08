# 4.	Определить, какое число в массиве встречается чаще всего.
from random import randint

lenght = int(input('Введите длину массива: '))
mass = [0] * lenght

for i in range(lenght):
  mass[i] = randint(0, 31) # диапазон генерации можно ещё уменьшить для получения более частого выпадания повторяющегося числа
print(mass)

max_frequency = 1
number = mass[0]

for i in range(lenght-1):
  frequency = 1
  for j in range(i+1, lenght):
    if mass[i] == mass[j]:
      frequency +=1
  if frequency > max_frequency:
    max_frequency = frequency
    number = mass[i]

if max_frequency > 1:
  print(f'Чаще всего встречается  число {number} - {max_frequency} раза ')
