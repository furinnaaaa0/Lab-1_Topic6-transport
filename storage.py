import json
from pathlib import Path

from data_layer import Car, Truck, Motorcycle, Garage
from data_layer import Vehicle

# Путь к файлу хранения данных
STORAGE_FILE = Path(__file__).with_name("storage.json")

# Преобразует транспортный объект в словарь
def vehicle_to_dict(vehicle):
    data = {
        "type": type(vehicle).__name__,
        "id": vehicle.id,
        "garage_id": vehicle.garage_id,
        "brand": vehicle.brand,
        "model": vehicle.model,
        "year": vehicle.year
    }

    if isinstance(vehicle, Car):
        data["passengers"] = vehicle.passengers

    elif isinstance(vehicle, Truck):
        data["cargo_weight"] = vehicle.cargo_weight

    elif isinstance(vehicle, Motorcycle):
        data["has_sidecar"] = vehicle.has_sidecar

    else:
        raise ValueError("Неизвестный тип транспорта")

    return data

# Преобразует гараж в словарь
def garage_to_dict(garage):
    return {
        "id": garage.id,
        "owner": garage.owner,
        "capacity": garage.capacity
    }

# Восстанавливает транспортный объект из словаря
def dict_to_vehicle(data):
    vehicle_type = data["type"]

    if vehicle_type == "Car":
        vehicle = Car(
            data["brand"],
            data["model"],
            data["year"],
            data["passengers"]
        )

    elif vehicle_type == "Truck":
        vehicle = Truck(
            data["brand"],
            data["model"],
            data["year"],
            data["cargo_weight"]
        )

    elif vehicle_type == "Motorcycle":
        vehicle = Motorcycle(
            data["brand"],
            data["model"],
            data["year"],
            data["has_sidecar"]
        )

    else:
        raise ValueError("Неизвестный тип транспорта в файле")

    vehicle.id = data["id"]
    vehicle.garage_id = data["garage_id"]

    return vehicle

# Восстанавливает гараж из словаря
def dict_to_garage(data):
    garage = Garage(
        data["owner"],
        data["capacity"]
    )

    garage.id = data["id"]

    return garage