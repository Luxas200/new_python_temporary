from datetime import date
from math import ceil


class Driver:
    def __init__(self,
                 vacation: tuple [date, date],
                 license_cat: list[str],
                 wage_per_km: float
                 ):
        self.vacation = vacation
        self.license_cat = license_cat
        self.wage_per_km = wage_per_km

    def check_driver_availability(self):
        today = date.today()
        if self.vacation[0]<=today<=self.vacation[1]:
            return False
        return True

class Transport:
    def __init__(self,
                 total_km: int,
                 plate_number: str,
                 fuel_type: str,
                 insurance_exp: int,
                 tech_inspection_exp: int,
                 yearly_repair_exp: int,
                 tech_inspection_date: date(year=2025,month=11,day=10),
                 insurance_date: date(year=2025,month=6,day=20),
                 available_cat: str,
                 fuel_per_100_km: int,
                 fuel_price: float,
                 ):
        self.total_km = total_km
        self.plate_number = plate_number
        self.fuel_type = fuel_type
        self.insurance_exp = insurance_exp
        self.tech_inspection_exp = tech_inspection_exp
        self.yearly_repair_exp = yearly_repair_exp
        self.tech_inspection_date = tech_inspection_date
        self.insurance_date = insurance_date
        self.available_cat = available_cat
        self.fuel_per_100_km = fuel_per_100_km
        self.fuel_price = fuel_price

    def check_dates(self):
        today = date.today()
        if today >= self.insurance_date:
            return False
        elif today >= self.tech_inspection_date:
            return False
        return True

    def total_exp(self):
        exploitation_exp = self.insurance_exp + self.tech_inspection_exp + self.yearly_repair_exp
        fuel_exp = self.fuel_price * (self.total_km * self.fuel_per_100_km/100)
        total_exp = exploitation_exp + fuel_exp
        return total_exp

    def count_price_km(self):
        km_price = self.total_exp()/self.total_km
        return km_price

class Car(Transport):
    def __init__(self,
                 total_km: int,
                 plate_number: str,
                 fuel_type: str,
                 insurance_exp: int,
                 tech_inspection_exp: int,
                 yearly_repair_exp: int,
                 tech_inspection_date: date(year=2025, month=11, day=10),
                 insurance_date: date(year=2025, month=6, day=20),
                 available_cat: str,
                 fuel_per_100_km: int,
                 fuel_price: float,
                 ):
        super().__init__(total_km, plate_number, fuel_type, insurance_exp, tech_inspection_exp, yearly_repair_exp,
                         tech_inspection_date, insurance_date, available_cat, fuel_per_100_km, fuel_price)

class Bus(Transport):
    def __init__(self,
                 total_km: int,
                 plate_number: str,
                 fuel_type: str,
                 insurance_exp: int,
                 tech_inspection_exp: int,
                 yearly_repair_exp: int,
                 tech_inspection_date: date(year=2025, month=11, day=10),
                 insurance_date: date(year=2025, month=6, day=20),
                 available_cat: str,
                 fuel_per_100_km: int,
                 seats: int,
                 fuel_price: float,
                 ):
        super().__init__(total_km, plate_number, fuel_type, insurance_exp, tech_inspection_exp, yearly_repair_exp,
                         tech_inspection_date, insurance_date, available_cat, fuel_per_100_km, fuel_price)
        self.seats = seats

    def count_bus_quantity(self, seats: int, persons: int):
        result = ceil(persons/seats)
        return result

    def count_bus_trip_price(self, persons: int, trip_length: int, driver: Driver):
        bus_quantity = ceil(persons/self.seats)
        one_bus_trip_price = trip_length*self.count_price_km()+trip_length*driver.wage_per_km
        price = bus_quantity * one_bus_trip_price
        return price

class Truck(Transport):
    def __init__(self,
                 total_km: int,
                 plate_number: str,
                 fuel_type: str,
                 insurance_exp: int,
                 tech_inspection_exp: int,
                 yearly_repair_exp: int,
                 tech_inspection_date: date(year=2025, month=11, day=10),
                 insurance_date: date(year=2025, month=6, day=20),
                 available_cat: str,
                 fuel_per_100_km: int,
                 truck_load: int,
                 trailer_load: int,
                 is_hook: bool,
                 fuel_price: float,
                 legal_trailer_cat: str
                 ):
        super().__init__(total_km, plate_number, fuel_type, insurance_exp, tech_inspection_exp, yearly_repair_exp,
                         tech_inspection_date, insurance_date, available_cat, fuel_per_100_km,fuel_price)

        self.truck_load = truck_load
        self.trailer_load = trailer_load
        self.is_hook = is_hook
        self.legal_trailer_cat = legal_trailer_cat

    def check_driver_trailers_license(self, driver: Driver):
        return self.legal_trailer_cat in driver.license_cat

    def calculate_efficient_delivery(self, weight: int, ):
        trips_with_trailer = ceil(weight/(self.truck_load+self.trailer_load))
        trips_without_trailer = ceil(weight/self.truck_load)
        if trips_with_trailer == trips_without_trailer:
            print(f'Planned trips with trailer {trips_with_trailer} is the same as '
                  f'trips without trailer {trips_without_trailer}. You have to drive without trailer')
        else:
            print(f'More efficient is to drive with trailer. '
                  f'With trailer: {trips_with_trailer} trips < without trailer {trips_without_trailer} trips')

driver = Driver((date(year=2025, month=7, day=15), date(year=2025, month=7, day=30)),
                ['A', 'B', 'CE', 'D'],
                2
                )
car = Car(20000,
          'ABC123',
          'Petrol',
          200,
          20,
          1000,
          date(year=2025,month=2,day=20),
          date(year=2025,month=2,day=18),
          'B',
          8,
          1.49
          )
bus = Bus(80000,
          'DDA123',
          'Diesel',
          1000,
          200,
          5000,
          date(year=2025,month=10,day=15),
          date(year=2025,month=2,day=18),
          'D',
          20,
          50,
          1.59,
          )
truck = Truck(120000,
              'ZDA123',
              'Diesel',
              5000,
              200,
              10000,
              date(year=2026, month=9, day=8),
              date(year=2025, month=12, day=3),
              'C',
              30,
              12,
              5,
              True,
              1.59,
              'CE'
              )
#selfcheck for functions:
print(car.total_exp())
print(car.check_dates())
print(car.tech_inspection_date)
print(driver.check_driver_availability())
print(bus.count_bus_quantity(50,160))
print(bus.count_price_km())
print(bus.count_bus_trip_price(160,500,driver))
print(truck.check_driver_trailers_license(driver))
print(truck.calculate_efficient_delivery(37))

