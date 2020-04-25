# 1)Дан массив из словарей 
data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

# 1.1) отсортировать массив из словарей по значению ключа ‘age' 

print(sorted(data, key=lambda i: i['age']))  # sorted() with lambda

# 1.2) сгруппировать данные по значению ключа 'city' 

from collections import defaultdict


def key_gouping(some_data):
    """
    group data by key value 'city'
    using defaultdict
    :param some_data: list of dicts
    :return: dict
    """
    res = defaultdict(list)
    for i in some_data:
        res[i['city']].append(i)
    return dict(res)


print(key_gouping(data))


def key_grouping_2(my_data):
    """
    group data by key value 'city'
    :param my_data: list of dicts
    :return: dict
    """
    result = {}
    for d in my_data:
        result.setdefault(d['city'], []).append(d)
    return result


print(key_grouping_2(data))


# вывод должен быть такого вида :
# result = {
#     'Kiev': [
#         {'name': 'Viktor', 'age': 30},
#         {'name': 'Andrey', 'age': 34}],
#
#     'Dnepr': [{'name': 'Maksim', 'age': 20},
#               {'name': 'Artem', 'age': 50}],
#     'Lviv': [{'name': 'Vladimir', 'age': 32},
#              {'name': 'Dmitriy', 'age': 21}]
# }


# =======================================================
# 2) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.

def most_frequent(list_var):
    """
    This is a brute force approach in
    which we make use of for loop to count
    the frequency of each element
    :param list_var: line list
    :return: print most common string in a sequence
    """
    counter = 0
    number = list_var[0]
    for i in list_var:
        frequency = list_var.count(i)
        if frequency > counter:
            counter = frequency
            number = i
    return print(number)


def most_frequent_2(list_var):
    """
    Make a set of the list so
    that the duplicate elements are deleted.
    Then find the highest count of occurrences
    of each element in the set and thus, we
    find the maximum out of it.
    :param list_var: line list
    :return: print most common string in a sequence
    """
    return print(max(set(list_var), key=list_var.count))


most_frequent(['a', 'a', 'bi', 'bi', 'bi'])
most_frequent_2(['a', 'a', 'bi', 'bi', 'bi'])


# =======================================================
# 3) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.

def sum_numbers(any_number):
    """
    It counts the product of all digits
    in a number, except for zeros.
    :param any_number: any number
    :return: product of all digits
    in a number, except for zeros.
    """
    product = 1
    for i in (str(any_number)):
        if i != '0':
            product *= int(i)
    return product


print(sum_numbers(1023045))

# =======================================================
# 4) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.

my_array = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 1]


def raise_element(array, n):
    """
    Find the n-th degree of
    an element in an array
    with index n
    :param array: list of numbers
    :param n: item index
    :return: n-th degree of
    an element in an array
    with index n. If n is outside
    the array boundaries, then return -1.
    """
    return -1 if n >= len(array) else array[n] ** n


print(raise_element(my_array, 3))

# =======================================================
# 5) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.

my_str = "Line with words 1 and numbers 1 2 3 separated by spaces 2"


def triple_finder(some_str):
    """
    A function to determine if
    a line contains three words
    in a string. And displays them all.
    :param some_str: a line with words
    and numbers separated by spaces
    (one space between words and/or numbers)
    :return:print all three words in this string
    """
    triple = []
    for s in some_str.split():
        if s.isalpha():
            triple.append(s)
            if len(triple) == 3:
                print(*triple)
        else:
            del triple[:]


triple_finder(my_str)

import re


def re_triple_finder(string):
    """
    A function to determine if
    a line contains three words
    in a string using regular expressions
    :param string:
    :return: print only the first match in the string
    """
    str_match = re.search(r'\s+'.join([r'[^\d\s]+'] * 3), string)
    return print(str_match.group() if str_match else "not found")


re_triple_finder(my_str)
