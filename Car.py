class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year

    def display_info(self):
        print(f'Марка: {self.brand}')
        print(f'Год выпуска: {self.year}')

class Car(Vehicle):
    def __init__(self,brand,year,color):
        super().__init__(brand,year)
        self.color=color

    def display_info(self):
        super().display_info()
        print(f'Цвет: {self.color}')

class Motorcycle(Vehicle):
    def __init__(self,brand,year,engine_capacity):
        super().__init__(brand,year)
        self.engine_capacity=engine_capacity

    def display_info(self):
        super().display_info()
        print(f'Объем двигателя: {self.engine_capacity}')

car=Car("Mers e 200", 2017,"Black")
motorcycle=Motorcycle("Yamasaki",2019,500)

car.display_info()
print()
motorcycle.display_info()