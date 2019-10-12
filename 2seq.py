import re
entered_string = input('Введите числа через запятую: ')
if re.search(r'[^,\d ]', entered_string) and re.search(r'[^;\d ]', entered_string) \
        and re.search(r'[^/\d ]', entered_string):
    print('В строке имеются иные символы чем числа, запятая, точка с запятой, слеш и пробел либо разделители разные')
else:
    list_of_numbers = re.split(r' *[,;/] *', entered_string)
    list_of_unique_numbers = list(set(list_of_numbers))
    # тут про сортировку в задании нет
    print('Результат: ', ','.join(list_of_unique_numbers))