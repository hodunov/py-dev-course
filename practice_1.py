# Task1
# Take a string with a couple words and returns the length of the longest word.


def longest_word(string):
    result = ''
    for word in string.split():
        if len(word) > len(result):
            result = word
    return result


def longest(some_words):
    """I found a more beautiful answer after googling"""
    return max(some_words.split(), key=len)


print(longest_word("Full Dark No Stars"))
print(longest("No One Is Sure What Happens Next"))


# Task2
# Change a given string to a new string where the first and last chars have been exchanged.
# print(change_sring('abcd'))  # dbcd
# print(change_sring('12345')) # 52341


def change_string(str1):
    return str1.replace(str1[:1], str1[-1:])


print(change_string("abcd"))
print(change_string("54321"))


# Task3
# # Sum all the items in a given list


def list_sum(list1):
    counter = 0
    for element in list1:
        counter += element
    return counter


print(list_sum([10, 11, 12]))


# Task4
# Return the largest number from a list

def largest_number(list_1):
    return max(list_1)


print(largest_number([1, 3, 4, 6, 7, 8]))


# Task5
# Return the smallest number from a list

def smallest_number(list_1):
    return min(list_1)


print(smallest_number([1, 3, 4, 6, 7, 8]))


# Taks6
# Take two lists and returns True if they have at least one common member


def common_member(list1, list2):
    result = False
    if len(set(list1) & set(list2)) != 0:
        result = True
    return result


print(common_member([10, 23, 34], [10, 22, 33]))
print(common_member([10, 23, 34], [1, 22, 33]))

# Task7
# Map two lists into a dictionary.
keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']


def create_dict(key, value):
    return dict(zip(key, value))


print(create_dict(keys, values))

# Task8
# Convert a tuple to a string.

tuple1 = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')


def str_converter(some_tuple):
    str1 = ""
    for element in some_tuple:
        str1 += element
    return str1


def convert_tuple(tup):
    """Beautiful answer after googling"""
    result_str = ''.join(tup)
    return result_str


print(str_converter(tuple1))
print(convert_tuple(tuple1))

# Task9
# Unpack a tuple in several variables.

tuple2 = (999, 666, 777)
alpha, beta, gamma = tuple2  # there's no way to make it a function?

print(f"alpha is {alpha}, beta is {beta}, gamma is {gamma}")
