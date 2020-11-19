'''
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


def main():
    phone = input_phone()
    email = input_email()
    password = input_password()
    print()

def input_phone(): ...

def input_email(): ...

def input_password(): ...

main()

'''

def main():

    phone = input_phone()
    email = input_email()
    password = input_password()
    print(
        f'Congratulations on your successful registration! \n' 
        f'You number phone {phone}\n'f'You email: {email}\n'
        f'You password {password}\n'
        )
    
def input_phone():

    phone = input('Enter you number phone: ')
    phone = phone.replace(' ','').replace('-','').replace('(','').replace(')','')
    if  len(phone) > 12 and phone == None:
        return input_phone()
    else:
        phone = '+38' + phone[-10:]
    return phone


def input_email():

    email = input('Enter email: ')
    if email.count('@') != 1:
        return input_email()
    if len(email) < 7:
        return input_email()
    return email


def input_password():
    global password
    password = input('Enter the password: ')
    if password.isspace():
        return input_password()
    elif len(password) < 8:
        return input_password()
    elif password.isupper and password.islower() and password.isdigit() < 1:
        print('The password must contain at least 1 uppercase letter, 1 lowercase letter, 1 digit')
        return input_password() 
    return password_2()

def password_2():

    password_2 = input('Enter the password again to verify:')
    if password_2 != password:
        return password_2()
    return password

main()