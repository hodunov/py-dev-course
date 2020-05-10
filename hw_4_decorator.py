# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.


def divided_by_100(func):

    def inner(*args, **kwargs):
        res = 100 % func(*args, **kwargs)
        if res == 0:
            print("We are OK!")
        else:
            print(f"Bad news, guys, we got {res}")

    return inner


@divided_by_100
def my_sum(a, b):
    return a + b


my_sum(12, 3)
my_sum(7, 3)


# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))


def check_type(func):
    def checker(*args):
        if type(*args) is int:
            func(*args)
        if type(*args) is str:
            raise ValueError("string type is not supported")

    return checker


@check_type
def multiplier(a):
    return a * 100


multiplier(12)
multiplier('12')


# ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
# количество раз обращений в cache.

def caching(func):
    cache = {}
    count_ch = 0
    count_func = 0

    def decorate(*args):
        nonlocal count_ch
        nonlocal count_func
        if args in cache:
            count_ch += 1
            print(f"Used cache with counter = {count_ch}")
            return cache[args]
        else:
            count_func += 1
            cache[args] = func(*args)
            print(f"Function executed with counter = {count_func}, function result = {cache[args]}")
            return cache[args]

    return decorate


@caching
def add_ver(abc):
    return abc + " ver1"

add_ver('abc')
add_ver('abc')
add_ver('abc')
