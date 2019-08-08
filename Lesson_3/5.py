#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
from random import randint

lenght = int(input('Введите длину массива: '))
mass = [0] * lenght

for i in range(lenght):
  mass[i] = randint(-50, 51) 
print(mass)

index = -1
j = 0

while j < lenght:
  if mass[j] < 0 and index == -1:
    index = j
  elif mass[j] < 0 and mass[j] > mass[index]:
      index = j
  j +=1

print(f'Максимальный отрицательный элемент с индексом {index} -> {mass[index]}')
