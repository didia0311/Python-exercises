import random

n = random.randint(1, 10)
guess = 0
while guess != n:
    guess = int(input('Guess a nr'))
    if guess < n:
        print('Too low')
    elif guess > n:
        print('Too high')
    else:
        print('perfect')