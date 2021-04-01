import random
def roll_dice():
    roll=random.randint(1,6)
    return roll
print('Welcome to Dice Game')
option=0
while option != 4:
    option = input('Enter Your Choice \n 1. Roll Dice \n 2. Points Check \n 3. Select Dice \n 4.Exit')
    if option == '1':
        print("The dice gave :")
        result = roll_dice()
        print(result)
