s1 = input ("Enter a string: ")

rev = s1[::-1]
if s1 == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

---to make a palindrome
print(s1+rev)