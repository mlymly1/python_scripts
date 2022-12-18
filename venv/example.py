# объявление функции
def convert_to_python_case(text):
    s = text[0].lower()
    for i in text[1:]:
        if i.isupper():
            s = s + '_' + i.lower()
        else:
            s += i
    return s


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
