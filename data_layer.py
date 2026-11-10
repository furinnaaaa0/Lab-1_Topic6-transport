class Vehicle:
    def __init__(self, brand, model, year):
        self.id = None
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"ID: {self.id} | {self.brand} {self.model}, {self.year} год"


class Car(Vehicle):
    def __init__(self, brand, model, year, passengers):
        super().__init__(brand, model, year)
        self.passengers = passengers

    def get_info(self):
        return super().get_info() + f" | Пассажиров: {self.passengers}"


class Truck(Vehicle):
    def __init__(self, brand, model, year, cargo_weight):
        super().__init__(brand, model, year)
        self.cargo_weight = cargo_weight

    def get_info(self):
        return super().get_info() + f" | Вес груза: {self.cargo_weight} т"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        return super().get_info() + f" | Коляска: {self.has_sidecar}"
