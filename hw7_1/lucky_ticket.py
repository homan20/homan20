"""
    Написать функцию, которая будет проверять счастливый билетик или нет.
    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""

ticket_num = list(map(int, input()))


def is_lucky(ticket_num):
    a = ticket_num
    if len(a) % 2 == 1:
        print("No Luck")
        return ticket_num

    elif sum(a[:len(a)//2]) == sum(a[len(a)//2:]):
        print("Luck")
        return ticket_num
        
    else:
        print("No Luck")
        return ticket_num
        
is_lucky(ticket_num)

'''
assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True
'''
