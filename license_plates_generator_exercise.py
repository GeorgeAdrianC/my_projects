import random
"""
In a particular jurisdiction, older license plates consist of three letters followed by
three numbers. When all of the license plates following that pattern had been used,
the format was changed to four numbers followed by three letters.
Write a function that generates a random license plate. Your function should have
approximately equal odds of generating a sequence of characters for an old license
plate or a new license plate. Write a main program that calls your function and
displays the randomly generated license plate.
"""

numbers = ['1','2','3','4','5','6','7','8','9','0']
letters = ["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

number_1 = random.choice(numbers)
number_2 = random.choice(numbers)
number_3 = random.choice(numbers)
number_4 = random.choice(numbers)

letter_1 = random.choice(letters)
letter_2 = random.choice(letters)
letter_3 = random.choice(letters)
letter_4 = random.choice(letters)


license_plate_new = number_1 + number_2 + number_3 + number_4 + letter_1 + letter_2 + letter_3 + letter_4
license_plate_old = number_2 + number_3 + number_4 + letter_1 + letter_2 + letter_3 + letter_4

chances = [license_plate_new, license_plate_old]
evan_chance = random.choice(chances)
evan_upper = evan_chance.upper()

print(f"Your new license plate is: {evan_upper} ")