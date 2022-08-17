class Laptop:
    """Laptop price"""
    #constructor:
    def __init__(self, name: str, model: str):
        """Attributes that describe the laptop"""
        #atribute:
        self._name = name
        self.model = model
        self.price = 3499  

    #methods:
    def laptop_name(self) -> str:
        """Returns the name of the laptop"""
        name = f"{self._name} - {self.model}"
        return name
    
    def get_price(self) -> int or float:
        """Prints the actual price of the laptop"""
        price = self.price
        print(f"Price: {price} $")
    
    def set_price(self) -> int or float:
        """Sets the new price of the product"""
        
        while True:
            try:
                price = float(input("Please enter the new price: "))
            except ValueError:
                print("The price attribute must be an int or float type.")
            if price>0:
                break
            else:
                raise ValueError(
                    "The price attribute must be a positive int or float value."
                    )       

        self.price = price
        print(f"The new price is: {self.price}")

