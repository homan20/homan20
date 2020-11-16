import random
import string

print(
'''
Select password generation option:  \n
    option 1 - simple password (lowercase letters only, 8 characters); \n
    option 2 - average password (any letters and numbers of 8 characters);\n
    option 3 - complex password (at least 1 uppercase letter, 1 lowercase, \n
    1 digit and 1 special character, length from 8 to 16 characters).\n
'''
)

def main():
    
    option = int(input('Enter the option number:'))
    
    if option == 1:
        print(passw_1())

    elif option == 2:
        print(passw_2())

    elif option == 3:
        print(passw_3())

    else:
        print('enter the correct option number')  

def passw_1():
    chars = string.ascii_lowercase
    size = random.randint(8,8)
    return ''.join(random.choice(chars) for x in range(size))

passw_1()

def passw_2():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits 
    size = random.randint(8,8)
    return ''.join(random.choice(chars) for x in range(size))

passw_2()

def passw_3():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    chars = chars.replace('-', '/')

    lowers = 0
    uppers = 0
    digits = 0
    punctuations = 0
    for i in chars:
        if i.islower() and i.isupper() and i.isdigit() and i.ispunctuation() >=1:
            pass
        else:
            continue
    size = random.randint(8,16)
    return ''.join(random.choice(chars) for x in range(size))

passw_3()

main()
