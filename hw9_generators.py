import functools

# Задача-1
# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерировании по генератору необходимо проверять строки на уникальность.
# Если строка уникальна, тогда ее выводим на экран, если нет - скипаем


def str_generator(file, seen=None):
    seen = set(seen or [])
    with open(file) as f:
        for line in f.readlines():
            if line not in seen:
                seen.add(line)
                yield line.strip()


print(list(str_generator('words.txt')))


"""""
Задача-2 (оригинальный вариант и его делать не обязательно):
представим есть файл с логами, его нужно бессконечно контролировать
на предмет возникнования заданных сигнатур.

Необходимо реализовать пайплайн из корутин, который подключается к существующему файлу
по принципу команды tail, переключается в самый конец файла и с этого момента начинает следить
за его наполнением, и в случае возникнования запиcей, сигнатуры которых мы отслеживаем -
печатать результат

Архитектура пайплайна
                   --------
                  /- grep -\
dispenser(file) <- - grep - -> pprint
                  \- grep -/
                   --------
Структура пайплайна:
"""""


def coroutine(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        next(result)
        return result

    return inner


@coroutine
def grep(pattern, target):
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)


@coroutine
def printer():
    try:
        while True:
            line = (yield)
            print(line)
    except GeneratorExit:
        print("Pipeline Ended")


@coroutine
def dispenser(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)


def follow(file, target):
    file.seek(0, 2)
    try:
        while True:
            line = file.readline()
            if not line:
                continue
            target.send(line)
    except StopIteration:
        print("Pipeline Ended")


"""""
Каждый grep следит за определенной сигнатурой
"""""


with open("words.txt", "r") as f_open:
    follow(f_open, dispenser([grep('python', printer()),  # отслеживаем
                              grep('is', printer()),  # заданные
                              grep('great', printer())])  # сигнатуры
           )


"""
Как только в файл запишется что-то содержащее ('python', 'is', 'great') мы сможем это увидеть

Итоговая реализация фактически будет асинхронным ивент хендлером, с отсутствием блокирующих операций.

Если все плохо - план Б лекция Дэвида Бизли
[warning] решение там тоже есть :)
https://www.dabeaz.com/coroutines/Coroutines.pdf
"""

"""
Задача-3 (упрощенный вариант делаете его если задача 2 показалась сложной)
Вам нужно создать pipeline (конвеер, подобие pipeline в unix https://en.wikipedia.org/wiki/Pipeline_(Unix)).

Схема пайплайна :
source ---send()--->coroutine1------send()---->coroutine2----send()------>sink

Все что вам нужно сделать это выводить сообщение о том что было получено на каждом шаге и обработку ошибки GeneratorExit.

Например: Ваш source (это не корутина, не генератор и прочее, это просто функция ) в ней опеделите цикл из 10 элементов
которые будут по цепочке отправлены в каждый из корутин и в каждом из корутив вызвано сообщение о полученном элементе.
После вызова .close() вы должны в каждом из корутин вывести сообщение что работа завершена.
"""


def source_func(source, cor):
    for number in source:
        cor.send(number)
    cor.close()


def coroutine1(to_coroutine):
    print("Let's check your number")
    try:
        while True:
            number = (yield)
            if number % 5:
                print(f"1) Obtained number {number}")
                to_coroutine.send(number)
    except GeneratorExit:
        print("End of function corounite1")


def coroutine2():
    print("Let's check your number again")
    try:
        while True:
            number = (yield)
            print(f"2) Now I'm obtained number {number}")
            if number > 20:
                print(f"3) Your number {number} bigger than 20")
    except GeneratorExit:
        print("End of function corounite2")


my_data = [1, 10, 12, 15, 25, 27, 29, 30, 50, 49]

# source_func(my_data, coroutine1(next(coroutine2()))) ?? doesn't work
