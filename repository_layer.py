# Класс для хранения и управления транспортными средствами
class VehicleRepository:
    def __init__(self):
        self.vehicles = []
        self.next_id = 1

    # Добавляет транспорт в список и присваивает ему ID
    def add_vehicle(self, vehicle):
        vehicle.id = self.next_id
        self.next_id += 1
        self.vehicles.append(vehicle)
        return vehicle

    # Возвращает весь список транспорта
    def get_all_vehicles(self):
        return self.vehicles

    # Ищет транспорт по его ID
    def get_by_id(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.id == vehicle_id:
                return vehicle

        return None

        # Возвращает транспорт, размещённый в указанном гараже
    def get_vehicles_in_garage(self, garage_id):
         return [
            vehicle for vehicle in self.vehicles
            if vehicle.garage_id == garage_id
            ]

        # Размещает транспорт в гараже
    def set_vehicle_garage(self, vehicle_id, garage_id):
        vehicle = self.get_by_id(vehicle_id)

        if vehicle is not None:
            vehicle.garage_id = garage_id
            return True

        return False

    # Убирает транспорт из гаража
    def remove_vehicle_from_garage(self, vehicle_id):
        vehicle = self.get_by_id(vehicle_id)

        if vehicle is not None:
            vehicle.garage_id = None
            return True

        return False

    # Освобождает весь транспорт из указанного гаража
    def remove_vehicles_from_garage(self, garage_id):
        for vehicle in self.vehicles:
            if vehicle.garage_id == garage_id:
                vehicle.garage_id = None

    # Удаляет транспорт по ID
    def remove_vehicle(self, vehicle_id):
        vehicle = self.get_by_id(vehicle_id)

        if vehicle is not None:
            self.vehicles.remove(vehicle)
            return True

        return False

    # Изменяет основные данные найденного транспорта
    def update_vehicle(self, vehicle_id, brand, model, year):
        vehicle = self.get_by_id(vehicle_id)

        if vehicle is not None:
            vehicle.brand = brand
            vehicle.model = model
            vehicle.year = year
            return True

        return False

# Класс для хранения и управления гаражами
class GarageRepository:
    def __init__(self):
        self.garages = []
        self.next_id = 1

    # Добавляет гараж и присваивает ему ID
    def add_garage(self, garage):
        garage.id = f"G{self.next_id}"
        self.next_id += 1
        self.garages.append(garage)
        return garage

    # Возвращает список всех гаражей
    def get_all_garages(self):
        return self.garages

    # Ищет гараж по его ID
    def get_by_id(self, garage_id):
        for garage in self.garages:
            if garage.id == garage_id:
                return garage

        return None

# Изменяет данные гаража
    def update_garage(self, garage_id, owner, capacity):
        garage = self.get_by_id(garage_id)

        if garage is not None:
            garage.owner = owner
            garage.capacity = capacity
            return True

        return False

    # Удаляет гараж по ID
    def remove_garage(self, garage_id):
        garage = self.get_by_id(garage_id)

        if garage is not None:
            self.garages.remove(garage)
            return True

        return False
