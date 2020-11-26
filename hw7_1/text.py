"""
    Дан файл с текстом (text.txt).
    Создать новый файл (edited_text.txt), каждая строка которого получается из
    соответствующей строки исходного файла с обратным порядком слов, причем
    первое слово с заглавной буквы, а все остальные со строчной.
    Например 1 файл содержит:
    Hello world
    How are you
    Тогда второй файл будет содержать:
    World hello
    You are how
"""

file = open('text.txt', 'w')
file.write('Hello world \nHow are you')
file.close()


with open('text.txt', 'r') as file:
    for line in file:
        print(line)


file = open('hello.txt', 'w')
file.write('Hello world \nHow are you')
file.close()


with open("hello.txt", "r") as file:
    contents = file.readlines()
    str1 = contents[0]
    str2 = contents[1]
    print(str1, end = "")
    print(str2)
str_1 = str1.split()
str_1[-1],str_1[0] = str_1[0],str_1[-1]
print(' '.join(str_1.title())


with = open('edited_text.txt', 'w') as edited_text:
     text = edited_text.write(str_1)
#edited_text.write(str2 + str_1)
#edited_text.close()


with open("edited_text.txt", "r") as file:
    for line in file:
        print(line)
