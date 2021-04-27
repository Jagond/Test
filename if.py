#Оператор условия
#================

brand = 'Ford'
engine_volume = 1.6
horsepower = 99
sunroof = False

#Проверка условия if

# if horsepower < 100:
#     print('no tax')

#Проверка условия if\else

# if horsepower < 100:
#      print('no tax')
#      print('no tax')
#      print('no tax')
# else:
#     print('Tax')

# короткая запись
# if horsepower < 100:print('no tax')
# else:print('Tax')

# Проверка условия if/elif/elif/else
tax = 0
if horsepower < 80:
    tax = 0
elif horsepower < 100:
    tax = 10000
elif horsepower < 150:
    tax = 20000
else:
    tax = 50000
print('tax=', tax, sep='')

# Проверка условия if для присваивания



