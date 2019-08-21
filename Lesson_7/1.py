"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import numpy as np
from memory_profiler import profile
from timeit import timeit

lenght = int(input('Введите длину массива: '))
array = [np.random.randint(-100, 100) for i in range(lenght)]
array1 = array.copy()


# @profile
def bb_sort(array):
    """Стандартный пузырьковый алгоритм"""
    for j in range(lenght - 1):
        for k in range(lenght - j - 1):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
    return array


print(f'Сгенерированный массив: {array}')
new_array = bb_sort(array)
print(f'Отсортированный массив bb_sort: {new_array}')


# @profile
def bb_sort_faster(array1):
    """Новый алгоритм сортировки предполагает не делать прогоны сравнения если изменений не состоялось ранее"""
    change = True  # счетчик изменения массива, по умолчанию True
    run = lenght - 1  # прогоны измерений элементов
    while run > 0 and change:  # прогоняет до тех пор пока есть изменения и прогоны > 0
        change = False  # в начале цикла нет изменений
        for i in range(run):
            if array1[i] > array1[i + 1]:
                change = True  # если условие верно то изменение состоялось и оно True
                array1[i], array1[i + 1] = array1[i + 1], array1[i]  # меняем элементы местами если верхнее условие True
        run = run - 1  # сокращаем количество прогонов
    return array1


print(f'Сгенерированный массив: {array1}')
new_array1 = bb_sort_faster(array1)
print(f'Отсортированный массив bb_sort1: {new_array1}')

print(timeit('bb_sort(array)', setup='from __main__ import bb_sort, array', number=10000))
print(timeit('bb_sort_faster(array1)', setup='from __main__ import bb_sort_faster, array1', number=10000))

'''При 100 элементах в массиве и 10000 прогонах этих двух функций получаем время выполнения:
    bb_sort - 3.08с
    bb_sort_faster - 0.06с 
    Новый вариант в 51 раз быстрее стандартного пузырькового алгоритма
    При использовании профилировщика память тратится одинаково ~ 31 Мб'''
