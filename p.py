from collections import namedtuple
import random


Car = namedtuple("Car", ["color", "brand"])

garage = [Car(color="brown", brand="Porsche"), Car(color="black", brand="BMW"), Car(color="silver", brand="Mercedes")]

for car in garage:
    print(*car)
    print(car.brand)

print(len(garage))
print(garage[0:1])
print("Сегодня поедем на:", random.choice(garage))  # Выбор случайного автомобиля
