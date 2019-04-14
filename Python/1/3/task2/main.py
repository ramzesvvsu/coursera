from builtins import float
from os.path import splitext
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.car_type = None

    def get_photo_file_ext(self):
        return splitext(self.photo_file_name)[1]

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except:
            self.passenger_seats_count = 0
        self.car_type = 'car'

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        if body_whl:
            body_whl_split = body_whl.split('x')
            self.body_length = float(body_whl_split[0])
            self.body_width = float(body_whl_split[1])
            self.body_height = float(body_whl_split[2])
        else:
            self.body_length = 0
            self.body_width = 0
            self.body_height = 0
        #self.body_whl = body_whl
        self.car_type = 'truck'

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'


def get_car_list(csv_filename):
    car_list = []


    with open(csv_filename) as csv_fd:
        reader = csv.DictReader(csv_fd, delimiter=';')
        #next(reader)  # пропускаем заголовок
        for row in reader:
            if row['car_type'] == 'car':
                new_object = Car(row['brand'], row['photo_file_name'], row['carrying'], row['body_whl'])
            elif row['car_type'] == 'truck':
                new_object = Truck(row['brand'], row['photo_file_name'], row['carrying'], row['body_whl'])
            elif row['car_type'] == 'spec_machine':
                new_object = SpecMachine(row['brand'], row['photo_file_name'], row['carrying'], row['extra'])
            else:
                continue
            car_list.append(new_object)


    return car_list

if __name__ == '__main__':
    get_car_list('coursera_week3_cars.csv')


class Pet:
    pass

class Cat(Pet):
    pass

print(isinstance(Cat(), Pet))


print(issubclass(Cat, Pet))


print(isinstance(Cat(), Cat))


print(issubclass(Cat, object))


print(issubclass(Pet, Cat))