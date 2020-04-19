"""
1) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).
 keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 ожидаемый результат: {1: 1, 2: 4, 3: 9 …} 
"""

my_dict = {i: (i ** 2) for i in range(1, 11)}
print(my_dict)

"""
2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа. 
"""

my_list = [i for i in range(1, 101)]
resulting_list = sorted(my_list, key=lambda item: item % 2)
print(resulting_list)

"""
3)Заменить в произвольной строке согласные буквы на гласные.  
"""
import random

Vowel = "aeiou"


def isVowel(my_ch):
    ch = my_ch.lower()
    if ch not in Vowel:
        return False
    return True


def replaceConsonants(s):
    for i in range(len(s)):
        if not isVowel(s[i]):
            if s[i] == ' ':
                pass
            else:
                s[i] = random.choice(Vowel)
    return ''.join(s)


my_str = "programming is awesome"
print(my_str)
print(replaceConsonants(list(my_str)))

"""
4)Дан массив чисел. [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]  
4.1) убрать из него повторяющиеся элементы 
4.2) вывести 3 наибольших числа из исходного массива  
4.3) вывести индекс минимального элемента массива
4.4) вывести исходный массив в обратном порядке 
"""

my_array = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

clean_array_one = list(set(my_array))  # убрать повторяющиеся элементы с потерей порядка
clean_array_two = list(dict.fromkeys(my_array))  # dict гарантирует порядок ключей, который был использован при вставке
print("Clean array = ", clean_array_two)

my_second_array = sorted(my_array)  # отсортируем массив
print("Highest numbers =", my_second_array[-3:])  # выведем 3 наибольших числа из исходного массива

print("Minimum value index", my_array.index(min(my_array)))

print("Reversed array", list(reversed(my_array)))

"""
5) Найти общие ключи в двух словарях: 
dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
dict_two = {'a': 6, 'b': 8, 'z': 20, 'x': 40}
"""

dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_two = {'a': 6, 'b': 8, 'z': 20, 'x': 40}
common_keys = set(dict_one.keys()).intersection(dict_two.keys())

print("Common keys is", common_keys)
