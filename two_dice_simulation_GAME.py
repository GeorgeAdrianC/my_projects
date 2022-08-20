import random

def random_dices():
    dice_1= [1,2,3,4,5,6]
    dice_2= [1,2,3,4,5,6]

    random_dice_1 = random.choice(dice_1)
    random_dice_2 = random.choice(dice_2)
    both_dices = f"{random_dice_1} and {random_dice_2}"
    return both_dices

def main():
    print("Welcome to the dice simulation")
    print("Rolling the dices...")
    print("The result is:", random_dices())
    print("Thank you for using the dice simulation")
    
if __name__ == "__main__":
    main()