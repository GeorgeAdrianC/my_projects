class Restaurant:
    """A restaurant with italian cousine."""

#__init__ method(constructor):
    def __init__(self, name: str, cuisine: str):
        """Attributes that describe the restaurant."""
        
        #attribute:
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0 

#methods:
    def describe_restaurant(self) -> str:
        """Return the name and specific of the restaurant."""
        name = f"{self.name}\n{self.cuisine}\n"       
        return name.title()

    def open_restaurant(self) ->str:
        """Return a greeting phrase."""
        its_opened = f"Welcome to {self.name.title()}!\nHere you will be served with the best {self.cuisine} in town!\n"
        return its_opened

    def restaurant(self) ->str:
        """Return the number of customers served."""
        served = f"So far were served {self.number_served} customers today\n      * * * * * * * * *\n"
        return served
    
    def set_number_served(self) -> None:
        """Let's us modify the number of customers served."""
        while True:
            try:
                served = int(input(f"How many customers were served today at {self.name.title()}?: "))
                self.number_served = served
                break
            except ValueError:
                print("Please enter an integer.")
    
    def increment_number_served(self):
        """Add clients to the number served."""
        
        while True:
            try:
                served = int(input("How many customers were served since last time?: "))
                self.number_served = served
                break
            except ValueError:
                print("Please enter an integer.")
        
        
        
        self.number_served = served + self.number_served
       
            

