import random
roll_dice = input("Please guess which side the dice will land on: ")

if roll_dice == "1" or "2" or "3" or "4" or "5" or "6":
    possible_results = [1, 2, 3, 4, 5, 6]
    result = random.choice(possible_results)
    if roll_dice ==  result:
        print("Wow you guessed correctly")
        print("The dice landed on: " + str(result))
    else:
        print("You guessed incorrectly, The dice landed on: " + str(result))
    