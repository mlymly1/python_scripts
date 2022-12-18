# объявление функции
import math


def is_valid_password(password):
    password = password.split(':')

    if len(password) != 3:
        return False
    elif len(password) == 3:

        a = password[0]
        b = password[1]
        c = password[2]

    return is_palindrome_easy(a) and is_digit_simple(b) and is_even_number(c)


def is_palindrome_hard(text):
    if len(text) % 2 == 1:
        text1 = text[0:(len(text)) // 2]
        text2 = text[::-len(text) // 2]
        return text1 == text2

    elif len(text) % 2 == 0:
        text1 = text[0:(len(text)) // 2]
        text2 = text[-1:-len(text) // 2 - 1:-1]
        return text1 == text2





def is_even_number(num):
    return int(num) % 2 == 0


def is_palindrome_easy(text):
    return text == text[::-1]


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# считываем данные
# psw = input()

# вызываем функцию
# print(is_valid_password(psw))
