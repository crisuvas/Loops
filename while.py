from random import randint

random_number = randint(1, 10)
guesses_left = 3

while guesses_left > 0:
    number = int(input("Which number do you think is it?\n"))
    if number == random_number:
        print("You win!!!")
        break
    else:
        print("You were wrong, try again\n\n")
        guesses_left -= 1
else:
    print("You have lost")
