# При запуску програми робимо вибір:
def main():
    option = int(input('Todo list: \n'
                       '1. Добавити нову замітку.\n'
                       '2. Дивитися всі замітки. \n'
                       '3. Видалити замітку.\n'
                       ))
    if option == 1:
        new_note()
    elif option == 2:
        print(see_notes())
    elif option == 3:
        print(del_notes())
    else:
        print('Введіть коректний номер')

# Вносимо дату і зміст замітки.
def new_note():
    new_data = input('дата:\n')
    with open('new_note.txt', 'a+') as new_note:
        # Записуємо дату в файл.
        print(new_data, file=new_note, sep='', end=' ')
        # Записуємо замітку в файл з попередньо збереженою датою.
    new_notes = input('замітка:  \n')
    with open('new_note.txt', 'a+') as new_note:
        print(new_notes, file=new_note, sep='', end='\n')

# Повний перегляд заміток.      

def see_notes():
    line_number = 0
    with open('new_note.txt', 'r+') as new_note:
        for line in new_note:
            line_number += 1
            # Виведення номеру рядка і відповідно замітки.
            print('{:>4} {}' .format(line_number, line.rstrip()))

# Імпортування модулю os для можливості перейменування файла.
import os

# Видалення замітки по номеру рядка.

def del_notes():
    # Виведення повного списку заміток.
    print(see_notes())
    # Введення номеру рядка(замітки).
    del_line = int(input('номер замітки для видалення:'))
    # Відкриття файлу new_note.txt для читання.
    with open('new_note.txt', 'r+') as inf:
        # Створення файлу out.txt для внесення змін.
        with open ('out.txt','w+') as ouf:
            # Викорисання фунції enumerate для проходження по 
            # початкових номерах рядків починаючи з 1.
            for num_line, line in enumerate(inf, start=1):
                if num_line != del_line:
                    # Запис всіх рядків крім рядка з початковим
                    #  номером del_line в файл out.txt.
                    ouf.write(line)
    # Використовуємо функцію os.rename для перейменування файла 
    # out.txt в new_note.txt.                
    os.rename('out.txt', 'new_note.txt')
        
main()
