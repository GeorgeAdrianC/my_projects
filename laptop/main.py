from laptop import Laptop

"""An OOP program with different types of cuisine that gest input for number of customer served"""

def main():
    hp_laptop = Laptop(
        name = "HP",
        model = "PRO 21"
    )

    print(hp_laptop.laptop_name())
    hp_laptop.get_price()
    hp_laptop.set_price()





if __name__ == "__main__":
    main()