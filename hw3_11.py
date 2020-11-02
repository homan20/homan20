# Ввести 5 цифр, замінити кожну другу на 0
n = int(input('Enter 5 digit:'))

d1 = n // 10000 # 1st
d2 = (n // 1000) % 10 # 2st
d3 = (n // 100)%10 #3 st
d4 = (n //10)%10
d5 = n % 10
print( 'in',d1,d2,d3,d4,d5)
d2 = d4 = 0
print( 'out',d1,d2,d3,d4,d5)

s= 0
while n  :
    s += 1 
    n //= 10 # number of digits in the number
if s > 5:
    print('Digit > 5')
    if s < 5:
        print('Digit < 5') 