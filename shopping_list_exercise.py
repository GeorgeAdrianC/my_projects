
import random
user_greetings_prompts = ["Hi!","Hello!","Greetings, traveler!"]
user_info_prompts = ["What's your age? ","How old are you? ","Please tell me your age. "]
user_shopping_list_prompts = ["What's on your shopping list? ","What would you like to buy? ","What can I get you? "]
user_farewell_prompts = ["Thank you for your purchase!","Thanks! Please come again.","Thank you!"]

def get_customer_name():    
    name = input(f"{random.choice(user_greetings_prompts)} \n Please enter your name here: ")
    return name 

def get_customer_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
            break
        except ValueError:
            print("Please enter a valid number")

    return age

def get_shopping_list(age):
    
    not_allowed = ("beer", "wine", "rum", "cigarettes")
    shopping_list = list()
    print("\nTo stop press 'ENTER'.\n")
    while True:
        print("Please enter your item here: ")
        groceries = input()
       
        if groceries == " " or groceries == "nothing" or groceries == "":
            break
        if age < 18:
            if groceries in not_allowed:
                print(f"You can't buy {groceries}, I will not add it to your list.")
                continue    
        shopping_list.append(groceries)
    return shopping_list
        

def main():
    name = get_customer_name()
    print(f"Hi {name}! \n Welcome to our store!")
    age = int(get_customer_age()) 
    shopping_list = get_shopping_list(age) 
       
    number_groceries = len(shopping_list)
    seconds = number_groceries * 30 
    
    if number_groceries <= 1:
        print("Please enter a shopping list!")

    else:            
        print(f"\nWe're really sorry {name}, but '{random.choice(shopping_list)}' is no longer available. \nYou will have to wait 30 seconds for every item in your list. \n Please wait for {seconds} seconds. \n Have a great day, {name}!")


if __name__ == "__main__":
    main()