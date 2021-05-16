def sum_num():
    n = 0
    while True:
        numbers_list = input('Input number with space: ').split()
        for num in numbers_list:
            if num == 'a':
                return n
            else:
                try:
                    n += int(num)
                except ValueError:
                    print('Error')
        print(n)
print(sum_num())
