# Задача-1
# Реализовать дескриптор валидации для аттрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить
import re


class EmailNotValidError(ValueError):
    """This custom exception occurring when entering the wrong e-mail"""
    pass


class EmailDescriptor:
    def __get__(self, instance, owner):
        return self.email

    def __set__(self, instance, value):
        if re.match(r'[\w.-]+@[\w.-]+.\w+', value) is not None:
            print("valid email :::", value)
            self.email = value
        else:
            print("not valid:::")
            raise EmailNotValidError('Error with this email')


class MyClass:
    email = EmailDescriptor()


my_class = MyClass()

my_class.email = "validemail@gmail.com"

my_class.email = "novalidemail"  # Raised Exception


# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass


c = MyClass()
b = MyClass()
assert id(c) == id(b)


# Задача-3
# реализовать дескриптор IngegerField(), который будет хранить уникальные
# состояния для каждого класса где он объявлен

class IngegerField:
    def __get__(self, instance, owner):
        return instance._number  # return self.value

    def __set__(self, instance, value):
        instance._number = value  # self.value = value


class Data:
    number = IngegerField()


data_row = Data()
new_data_row = Data()

data_row.number = 5
new_data_row.number = 10

assert data_row.number != new_data_row.number
