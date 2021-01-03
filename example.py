import random

num = random.randint(1, 100)

for i in range(1,6):
    guess = int(input('please guess: '))
    if guess > num:
        print(" the number too big \n")
    elif guess < num:
        print('the number too small \n')
    else:
        print('congratulation !')
        exit()
else:
    print('game over !')
    
