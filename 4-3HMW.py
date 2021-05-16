def my_func(x,y):
    try:
        res = x ** y
    except TypeError:
        return 'Error'
    return res
print(my_func(float(input('x:')),int(input('y:'))))
