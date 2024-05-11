import hashlib


"""
Авторизация пользователя с использованием hash пароля
"""


def my_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()


hash_password = '54b522e8e26130ce07bd9ef1b5d54da96b8feea3df9f855a90c4dbe70f24656a'
input_password = input('Ваш пароль: ')
autorizate_hash_password = my_hash(input_password)

if hash_password == autorizate_hash_password:
    print('Вы авторизованы')
else:
    print('Неверный пароль')

