fxdnum = 13
print("\n\n\n------------------Python Game: Guessing the number-----------------------")
print("------------------------------------------------------------")
print("\nRules:\nYou have to guess the accurate number between 1-20")
print("You have only 9 guesses!\n")
print("------------------------------------------------------------")
guess = 10
i = 1
while(i < 10):
    print("------------------------------------------------------------")
    acunum = int(input("\nGuess the accurate number: "))
    if acunum > fxdnum:
        if acunum > 20:
            print(
                "You have entered the number which is greater than 20!\nSo you are disqualified!")
            print("------------------------------------------------------------")
            break
        print("\nDecrease the number!")
        print("Guesses left: ", guess-i-1, end="\n")
        print("------------------------------------------------------------")
    elif acunum < fxdnum:
        print("\nIncrease the number!")
        print("Guesses left: ", guess-i-1, end="\n")
        print("------------------------------------------------------------")
    elif acunum == fxdnum:
        print("\nCongo!")
        print("You got the number in ", i, " guesses!")
        print("------------------------------------------------------------")
        break

    i = i+1
    if i+1 == 11:
        print("\n\nOH BUDDY! You loose the game!")
        print("------------------------------------------------------------")
