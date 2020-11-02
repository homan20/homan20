# Магічне число
import random
 
number = random.randint(0, 20)
# print(number)
 
while True:
    temp = input('Вгадай число: ')
    if temp == "" or temp == "exit":
        print("Вихід з програми")
        break
 
    if not temp.isdigit():
        print("Введи правильне число")
        continue
 
    temp = int(temp)
 
    if temp == number:
        print('Вірно!')
        break
 
    elif temp > number:
        print('Загадане число більше')
    else:
        print('Загадане число менше')
