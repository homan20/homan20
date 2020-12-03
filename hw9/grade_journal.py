"""
    Пользователь вводит количество студентов n.
    После чего вводит n строк, в которых записана фамилия и балл через пробел.
    Программа выводит список фамилий, отсортированный по их баллам по убыванию.
    Пример:
    [out] Введите количество студентов:
    [in]  3
    [out] Введите фамилию и балл:
    [in]  Иванов 87
    [out] Введите фамилию и балл:
    [in]  Смирнов 90
    [out] Введите фамилию и балл:
    [in]  Фролов 89
    [out]
        1. Смирнов
        2. Фролов
        3. Иванов
"""

def student_dict(n):
    d = {}
    for i in range(n):
        word_list = input(f'{i + 1} Введіть фамілію і бал: ')
        if i == n:
            d = word_list
            return d
        else:
            student_dict(n)

'''
def swap_items(d):
    modified_dict = {}
    for k, v in d.items():
        for i in v:
            values = modified_dict.get(i, [])
            values.append(k)
            modified_dict[i] = values
    return modified_dict
'''

def main():

    n = int(input('Введіть кількість студентів: '))


    first_dict = student_dict(n)
    print(first_dict)


main()
