print("------------zhuolingmin----------------- \n")
temp = input("Do you want input which number \n")
guess = int(temp)

for i in range(5):
    if guess == 8:
        print("you guessed right \n")
        break
    else:
        print("you guessed wrong \n")
    temp = input("you can guess aganst \n")
    guess = int(temp)


print("---------------finish the game--------------- \n")

