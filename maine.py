class MyClass:
    print("Класс MyClass определен!")


class Class2:
    print("Класс Class2 определен!")


class Garage:
    """Класс «Гараж»

    Этот класс ...

    """

    def __init__(self):
        self._cars = [1, 2, 3]

    def __len__(self):
        return len(self._cars)

    def __getitem__(self, position):
        return self._cars[position]

    print("Создаю объект класса Garage")


obj = MyClass()
garage = Garage()

print(garage, obj)

for car in garage:
    print(car)
