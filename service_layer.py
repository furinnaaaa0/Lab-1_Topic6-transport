from data_layer import Car, Truck, Motorcycle, Garage

# Класс для работы с транспортом
class VehicleService:
    def __init__(self, repository, garage_repository):
        self.repository = repository
        self.garage_repository = garage_repository

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
    # Размещает транспорт в гараже
    def place_vehicle_in_garage(self, vehicle_id, garage_id):
        vehicle = self.repository.get_by_id(vehicle_id)
        garage = self.garage_repository.get_by_id(garage_id)

        if vehicle is None:
            return "Транспорт не найден"

        if garage is None:
            return "Гараж не найден"

        if vehicle.garage_id is not None:
            return "Транспорт уже находится в гараже"

        vehicles_in_garage = self.repository.get_vehicles_in_garage(
            garage_id
        )

        if len(vehicles_in_garage) >= garage.capacity:
            return "В гараже нет свободных мест"

        self.repository.set_vehicle_garage(vehicle_id, garage_id)
        return "Транспорт размещён в гараже"

     # Убирает транспорт из гаража
    def remove_vehicle_from_garage(self, vehicle_id):
        vehicle = self.repository.get_by_id(vehicle_id)

        if vehicle is None:
            return "Транспорт не найден"

        if vehicle.garage_id is None:
            return "Транспорт не находится в гараже"

        self.repository.remove_vehicle_from_garage(vehicle_id)
        return "Транспорт убран из гаража"




# Класс для работы с гаражами
class GarageService:
    def __init__(self, repository, vehicle_repository):
        self.repository = repository
        self.vehicle_repository = vehicle_repository

    # Создаёт гараж и добавляет его в репозиторий
    def add_garage(self, owner, capacity):
        garage = Garage(owner, capacity)
        return self.repository.add_garage(garage)

    # Получает список всех гаражей
    def get_all_garages(self):
        return self.repository.get_all_garages()

    # Возвращает количество занятых мест в гараже
    def get_occupied_places(self, garage_id):
        vehicles = self.vehicle_repository.get_vehicles_in_garage(
            garage_id
        )
        return len(vehicles)

    # Передаёт команду на изменение гаража
    def update_garage(self, garage_id, owner, capacity):
        garage = self.repository.get_by_id(garage_id)
        if garage is None:
            return "Гараж не найден"
        occupied_places = len(self.vehicle_repository.get_vehicles_in_garage(garage_id))

        if capacity < occupied_places:
            return (
                "Новая вместимость не может быть меньше количества занятых мест"
            )

        self.repository.update_garage(garage_id, owner, capacity)
        return "Гараж изменён"

    # Удаляет гараж и освобождает находящийся в нём транспорт
    def remove_garage(self, garage_id):
        garage = self.repository.get_by_id(garage_id)

        if garage is None:
            return False

        self.vehicle_repository.remove_vehicles_from_garage(
            garage_id
        )

        return self.repository.remove_garage(garage_id)