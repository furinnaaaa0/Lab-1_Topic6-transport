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

# Сохраняет данные в JSON
def save_data(vehicle_repository, garage_repository):
    data = {
        "vehicles": [
            vehicle_to_dict(vehicle)
            for vehicle in vehicle_repository.vehicles
        ],

        "garages": [
            garage_to_dict(garage)
            for garage in garage_repository.garages
        ],

        "vehicle_next_id": vehicle_repository.next_id,
        "garage_next_id": garage_repository.next_id
    }

    temp_file = STORAGE_FILE.with_suffix(".json.tmp")

    with open(temp_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    temp_file.replace(STORAGE_FILE)

# Загружает данные из JSON
def load_data(vehicle_repository, garage_repository):
    if not STORAGE_FILE.exists():
        return False

    with open(STORAGE_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Сначала восстанавливаем данные отдельно
    vehicles = [
        dict_to_vehicle(item)
        for item in data["vehicles"]
    ]

    garages = [
        dict_to_garage(item)
        for item in data["garages"]
    ]

    vehicle_next_id = data["vehicle_next_id"]
    garage_next_id = data["garage_next_id"]

    # Заменяем содержимое репозиториев
    vehicle_repository.vehicles = vehicles
    vehicle_repository.next_id = vehicle_next_id

    garage_repository.garages = garages
    garage_repository.next_id = garage_next_id

    return True

# Удаляет сохранённые и текущие данные
def delete_data(vehicle_repository, garage_repository):
    file_exists = STORAGE_FILE.exists()

    # Очищаем транспорт
    vehicle_repository.vehicles.clear()
    vehicle_repository.next_id = 1

    # Очищаем гаражи
    garage_repository.garages.clear()
    garage_repository.next_id = 1

    # Удаляем JSON-файл, если он существует
    if file_exists:
        STORAGE_FILE.unlink()

    return file_exists