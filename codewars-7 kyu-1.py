"""Создать функцию, которая берет список неотрицательных целых чисел и строк
и возвращает новый список с отфильтрованными строками. (остаются только числа)  """

def filter_list(l):
    res=[i for i in l if type(i)==int]
    return res
