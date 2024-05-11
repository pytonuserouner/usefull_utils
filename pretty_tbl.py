from prettytable import PrettyTable

"""
Красивый вывод табличных данных
"""

table = PrettyTable()

table.field_names = ['Names', 'Password', 'Sex', 'Age']
table.add_row(['Anna', 'qwerty', 'fimale', '25'])

print(table)
