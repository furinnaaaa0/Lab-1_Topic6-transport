from data_layer import Car, Truck, Motorcycle


class VehicleService:
    def __init__(self, repository):
        self.repository = repository

    def add_car(self, brand, model, year, passengers):
        car = Car(brand, model, year, passengers)
        return self.repository.add_vehicle(car)

    def add_truck(self, brand, model, year, cargo_weight):
        truck = Truck(brand, model, year, cargo_weight)
        return self.repository.add_vehicle(truck)

    def add_motorcycle(self, brand, model, year, has_sidecar):
        motorcycle = Motorcycle(brand, model, year, has_sidecar)
        return self.repository.add_vehicle(motorcycle)

    def get_all_vehicles(self):
        return self.repository.get_all_vehicles()

    def update_vehicle(self, vehicle_id, brand, model, year):
        return self.repository.update_vehicle(
            vehicle_id, brand, model, year
        )

    def remove_vehicle(self, vehicle_id):
        return self.repository.remove_vehicle(vehicle_id)
