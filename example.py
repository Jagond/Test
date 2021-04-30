'''
Задача 1

Ввести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

# for i in range(0,5):
#     print(i+1, '0')

'''
Задача 2

Пользователь в цикле ввод 10 цифр, найти количество введенных пользователем цифр 5 
'''

# num = int(input("Сколько будет чисел? "))
# out = int(input("Какую цифру считать? "))
# count = 0
# for i in range (1,1+num):
#     number = int(input("Число " + str(i) + ": "))
#     while number > 0:
#      if number%10 == out:
#       count += 1
#      number = number // 10
# print("Было введено %d цифр %d" % (count, out))

'''
Задача 3
найти сумму ряда чисел от 1 до 100. Полученный результат высвести на экран
'''
# sum = 0
# for i in range(1,101):
#     sum += i
# while i <=100:
#     break
# print(sum)

'''
Задача 4
Найти произведение ряда чилел от 1 до 10. Полученый результат вывести на экран
'''
# n = 1
# for i in range(1,10):
#     n *= i
# while i <= 10:
#   break
# print(n)

'''
Задача 5
Вывести цифры числа в каждой строчке
'''
# int_number = int(input("Vvedi chislo: ")[::-1])
# #print(int_number%10, int_number//10)
# while int_number>0:
#     print(int_number%10)
#     int_number = int_number//10

'''
Задача 6
Найти сумму цифр числа
'''
# u = int(input('Chislo:'))
# sum = 0
# while u>0:
#     digit = u%10
#     sum += digit
#     u = u // 10
# print(sum)
'''
Задача 7
Найти произведение цифр числа
'''
# m = int(input('Chislo:'))
# mult = 1
# while m>0:
#     digit = m%10
#     mult *= digit
#     m = m // 10
# print(mult)
'''
Задача 8
Ответить на вопрос, есть ли среди числа цифра 5
'''
# int_number = int(input("Vvedi chislo: "))
# #print(int_number%10, int_number//10)
# while int_number>0:
#     if int_number%10 == 5:
#         print("Yes")
#         break
#     int_number = int_number//10
# else:print('No')
'''
Задача 9
Найти максимальную цифру в числе
'''
# int_number = int(input("Vvedi chislo: "))
# max = int_number%10
# int_number = int_number//10
# while int_number > 0:
#     if int_number%10 > max:
#         max = int_number%10
#     int_number = int_number//10
# print(max)
'''
Задача 10
Найти количество цифр в числе
'''
# num = int(input("Введите число "))
# out = int(input("Какую цифру считать? "))
# count = 0
# while num > 0:
#      if num%10 == out:
#       count += 1
#      num = num // 10
# print("Было введено %d цифр %d" % (count, out))