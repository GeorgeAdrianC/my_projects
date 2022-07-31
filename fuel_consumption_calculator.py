"""A simple program that calculates how much a trip will cost."""

def get_fuel_input():
    
    while True:
        try:
            fuel = float(input("Hello there!\nWhat is your average 100 km per liter fuel consumption? "))
            break
        except ValueError:
            print("Please enter a valid value.")
    return fuel
          
def get_km_input():
    
    while True:
        try:    
            km = float(input("How many km will you travel? "))
            break
        except ValueError:
            print("Please enter a valid value.")
    return km

def get_price_input():

    while True:
        try:
            price = float(input("What is the current price of gas in lei? "))
            break
        except ValueError:
            print("Please enter a valid value.")
    return price


def main():
      
    fuel = get_fuel_input()
    km = get_km_input()
    price = get_price_input()
    consumed_fuel = km * (fuel /100)
    money_value = consumed_fuel * price
    two_digit_money = format(money_value,".2f")
    last = (f"For this trip you will need {consumed_fuel} liters of gas that will cost {two_digit_money} lei. \nHave a safe trip!")
    print(last)


if __name__ == "__main__":
    main()






    