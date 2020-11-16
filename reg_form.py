"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.
    !!! Для решения необходимо использовать функции и рекурсию, а не циклы. !!!
    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)
    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер
    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.
    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа
    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.
        Программа выводит сообщение:
        Поздравляем с успешной регистрацией!
        Ваш номер телефона: +380501234567
        Ваш email: example@mail.com
        Ваш пароль: **********
"""

import random
def main():
    
    def input_phone():
        phone_number = input('Enter phone number:')
        number = ''
        for i in phone_number:
            if i.isdigit():
                number += i

        number = number[-9:]
        n = '+380'+ number
        if len(n)< 11:
            print('The number is entered incorrectly') 
        else:
            print(n)
           

    input_phone()


    def input_email():

        characters_email = input('Enter email:')
        c = characters_email

        while True:
            if c.count('@') == 1 and len(c) > 7 :
                print(c)
            else:
                print(input('Enter the correct email: mailbox@domain.name: '))
            break
        if len(c) <= 7:
            print('small number of characters, less than 6',input())
        #print( input('Enter again email: '))

    input_email()
    
    def input_password():
     
        password = input('Enter the password: ')

        while True:

            if password.isspace():
                print('The password contains spaces')

            elif len(password) < 8:
                print('The password is short')
    
            elif password.isupper and password.islower() and password.isdigit() < 1:
                print('The password must contain at least 1 uppercase letter, 1 lowercase letter, 1 digit')

            else:
                print(password)
                break
            password = input('Enter the password again: ')

        print('Enter the password again to verify')
        password_2 = input()
        while True:
            if password_2 == password:
                print('OK')
                break
            else:
                print('Re-enter')
                password2 = input()
            if password2 == password:
                print('OK')
                break
        
    input_password()

main()

