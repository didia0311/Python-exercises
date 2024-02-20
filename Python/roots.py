import math
a = int(input('A is'))
b = int(input('B is'))
c = int(input('C is'))
r1 = (-b +math.sqrt(b**2-4*a*c))/(2*a)
r2 = (-b -math.sqrt(b**2-4*a*c))/(2*a)
print('The solutions', r1,r2)