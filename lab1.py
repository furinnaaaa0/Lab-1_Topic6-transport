class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_info(self):
        print(f"{self.brand} {self.model}, {self.year} год")

class Car(Vehicle):
    def __init__(self, brand, model, year, passengers):
        super().__init__(brand, model, year)
        self.passengers = passengers

    def show_info(self):
        super().show_info()
        print(f"Количество пассажиров: {self.passengers}")

class Truck(Vehicle):
    def __init__(self, brand, model, year, cargo_weight):
        super().__init__(brand, model, year)
        self.cargo_weight = cargo_weight

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar
