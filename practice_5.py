# Создайте класс Student,
# который содержит атрибуты:
# фамилия и инициалы, номер группы, успеваемость (дикт элементов).
# Создать класс UserInfoAggregator(), который будет принимать на вход данные о студентах(data_context).
# У него должен быть метод создания экземпляров класса Students и хранения этих студентов в коллекции.
# Класс должен иметь возможность вывода фамилий и номеров групп студентов, имеющих оценки,
# равные только 4 или 5.
from prettytable import PrettyTable


class Group(object):
    """
    Main group class
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Student(object):
    """
    Main students class
    """

    def __init__(self, first_name, last_name, group, progress):  # progress = dict
        self.first_name = first_name
        self.last_name = last_name
        self.group = Group(group)
        self.progress = progress


all_data = [("Artem", "Hodunov", "Python", {"hw1": 5, "hw2": 4}),
            ('Edem', "Orlov", 'DevOps', {"hw1": 4, "hw2": 4}),
            ('Oleg', "Ivanov", 'Java', {"hw1": 3, "hw2": 2}),
            ('Max', "Mikhailenko", 'Python', {"hw1": 5, "hw2": 5}),
            ('Margo', "Robbie", '1C', {"hw1": 5, "hw2": 2})]


class UserInfoAggregator(object):
    students = []

    def __init__(self, data_context):
        self.data_context = data_context

    def create_students(self):
        """
        This method creates student objects
        :return: add objects to students list
        """
        for i in self.data_context:
            first_name, last_name, group, progress = i
            self.students.append(Student(first_name, last_name, group, progress))

    def show_students(self):
        """
        :return: Prints the student table
        """
        t = PrettyTable(["First Name", "Last Name", "Group", "Progress"])
        for i in self.students:
            t.add_row([i.first_name, i.last_name, i.group, i.progress])
        print(t)

    def show_successful(self):
        """
        :return: prints list of successful students
        """
        successful_students = []

        for i in self.students:
            for key, value in i.progress.items():
                if value > 3:
                    if i not in successful_students:
                        successful_students.append(i)
                if value < 3:
                    if i in successful_students:
                        successful_students.remove(i)

        table = PrettyTable(["First Name", "Last Name", "Group"])

        for i in successful_students:
            table.add_row([i.first_name, i.last_name, i.group])
        print("| List of students with 4 and 5 grades |\n", table)


first_course = UserInfoAggregator(all_data)
first_course.create_students()
first_course.show_students()
first_course.show_successful()
