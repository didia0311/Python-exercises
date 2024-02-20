n = int(input('Enter nr'))
rev = 0

while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r

    print('reverse is', rev)
    print(n)