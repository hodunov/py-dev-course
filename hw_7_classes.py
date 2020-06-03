# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)


class IpOperations(object):
    """
    Class for working with IP
    """
    def __init__(self, ip_list):
        self._ip_list = ip_list

    @property
    def addresses(self):
        """
        :return: IP address list
        """
        return self._ip_list

    @addresses.setter
    def addresses(self, new_ip_list):
        """
        :param new_ip_list: new IP address list
        :return: set new list
        """
        self._ip_list = new_ip_list

    def reversed_addresses(self):
        """
        Get the IP address list in reverse form
        :return: list
        """
        new_ip_list = []
        for ip in self._ip_list:
            new_ip_list.append('.'.join(ip.split('.')[::-1]))
        return new_ip_list

    def without_first_octets_list(self):
        """
        Get the IP address list without the first octets
        :return: list
        """
        new_ip_list = []
        for i in self._ip_list:
            new_ip_list.append(i[i.find('.') + 1:])
        return new_ip_list

    def last_octets_list(self):
        """
        Get a list of last octets of IP addresses
        :return: list
        """
        new_ip_list = []
        for i in self._ip_list:
            new_ip_list.append(i[i.rfind('.') + 1:])
        return new_ip_list


my_IP = IpOperations(["10.98.162.168", "10.11.12.13", "80.0.1.10"])
print(my_IP.addresses)
print(my_IP.reversed_addresses())
print(my_IP.without_first_octets_list())
print(my_IP.last_octets_list())


# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу
import json
import os


class JsonEditor(object):

    def __init__(self, json_file):
        self.json_file = json_file

    def write_file(self, data):
        """
        :param data: new data to write
        :return: write data to json
        """
        with open(self.json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def read_file(self):
        """
        Reading a file
        :return: file data
        """
        try:
            with open(self.json_file, "r") as read_file:
                data = json.load(read_file)
                return data
        except FileNotFoundError:
            print(f"File {self.json_file} not found")

    def merge_files(self, json_file2, final_file_name):
        json_data1 = self.read_file()
        json_data2 = JsonEditor(json_file2).read_file()
        results = [json_data1, json_data2]
        with open(final_file_name, 'w') as final_file:
            json.dump(results, final_file, indent=2)
        return final_file

    def get_path(self):
        return os.path.realpath(self.json_file)

    def get_abs_path(self):
        return os.path.abspath(self.json_file)


first_json = JsonEditor("data.json")
print(first_json.read_file())
first_json.merge_files("data_2.json", "data_3.json")
print(JsonEditor('data_3.json').read_file())
print(first_json.get_path())


# Задача-3
# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.

class Switch(object):
    """
    The class keeps the connection parameters
    """

    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    # using property decorator
    # a getter function
    @property
    def unit_name(self):
        return self._unit_name

    # a setter function
    @unit_name.setter
    def unit_name(self, name):
        self._unit_name = name

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, new_address):
        self._mac_address = new_address

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, new_ip):
        self._ip_address = new_ip

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, new_login):
        self._login = new_login

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password


switch_test = Switch("Unit_1", "13.12.11.10", "1234", "Art", "Lol_Kek")

print(switch_test.unit_name)
switch_test.unit_name = "Unit_2"
print(switch_test.unit_name)
