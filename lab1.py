

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def get_all_vehicles(self):
        return self.vehicles

    def remove_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            return True
        return False

    def update_vehicle(self, vehicle, brand, model, year):
        if vehicle in self.vehicles:
            vehicle.brand = brand
            vehicle.model = model
            vehicle.year = year
            return True
        return False

