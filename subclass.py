from class_example import Vehicle


class Car(Vehicle):
    # This is a new class

    def brake(self):
        # Override the break method
        return "The car class is breaking slowly!"


if __name__ == "__main__":
    car = Car("yellow", 2, 4, "car")

    print(car.brake())


