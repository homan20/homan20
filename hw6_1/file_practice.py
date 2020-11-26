"""
    Выполните все пункты.
    * можно описывать вложенные with open(), если это необходимо.
    * работа в основном с одним файлом, поэтому имя можно присвоить переменной
"""

# 1.
# Создайте файл file_practice.txt
# Запишите в него строку 'Starting practice with files'
# Файл должен заканчиваться пустой строкой

# 2.
# Прочитайте файл, выведете содержимое на экран
# Прочитайте первые 5 символов файла и выведите на экран

# 3.
# Прочтите файл 'files/text.txt'
# В прочитанном тексте заменить все буквы 'i' на 'e', если 'i' большее количество,
# иначе - заменить все буквы 'e' на 'i'
# Полученный текст дописать в файл 'file_practice.txt'

# 4.
# Вставьте строку '*some pasted text*'.
# Если после вставки курсор остановился на четной позиции
#   - добавить в конец файла строку '\nthe end',
# иначе - добавить в конец файла строку '\nbye'
# Прочитать весь файл и вывести содержимое

#1.
file_practice = open('file_practice.txt', 'w')
file_practice.write('Starting practice with files \n\n')
file_practice.close()

#2.
with open ('file_practice.txt', 'r+') as file_practice:
    line = file_practice.readline() 
    print(line)

with open('file_practice.txt', 'r+') as file_practice:
    line = file_practice.readline(5) 
    print(line)

#3.
text_1 = open('text_1.txt', 'w')
text_1.write('Proin laoreet dui vel libero dapibus vehicula vitae eget turpis.\n'
             'Nam non eros eu elit posuere posuere id ac turpis.\n'
             'Quisque nec orci blandit, lobortis felis non, eleifend felis.\n'
             'Vivamus at odio at lacus viverra luctus et ut mauris.\n'
             'Etiam vehicula nibh eu quam feugiat tempus.')
text_1.close()

with open('text_1.txt', 'r+') as f:
    text = f.read()
    chars_i = text.count('i')
    chars_e = text.count('e')

    if chars_i > chars_e:
        print(text.replace('i', 'e'))
    else:
        text_2 = text.replace('e', 'i')
        print(text_2, end="\n\n")
    
lines = [text_2]
with open('file_practice.txt', 'a+') as file_practice:
    for  line in lines:
        file_practice.write(line + '\n')

with open('file_practice.txt', 'r+') as f:
    text = f.read()
    print(text)

#4.
with open('file_practice.txt', 'a+') as f:
    print('*some pasted text*', file=f)
    s = f.tell()
    if s % 2 == 0:
        print('\nthe end', file=f)
    else:
        print('\nbye', file=f)

with open('file_practice.txt', 'r') as f:
    text = f.read()
    print(text)   
    