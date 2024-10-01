import re

def how_strong_pas(password):
    validation = r'^(?=.*[а-я]|.*[a-z])(?=.*[A-Z]|.*[А-Я])(?=([А-Яа-яA-Za-z\d@$!%*#?&]{8,}))'
    if re.match(validation, password):
        return True
    else:
        return False

password = input('Введите пароль: ')

if how_strong_pas(password):
    print('Действительный пароль')
else:
    print('Пароль не соответствует требованиям')
