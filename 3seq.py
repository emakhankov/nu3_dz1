import re


def input_list():

    entered_string = input('Введите числа через запятую: ')
    if re.search(r'[^,\d ]', entered_string) and re.search(r'[^;\d ]', entered_string) \
            and re.search(r'[^/\d ]', entered_string):
        print(
            'В строке имеются иные символы чем числа, запятая, точка с запятой, слеш и пробел либо разделители разные')
        return None
    list_of_numbers = re.split(r' *[,;/] *', entered_string)
    return list_of_numbers


# Можно было преобразовать во множество, но в задании не сказано что элементы должны быть уникальыми


list_1 = input_list()
if not (list_1 is None):
    list_2 = input_list()
    if not (list_2 is None):
        for el in list_2:
            while el in list_1:
                list_1.remove(el)
print('Результат: ', ','.join(list_1))
