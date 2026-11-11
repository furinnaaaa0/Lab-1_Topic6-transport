from data_layer import Car, Truck, Motorcycle, Garage

# Класс для работы с транспортом
class VehicleService:
    def __init__(self, repository):
        self.repository = repository

    # Создаёт автомобиль и добавляет его в репозиторий
    def add_car(self, brand, model, year, passengers):
        car = Car(brand, model, year, passengers)
        return self.repository.add_vehicle(car)

    # Создаёт грузовик и добавляет его в репозиторий
    def add_truck(self, brand, model, year, cargo_weight):
        truck = Truck(brand, model, year, cargo_weight)
        return self.repository.add_vehicle(truck)

    # Создаёт мотоцикл и добавляет его в репозиторий
    def add_motorcycle(self, brand, model, year, has_sidecar):
        motorcycle = Motorcycle(brand, model, year, has_sidecar)
        return self.repository.add_vehicle(motorcycle)

    # Получает весь транспорт из репозитория
    def get_all_vehicles(self):
        return self.repository.get_all_vehicles()

    # Передаёт команду на изменение транспорта
    def update_vehicle(self, vehicle_id, brand, model, year):
        return self.repository.update_vehicle(
            vehicle_id, brand, model, year
        )

    # Передаёт команду на удаление транспорта
    def remove_vehicle(self, vehicle_id):
        return self.repository.remove_vehicle(vehicle_id)


# Класс для работы с гаражами
class GarageService:
    def __init__(self, repository):
        self.repository = repository

    # Создаёт гараж и добавляет его в репозиторий
    def add_garage(self, owner, capacity):
        garage = Garage(owner, capacity)
        return self.repository.add_garage(garage)

    # Получает список всех гаражей
    def get_all_garages(self):
        return self.repository.get_all_garages()

    # Передаёт команду на изменение гаража
    def update_garage(self, garage_id, owner, capacity):
        return self.repository.update_garage(
            garage_id, owner, capacity
        )

    # Передаёт команду на удаление гаража
    def remove_garage(self, garage_id):
        return self.repository.remove_garage(garage_id)
