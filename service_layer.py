from data_layer import Car, Truck, Motorcycle


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
