from vechicles import Container
from vechicles import PlasticContainer
from vechicles import MetalContainer
from vechicles import Vechicle
from vechicles import LandVechicle
from vechicles import AirVechicle

def main():
    vehicles = Vechicle(category="land")
    land= LandVechicle()
    air = AirVechicle()

    # for vehicle in vehicles:
    #     vehicle.display_info()
        
    print(vehicles())




if __name__ == "__main__":
    main()
