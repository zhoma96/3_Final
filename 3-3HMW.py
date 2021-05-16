def my_func(number1, number2, number3):
    conv_list = [number1, number2, number3]
    try:
        conv_list.remove(min(conv_list))
        return conv_list
    except TypeError:
        return 'Numbers Only'
print(my_func(input('Number_1:'), input('Number_2:'),input('Number_3:')))