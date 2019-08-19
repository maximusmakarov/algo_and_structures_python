"""
2. Создать пользовательский класс данных (или использовать) один из классов, реализованных в курсе Python.Основы. 
Реализовать класс с применением слотов и обычным способом. Для объекта обычного класса проверить отображение словаря атрибутов.
Сравнить, сколько выделяется памяти для хранения атрибутов обоих классов.
"""
import sys
from pympler import asizeof

class Rounding(object):
    """Класс для параметров количества и определенного коэффициента (взято с рабочего проекта)"""
    def __init__(self, name, count, measure_ratio):
        self.name = name
        self.count = count
        self.measure_ratio = measure_ratio


class RoundingNew(object):
    __slots__ = ['name', 'count', 'measure_ratio']
    def __init__(self, name, count, measure_ratio):
        self.name = name
        self.count = count
        self.measure_ratio = measure_ratio

# Cтруктуру 2-х классов вкладываем в список
r1 = Rounding('округление', 4, 5)
r2 = RoundingNew('округление', 3, 4)


""" На github нашлась функция, подсчитывающая как бы реальный объем данных, рекурсивно вызывая getsizeof для всех объектов. 
Она отличается реализацией по сравнению с pympler.asizeof хотя описания у них во многом схожи"""

def get_size(obj, seen=None):
    # From https://goshippo.com/blog/measure-real-size-any-python-object/
    # Recursively finds size of objects
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0

    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
      size += sum([get_size(v, seen) for v in obj.values()])
      size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
      size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
      size += sum([get_size(i, seen) for i in obj])
    return size

print(f"get_size(r1): {get_size(r1)} б")
print(f"get_size(r2): {get_size(r2)} б")
print(f"getsizeof(r1): {sys.getsizeof(r1)} б")
print(f"getsizeof(r2): {sys.getsizeof(r2)} б")
print(f"asizeof(r1): {asizeof.asizeof(r1)} б")
print(f"asizeof(r2): {asizeof.asizeof(r2)} б")

# get_size(r1): 503 б
# get_size(r2): 72 б
# getsizeof(r1): 64 б
# getsizeof(r2): 72 б
# asizeof(r1): 520 б
# asizeof(r2): 232 б

"""С использованием getsizeof(функция sys.getsizeof возвращает размер переданного ей обьекта, этот размер не включает в себя сложные 
структуры классов) потребление памяти данными одинаково считается только при использовании __slots__ и то, как полагаю, не верно. 
get_size рекурсивно считает все объекты которые питон с собой подтягивает. Со слотами get_size пишет такое же значение в 72 байта.
 asizeof(рекурсивно ищет всё вложенние поля и элементы, и отображает общий размер обьекта, на сайте разработчика пишется что примерно)
 в свою очередь показывает наибольшие значения потребляемой памяти, пытается собрать полный размер объекта, видимо получается, но как 
 утверждают некоторые источники - не всегда ей удается
 https://ru.stackoverflow.com/questions/883933/%D0%9F%D0%B0%D0%BC%D1%8F%D1%82%D1%8C-%D0%B2-python-%D0%92-%D1%87%D0%B5%D0%BC-%D0%BE%D1%82%D0%BB%D0%B8%D1%87%D0%B8%D0%B5-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B9-pympler-asizeof-%D0%B8-sys-getsizeof-%D0%B2%D0%BE%D0%B7%D0%B2%D1%80%D0%B0%D1%89%D0%B0
 """
