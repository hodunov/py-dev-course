import random


def consonants_to_vowels(some_string):
    vowels = 'aeiouAEIOU'
    for letter in some_string:
        for vowel in vowels:
            if letter.isalpha() and letter not in vowels:
                some_string = some_string.replace(letter, random.choice(vowels))
    print(f'Encoded: {some_string}')


consonants_to_vowels(str(input('print something to encode: ')))