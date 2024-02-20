n = int(input("Enter a nr"))
fact = 1

for count in range(1, n+1):
    fact = fact * count
    print ('Factorial of', n, 'is', fact)