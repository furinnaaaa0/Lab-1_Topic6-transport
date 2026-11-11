from repository_layer import VehicleRepository, GarageRepository
from service_layer import VehicleService, GarageService


# Выводит список транспортных средств
def print_vehicles(vehicles):
    if not vehicles:
        print("Транспорт не найден")
        return

    for vehicle in vehicles:
        print(vehicle.get_info())

# Выводит список гаражей
def print_garages(garages, garage_service):
    for garage in garages:
        occupied_places = garage_service.get_occupied_places(
            garage.id
        )

        print(
            f"ID: {garage.id} | Владелец: {garage.owner} | "
            f"Всего мест: {garage.capacity} | "
            f"Занято: {occupied_places}"
        )



# Основная функция программы
def main():
    repository = VehicleRepository()
    garage_repository = GarageRepository()
    service = VehicleService(repository, garage_repository)
    garage_service = GarageService(garage_repository,repository)

    # Основной цикл программы
    while True:
        print("\n--- Управление транспортом ---")
        print("1. Показать транспорт")
        print("2. Добавить автомобиль")
        print("3. Добавить грузовик")
        print("4. Добавить мотоцикл")
        print("5. Изменить транспорт")
        print("6. Удалить транспорт")
        print("7. Показать гаражи")
        print("8. Добавить гараж")
        print("9. Изменить гараж")
        print("10. Разместить транспорт в гараже")
        print("11. Убрать транспорт из гаража")
        print("12. Удалить гараж")
        print("0. Выход")

        choice = input("Выберите действие: ")

        # Обрабатывает ошибки при вводе чисел
        try:
            if choice == "1":
                print_vehicles(service.get_all_vehicles())

            elif choice == "2":
                brand = input("Марка: ")
                model = input("Модель: ")
                year = int(input("Год: "))
                passengers = int(input("Количество пассажиров: "))

                service.add_car(brand, model, year, passengers)
                print("Автомобиль добавлен")

            elif choice == "3":
                brand = input("Марка: ")
                model = input("Модель: ")
                year = int(input("Год: "))
                cargo_weight = float(input("Вес груза: "))

                service.add_truck(
                    brand, model, year, cargo_weight
                )
                print("Грузовик добавлен")

            elif choice == "4":
                brand = input("Марка: ")
                model = input("Модель: ")
                year = int(input("Год: "))

                answer = input("Есть коляска? (да/нет): ").lower()
                has_sidecar = answer == "да"

                service.add_motorcycle(
                    brand, model, year, has_sidecar
                )
                print("Мотоцикл добавлен")

            elif choice == "5":
                vehicle_id = int(input("ID транспорта: "))
                brand = input("Новая марка: ")
                model = input("Новая модель: ")
                year = int(input("Новый год: "))

                if service.update_vehicle(
                    vehicle_id, brand, model, year
                ):
                    print("Транспорт изменён")
                else:
                    print("Транспорт не найден")

            elif choice == "6":
                vehicle_id = int(input("ID транспорта: "))

                if service.remove_vehicle(vehicle_id):
                    print("Транспорт удалён")
                else:
                    print("Транспорт не найден")


            elif choice == "7":
                print_garages(garage_service.get_all_garages(),garage_service)

            elif choice == "8":
                owner = input("Владелец гаража: ")
                capacity = int(input("Вместимость гаража: "))

                garage = garage_service.add_garage(owner, capacity)
                print("Гараж добавлен")
                print(garage.get_info())

            elif choice == "9":
                garage_id = input("ID гаража: ")
                owner = input("Новый владелец: ")
                capacity = int(input("Новая вместимость: "))
                if capacity <= 0:
                    print("Вместимость должна быть больше нуля")
                else:
                    result = garage_service.update_garage(
                        garage_id, owner, capacity
                    )
                    print(result)


            elif choice == "10":
                vehicle_id = int(input("ID транспорта: "))
                garage_id = input("ID гаража: ")

                result = service.place_vehicle_in_garage(
                    vehicle_id, garage_id
                )
                print(result)

            elif choice == "11":
                vehicle_id = int(input("ID транспорта: "))
                result = service.remove_vehicle_from_garage(vehicle_id)
                print(result)

            elif choice == "12":
                garage_id = input("ID гаража: ")

                if garage_service.remove_garage(garage_id):
                    print("Гараж удалён")
                else:
                    print("Гараж не найден")

            elif choice == "0":
                print("Программа завершена")
                break

            else:
                print("Неверный пункт меню")

        except ValueError:
            print("Ошибка: введите корректное число")


# Запускает программу
if __name__ == "__main__":
    main()
