import random


def roll_dice(side):
    if side == 1:
        sample_space = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6]  # biased samples
        print("\nUsing Red Dice\n")
        roll = random.choice(sample_space)
    elif side == 2:
        sample_space2 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6]
        print("\nUsing Blue Dice\n")
        roll = random.choice(sample_space2)
    else:
        print("\nUsing Black Dice\n")
        roll = random.randint(1, 6)
    return roll


print('Welcome to Dice Game')
point = 0
option = 0
dice = 1
while option != 4:
    option = int(input('Enter Your Choice \n 1. Roll Dice \n 2. Points Check \n 3. Select Dice \n 4.Exit\n'))
    if option == 1:  # dice roll
        print("The dice gave :")
        result = roll_dice(dice)
        print(result)
        if result == 6:  # Point is incremented
            point = point + 1

    elif option == 2:  # point count
        print('Your point is', point)

    elif option == 3:
        print("Choose Your Dice\n")
        dice_opt = int(input(
            '1.Red Dice-Lesser Chance of Scoring 6 \n 2.Blue Dice- A bit more chance of scoring 6 (10 points) \n 3.Black '
            'Dice-Unbiased Dice (20 points)\n'))
        if dice_opt == 1:
            print("\nRed Dice Selected")
        elif dice_opt == 2 & point >= 10:
            dice = 2
            print('\n Blue Dice Selected')
        elif dice_opt == 2 & point < 10:
            print("\nYou don't have enough points")
        elif dice_opt == 3 & point >= 20:
            dice = 3
            print('\n Black Dice selected')
        elif dice_opt == 3 & point < 20:
            print("\nYou don't have enough points")
        else:
            print('\nEnter correct option\n')


    elif option == 4:
        print("Goodbye")
    else:
        print("Enter Correct Option")

