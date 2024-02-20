mydate = input("Enter your date in DD-MM/yyyy:")

l = mydate.split('/')
print('day:',l[0])
print('month:', l[1])
print('year:', l[2])