class VehicleRepository:
    def __init__(self):
        self.vehicles = []
        self.next_id = 1

    def add_vehicle(self, vehicle):
        vehicle.id = self.next_id
        self.next_id += 1
        self.vehicles.append(vehicle)

    def get_all_vehicles(self):
        return self.vehicles

    def get_by_id(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.id == vehicle_id:
                return vehicle

        return None

    def remove_vehicle(self, vehicle_id):
        vehicle = self.get_by_id(vehicle_id)

        if vehicle is not None:
            self.vehicles.remove(vehicle)
            return True

        return False

    def update_vehicle(self, vehicle_id, brand, model, year):
        vehicle = self.get_by_id(vehicle_id)

        if vehicle is not None:
            vehicle.brand = brand
            vehicle.model = model
            vehicle.year = year
            return True

        return False
