import random

num = random.randint(1, 100)

while True:
    guess = int(input('please guess: '))
    if guess > num:
        print(" the number too big \n")
    elif guess < num:
        print('the number too small \n')
    else:
        print('congratulation !')
        print('game over !')
        exit()

    
