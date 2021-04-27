#Цикл For
#=======
# for i in range(10):     #range(start,stop,step)
#     print(i)
#     if i == 5: break

# for i in range(10):
#     answer = input('Какая у вас машина?')
#     if answer == 'Volvo':
#      print('Все верно')
#      break

for i in range(10):     #range(start,stop,step)
    if i == 9: break
    if i <3: continue
    print(i)

# while i < 10:
#     print(i)
#     i = i + 1
#     if i == 5: break