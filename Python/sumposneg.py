num_of_nos = int(input('Enter a number: '))
Psum = 0
Nsum = 0
count = 0

while count < num_of_nos:
    n = int(input('Enter'))
if n > 0:
    Psum = Psum + n
else:
    Nsum = Nsum + n
    count = count + 1
print('Psum is', Psum)
print('Nsum is', Nsum)