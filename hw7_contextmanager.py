# Задача-1
# Создать объект менеджера контекста который будет переходить в папку которую он принимает на вход.
# Так же ваш объект должен принимать исключение которое он будет подавлять Если флаг об исключении отсутствует,
# исключение должно быть поднято.
import os
from contextlib import contextmanager
import time


class GoTo(object):
    """
    This is the context manager's object that
    will be navigated to the folder he accepts as his login.
    This object accepts an exception that it will suppress
    If the exception flag is missing, the exception must be raised.
    """
    def __init__(self, path, *flag):
        self.path = os.path.expanduser(path)
        self.flag = flag

    def __enter__(self):
        self.saved_path = os.getcwd()
        try:
            os.chdir(self.path)
        except self.flag as e:
            print(f"The {e.__doc__} exception has been suppressed")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.saved_path)


with GoTo('world.txt', FileNotFoundError) as cd:
    print(cd.saved_path)


# Задача -2
# Описать задачу выше но уже с использованием @contexmanager


@contextmanager
def ChangeDirectory(path, *exception):
    """
    Directory change function,
    which performs the same function as the object in task 1,
    but using @contexmanager
    :param path: your path to file
    :param exception: exception that may arise (to be suppressed)
    :return: directory change
    """
    previous_path = os.getcwd()
    try:
        os.chdir(path)
    except exception as e:
        print(f"The {e.__doc__} exception has been suppressed")
    try:
        yield
    finally:
        os.chdir(previous_path)


with ChangeDirectory('word.txt', FileNotFoundError) as cd2:
    print(os.getcwd())

#
# Задача -3
# Создать менеджер контекста который будет подсчитывать время выполнения вашей функции


class TimeChecker(object):
    """
    context manager that will calculate the function's execution time
    """
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        result = end - self.start
        print(f"Function ends with time = {result}")


with TimeChecker() as tc:
    time.sleep(1)
