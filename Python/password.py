pass1 = input("Enter your password: ")
pass2 = input("confirm")

if pass1 = pass2:
    print('yes matching')
else:
    if pass1.casefold() == pass2.casefold():
        print('check cases and try again')
    else:
        print('not matching')