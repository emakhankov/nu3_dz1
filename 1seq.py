amount_of_elements = input('Введите кол-во элементов: ')
if amount_of_elements.isnumeric():
    amount_of_elements = int(amount_of_elements)
    list_of_numbers = list()
    for i in range(amount_of_elements):
        while True:
            entered_value = input(f'Введите {i+1} элемент списка: ')
            if entered_value.isnumeric():
                list_of_numbers.append(int(entered_value))
                break
            print('Введеное значение не число, вводите снова')

    list_of_numbers.sort()
    print(list_of_numbers)
else:
    print('Нужно было ввести число')

