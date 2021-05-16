def info(**kwargs):
    return ' '.join(kwargs.values())

name = input('Name: ')
Surname = input('Surname: ')
Birthyear = input('Birthyear: ')
city = input('City: ')
email = input('email: ')
phone = input('Phone: ')

print(info(name=name, Surname=Surname, Birthyear=Birthyear, city=city, email=email, phone=phone))