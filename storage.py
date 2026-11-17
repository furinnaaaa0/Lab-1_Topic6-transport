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