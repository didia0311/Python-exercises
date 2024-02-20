num_of_nos = int(input("Enter a number of numbers: "))
count = 0
max = int(input("Enter a number: "))

while count < num_of_nos - 1:
     n = int(input("Enter a number: "))
     if n > max:
        max = n
     count = count + 1
print("The number is", max)