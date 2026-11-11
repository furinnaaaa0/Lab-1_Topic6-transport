from repository_layer import VehicleRepository
from service_layer import VehicleService


# Выводит список транспортных средств
def print_vehicles(vehicles):
    if not vehicles:
        print("Транспорт не найден")
        return

    for vehicle in vehicles:
        print(vehicle.get_info())


# Основная функция программы
def main():
    repository = VehicleRepository()
    service = VehicleService(repository)

    # Основной цикл программы
    while True:
        print("\n--- Управление транспортом ---")
        print("1. Показать транспорт")
        print("2. Добавить автомобиль")
        print("3. Добавить грузовик")
        print("4. Добавить мотоцикл")
        print("5. Изменить транспорт")
        print("6. Удалить транспорт")
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
