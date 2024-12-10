#Определение классов данных
class HardDrive:
    def __init__(self, id, model, capacity):
        self.id = id  # ID жесткого диска
        self.model = model  # Модель жесткого диска
        self.capacity = capacity  # Вместимость жесткого диска в ГБ

class Computer:
    def __init__(self, id, name):
        self.id = id  # ID компьютера
        self.name = name  # Название компьютера
        self.hard_drives = []  # Список жестких дисков, связанных с компьютером

    def add_hard_drive(self, hard_drive):
        self.hard_drives.append(hard_drive)  # Добавление жесткого диска к компьютеру


#Создание тестовых данных

# Создание жестких дисков
hd1 = HardDrive(1, "Seagate Barracuda", 1000)
hd2 = HardDrive(2, "Western Digital Blue", 2000)
hd3 = HardDrive(3, "Samsung 970 EVO", 500)

# Создание компьютеров
pc1 = Computer(1, "Gaming PC")
pc2 = Computer(2, "Office PC")

# Связывание жестких дисков с компьютерами
pc1.add_hard_drive(hd1)
pc1.add_hard_drive(hd2)
pc2.add_hard_drive(hd3)


#Запрос 1: Вывод списка всех компьютеров с жесткими дисками
def list_computers_with_hard_drives():
    computers = [pc1, pc2]
    print("Запрос 1: Вывод списка всех компьютеров с жесткими дисками")
    for pc in computers:
        print(f"Компьютер: {pc.name}")
        for hd in pc.hard_drives:
            print(f"  Жесткий диск: {hd.model}, Вместимость: {hd.capacity} ГБ")
    print("\n")

list_computers_with_hard_drives()


#Запрос 2: Вывод средней вместимости жестких дисков в каждом компьютере
def average_capacity_per_computer():
    computers = [pc1, pc2]
    avg_capacities = {}
    for pc in computers:
        if pc.hard_drives:
            total_capacity = sum(hd.capacity for hd in pc.hard_drives)
            avg_capacity = round(total_capacity / len(pc.hard_drives), 2)
            avg_capacities[pc.name] = avg_capacity
    sorted_avg_capacities = sorted(avg_capacities.items(), key=lambda x: x[1])
    print("Запрос 2: Вывод средней вместимости жестких дисков в каждом компьютере")
    for name, avg in sorted_avg_capacities:
        print(f"{name}: Средняя вместимость жестких дисков = {avg} ГБ")
    print("\n")

average_capacity_per_computer()


#Запрос 3: Вывод всех жестких дисков, у которых вместимость больше 1000 ГБ
def list_large_hard_drives():
    large_drives = [hd for pc in [pc1, pc2] for hd in pc.hard_drives if hd.capacity > 1000]
    for hd in large_drives:
        print("Запрос 3: Вывод всех жестких дисков, у которых вместимость больше 1000 ГБ")
        print(f"Жесткий диск: {hd.model}, Вместимость: {hd.capacity} ГБ")

list_large_hard_drives()
