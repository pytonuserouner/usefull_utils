import random
import string

""" Классический пример генерации простых паролей заданной длины """

total = string.ascii_letters + string.digits + string.punctuation
length = 16
password = "".join(random.sample(total, length))
print(password)
