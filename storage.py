import json
from pathlib import Path

from data_layer import Car, Truck, Motorcycle, Garage
from data_layer import Vehicle

# Путь к файлу хранения данных
STORAGE_FILE = Path(__file__).with_name("storage.json")