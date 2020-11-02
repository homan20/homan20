# Алгоритм Евкліда
a = int(input('Enter a: '))
b = int(input('Enter b: '))

while a > b:
    c = a % b
    if c != 0:
       a = c
       print(a)
       continue
    else:
        print('b is HOD',b)
        break
while a < b:
    d = b % a
    if d != 0:
        b = d
        print(b)
        continue
    else:
        print('a is HOD',a)
        break
