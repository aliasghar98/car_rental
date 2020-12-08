from .car import Car
from ..models import CAR

class CarList:
    def __init__(self):
        pass

    def add_car(self,reg_no,make,model,body_type,engine_capacity,seats,color,transmission,fuel):
        try:
            new_car = CAR(
                reg_no=reg_no,make=make,model=model,
                body_type=body_type,engine_capacity=engine_capacity,
                seats=seats,color=color,transmission=transmission,fuel=fuel
            )
            new_car.save()
        except:
            raise Exception("Invalid Car")
