class Dishwasher:

    dishwasher_number = 0

    def __init__(self, name, water_outlay, program_number, dishes_set_number, price):
        self.name = name
        self.water_outlay = water_outlay
        self.program_number = program_number
        self.dishes_set_number = dishes_set_number
        self.price = price

        Dishwasher.dishwasher_number += 1

    @staticmethod
    def get_dishwasher_number():
        return Dishwasher.dishwasher_number

    def __del__(self):
        print("Dishwasher " + self.name + " was deleted")

    def __str__(self):
        return str(self.__dict__)
