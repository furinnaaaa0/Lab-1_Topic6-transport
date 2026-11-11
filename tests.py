import unittest

from repository_layer import VehicleRepository, GarageRepository
from service_layer import VehicleService, GarageService


class TransportGarageTest(unittest.TestCase):

    # Создаёт чистые репозитории и сервисы перед каждым тестом
    def setUp(self):
        self.vehicle_repository = VehicleRepository()
        self.garage_repository = GarageRepository()

        self.vehicle_service = VehicleService(
            self.vehicle_repository,
            self.garage_repository
        )

        self.garage_service = GarageService(
            self.garage_repository,
            self.vehicle_repository
        )

    # Проверяет создание автомобиля
    def test_add_car(self):
        car = self.vehicle_service.add_car(
            "BMW", "2000", 1967, 4
        )

        self.assertEqual(car.brand, "BMW")
        self.assertEqual(car.model, "2000")
        self.assertEqual(car.year, 1967)
        self.assertEqual(len(self.vehicle_service.get_all_vehicles()), 1)

    # Проверяет изменение автомобиля
    def test_update_vehicle(self):
        car = self.vehicle_service.add_car(
            "BMW", "2000", 1967, 4
        )

        result = self.vehicle_service.update_vehicle(
            car.id, "BMW", "E34", 1989
        )

        self.assertTrue(result)
        self.assertEqual(car.brand, "BMW")
        self.assertEqual(car.model, "E34")
        self.assertEqual(car.year, 1989)

    # Проверяет создание гаража
    def test_add_garage(self):
        garage = self.garage_service.add_garage(
            "Иван", 1
        )

        self.assertEqual(garage.id, "G1")
        self.assertEqual(garage.owner, "Иван")
        self.assertEqual(garage.capacity, 1)

    # Проверяет заполнение гаража
    def test_garage_capacity(self):
        car1 = self.vehicle_service.add_car(
            "BMW", "2000", 1967, 4
        )

        car2 = self.vehicle_service.add_car(
            "Toyota", "Land Cruiser", 1989, 5
        )

        garage = self.garage_service.add_garage(
            "Иван", 1
        )

        # Размещаем первую машину
        result1 = self.vehicle_service.place_vehicle_in_garage(
            car1.id, garage.id
        )

        self.assertEqual(
            result1,
            "Транспорт размещён в гараже"
        )

        self.assertEqual(
            self.garage_service.get_occupied_places(garage.id),
            1
        )

        # Вторая машина не помещается
        result2 = self.vehicle_service.place_vehicle_in_garage(
            car2.id, garage.id
        )

        self.assertEqual(
            result2,
            "В гараже нет свободных мест"
        )

        self.assertIsNone(car2.garage_id)

    # Проверяет увеличение вместимости гаража
    def test_increase_garage_capacity(self):
        car1 = self.vehicle_service.add_car(
            "BMW", "2000", 1967, 4
        )

        car2 = self.vehicle_service.add_car(
            "BMW", "E34", 1989, 5
        )

        garage = self.garage_service.add_garage(
            "Иван", 1
        )

        self.vehicle_service.place_vehicle_in_garage(
            car1.id, garage.id
        )

        # Увеличиваем вместимость до двух мест
        result = self.garage_service.update_garage(
            garage.id, "Иван", 2
        )

        self.assertEqual(result, "Гараж изменён")
        self.assertEqual(garage.capacity, 2)

        # Теперь размещаем вторую машину
        result2 = self.vehicle_service.place_vehicle_in_garage(
            car2.id, garage.id
        )

        self.assertEqual(
            result2,
            "Транспорт размещён в гараже"
        )

        self.assertEqual(
            self.garage_service.get_occupied_places(garage.id),
            2
        )

    # Проверяет запрет уменьшения вместимости
    def test_cannot_reduce_garage_capacity(self):
        car1 = self.vehicle_service.add_car(
            "BMW", "2000", 1967, 4
        )
        car2 = self.vehicle_service.add_car(
            "Ford", "Mustang", 1989, 4
        )

        garage = self.garage_service.add_garage(
            "Иван", 2
        )

        self.vehicle_service.place_vehicle_in_garage(
            car1.id, garage.id
        )

        self.vehicle_service.place_vehicle_in_garage(
            car2.id, garage.id
        )

        # Пытаемся уменьшить вместимость до одного места
        result = self.garage_service.update_garage(
            garage.id, "Иван", 1
        )

        self.assertEqual(
            result,
            "Новая вместимость не может быть меньше количества занятых мест"
        )

        self.assertEqual(garage.capacity, 2)

        # Проверяет удаление гаража без удаления транспорта

    def test_remove_garage(self):
        car = self.vehicle_service.add_car(
            "BMW", "E34", 1989, 5
        )

        garage = self.garage_service.add_garage(
            "Иван", 1
        )

        self.vehicle_service.place_vehicle_in_garage(
            car.id, garage.id
        )

        # Удаляем гараж
        result = self.garage_service.remove_garage(
            garage.id
        )

        self.assertTrue(result)

        # Гараж действительно удалён
        self.assertIsNone(
            self.garage_repository.get_by_id(garage.id)
        )

        # Машина осталась, но освобождена из гаража
        self.assertIsNone(car.garage_id)

        self.assertIsNotNone(
            self.vehicle_repository.get_by_id(car.id)
        )

if __name__ == "__main__":
    unittest.main()

