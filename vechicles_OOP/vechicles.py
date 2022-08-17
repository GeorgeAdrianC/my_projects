class Container:    
    def __init__(self, name:str):
        self.name = name
    


class PlasticContainer(Container):
    def __init__(self, name: str):
        super().__init__(name)



class MetalContainer(Container):
    def __init__(self, name: str):
        super().__init__(name)

class Vechicle:
    def __init__(self, category=None):
        self.catergory = category
    
    def display_info(self) ->str:
        category = f"{self.catergory}"
        return category.title()
        
            
class LandVechicle(Vechicle):
    def __init__(self, category=None):
        super().__init__(category)
        
class AirVechicle(Vechicle):
    def __init__(self, category=None):
        super().__init__(category)



    # def __init__(self, category=None):
    #     self.catergory = category
    
    # def display_info():
    #     category = f"air vechicle"
    #     return category.title()