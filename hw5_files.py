# Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.
from re import findall


def remover(file_name):
    """
    :param file_name:
    :return:
    """
    new_content = ""  # This is new content for our text file
    with open(file_name, "r+") as file:
        for line in file:
            del_worlds = findall(r"\b[a-zA-Z]{3,5}\b", line)
            if len(del_worlds) % 2 == 1:
                del_worlds.pop()
            for word in del_worlds:
                line = line.replace(word, '')
            new_content += line
        file.seek(0)
        file.truncate()
        file.write(new_content)


# remover("words.txt")

# Текстовый файл содержит записи о телефонах и их владельцах.
# Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.


def phone_numbers(file_in, file_out):
    with open(file_in) as f_in, open(file_out, 'w') as f_out:
        for line in f_in:
            words = line.split()
            if words[2].startswith(('K', 'C')):
                f_out.write(line)


# phone_numbers('phone_numbers.txt', 'phone_numbers_2.txt')


# Получить файл g, в котором текст выровнен по правому краю путем равномерного добавления пробелов.


def align_right(file_in, file_out):
    """Aligns the text from 'in_file' right and writes the result to 'out_file' (page width is 120)"""
    with open(file_in, "r") as file_in, open(file_out, "a") as file_out:
        for line in file_in:
            file_out.write(line.rjust(120))


# align_right("words.txt", "words2.txt")

# Дан текстовый файл со статистикой посещения сайта за неделю.
# Каждая строка содержит ip адрес, время и название дня недели
# (например, 139.18.150.126 23:12:44 sunday).
# Создайте новый текстовый файл, который бы содержал список ip
# без повторений из первого файла. Для каждого ip укажите количество посещений,
# наиболее популярный день недели. Последней строкой в файле
# добавьте наиболее популярный отрезок времени в сутках длиной один час в целом для сайта.
