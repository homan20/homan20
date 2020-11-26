#Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
#Переписать в файл (edited_phone_book.txt) телефоны владельцев,
#чьи имена начинаются на букву "м" либо заканчиваются на "а"
#(регистр не имеет значения).
#Перед записью в файл привести номер к формату +380501234567.

import re

with open('phone_book.txt', 'w') as f:
    text = f.write(
    'Влад 380993889900 \n'
    'Юра (73) 184-34-98 \n'
    'Аврора +38(073)176-21-00 \n'
    'Стас 38050 789 90 21 \n'
    'Марина 38(066) 123  33 77 \n'
    'Анна   +380 99 364 66 73 \n'
    'Михаил 063 789 55 67 \n')

with open('phone_book.txt', 'r') as phone_book:
    text = phone_book.read()
    #list = text.split()
    #print(list)
'''
string = text
name = re.findall(r'\D?[^()+' '-]', string)
names = ''.join(name)
print(names, end=' \n')
'''

string = text
for w in string.split():
    if (w.startswith('М') or w.endswith('а')):
        name_s = w
        print(name_s)

number = string
char = re.findall(r'\d?\W?', number)
charss = ''.join(char)
print(charss)


with open('phone_book.txt', 'r') as phone_book:
    text = phone_book.read().splitlines()
    el = 0
    for element in text:
        el += 1
        char = re.sub(r'\D+', '', element)
        phone = '+380'+ char[-9:]
        phones = ''.join(phone)
print(phones)

with open('edited_phone_book.txt', 'w') as f:
    f = f.write(name_s)

with open('edited_phone_book.txt', 'r') as f:
    f = f.read()
    print(f)