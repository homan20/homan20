"""
программа рахує суму/різницю/множення/ділення n чисел
"""
n = int(input('Введіть число 1:'))
operation = input('Виберіть операцію: (+, -, * , /)')
k = int(input('Введіть число 2:'))
'''
operation = ['+', '-', '*', '/']
'''
while operation == '+'or'-'or '*'or '/':
    if operation == '+':
        print( n + k)
        break
    if operation == '-':
        print( n - k) 
        break
    if operation == '*':
        print( n * k) 
        break
    if operation == '/':
        print( n / k)        
        break
print('Continue? Y/N')

f = input()
while f == 'Y'or'N':
    if f == 'Y':
        print('Bye')
        break
    if f == 'N':
        print('Begin')
        break
        
        
        
      