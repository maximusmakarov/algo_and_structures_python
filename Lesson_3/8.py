"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
M = 5
N = 4
a = []
for i in range(N):
  b = []
  summ = 0
  print(f'{i+1}-я строка: ')
  for j in range(M-1):
    num = int(input())
    summ += num
    b.append(num)
  b.append(summ)
  a.append(b)

for i in a:
  print(i)
