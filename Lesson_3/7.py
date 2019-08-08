"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
from random import randint

lenght = int(input('Введите длину массива: '))
mass = [0] * lenght

for i in range(lenght):
  mass[i] = randint(0, 51) 
print(mass)

if mass[0] > mass[1]:
  min0 = 0
  min1 = 1
else:
  min0 = 1
  min1 = 0

for i in range(2, lenght):
  if mass[i] < mass[min0]:
    x = min0
    min0 = i
    if mass[x] < mass[min1]:
      min1 = x
  elif mass[i] < mass[min1]:
    min1 = i

print(f'1-е минимальное: индекс {min0} число {mass[min0]}')
print(f'2-е минимальное:  индекс {min1} число {mass[min1]}')
