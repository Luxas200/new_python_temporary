class Driver:
    def __init__(self, vacation: str, license_cat: list, wage_per_km: int):
        self.vacation = vacation
        self.license_cat = license_cat
        self.wage_per_km = wage_per_km


class Transport:
    def __init__(self, total_km: int, plate_number: str, fuel_type: str, insurance_exp: int,
                 tech_inspection_exp: int, yearly_repair_exp: int, tech_inspection_date: str,
                 insurance_date: str, available_cat: str, fuel_per_100_km: int, fuel_price: int):

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


    def check_dates(self, insurance_date, tech_inspection_date):
        import datetime
        today = datetime.date.today()
        current_month = today.month
        print(current_month)
        if current_month == insurance_date or tech_inspection_date:
            return insurance_date and tech_inspection_date
        return False

    def total_exp(self, fuel_price: int, total_km: int, insurance_exp: int,
                  tech_inspection_exp: int, yearly_repair_exp: int, fuel_per_100_km: int):
        exploitation_exp = insurance_exp + tech_inspection_exp + yearly_repair_exp
        fuel_exp = fuel_price * (total_km * fuel_per_100_km/100)
        total_exp = exploitation_exp + fuel_exp
        return total_exp

    def check_driver_availability(self, vacation: str):
        import datetime
        today = datetime.date.today()
        if today == vacation:
            return False
        return True


class Car(Transport):
    def __init__(self, total_km: int, plate_number: str, fuel_type: str, insurance_exp: int, tech_inspection_exp: int,
                 yearly_repair_exp: int, tech_inspection_date: str, insurance_date: str, available_cat: str,
                 fuel_per_100_km: int, fuel_price):
        super().__init__(total_km, plate_number, fuel_type, insurance_exp, tech_inspection_exp, yearly_repair_exp,
                         tech_inspection_date, insurance_date, available_cat, fuel_per_100_km, fuel_price)


class Bus(Transport):
    def __init__(self, total_km: int, plate_number: str, fuel_type: str, insurance_exp: int, tech_inspection_exp: int,
                 yearly_repair_exp: int, tech_inspection_date: str, insurance_date: str, available_cat: str,
                 fuel_per_100_km: int, seats: int, persons: int, trip_length: int, fuel_price):
        super().__init__(total_km, plate_number, fuel_type, insurance_exp, tech_inspection_exp, yearly_repair_exp,
                         tech_inspection_date, insurance_date, available_cat, fuel_per_100_km, fuel_price)
        self.seats = seats
        self.persons = persons
        self.trip_length = trip_length



    def count_bus_quantity(self, seats: int, persons: int):
        result = round((seats / persons),0)
        return result

    def count_bus_estimate_price(self):
        bus_quantity = self.count_bus_quantity(self.seats, self.persons)
        price = bus_quantity * self.total_exp(self.fuel_price, self.trip_length, self.insurance_exp,
                                            self.tech_inspection_exp, self.yearly_repair_exp, self.fuel_per_100_km)
        return price


class Truck(Transport):
    def __init__(self, total_km: int, plate_number: str, fuel_type: str, insurance_exp: int, tech_inspection_exp: int,
                 yearly_repair_exp: int, tech_inspection_date: str, insurance_date: str, available_cat: str,
                 fuel_per_100_km: int, truck_load: int, trailer_load: int, is_hook: bool, fuel_price):
        super().__init__(total_km, plate_number, fuel_type, insurance_exp, tech_inspection_exp, yearly_repair_exp,
                         tech_inspection_date, insurance_date, available_cat, fuel_per_100_km, fuel_price)
        self.truck_load = truck_load
        self.trailer_load = trailer_load
        self.is_hook = is_hook

    def check_driver_trailers_license(self, license_cat: list):
        legal_trailer_cat = 'CE'
        for category in license_cat:
            if legal_trailer_cat == category:
                return True
            return False


driver = Driver('2025 06 30', ['A', 'B', 'CE', 'D'], 2)
car = Car(1000, 'ABC123', 'Petrol', 200, 200,
          1000, '2025 07 30', '2025 02 18', 'B', 8,
          1)
bus = Bus(1000, 'ABC123', 'Petrol', 200, 200,
          1000, '2025 07 30', '2025 02 18', 'B', 8,
          50, 30, 1000, 1)
truck = Truck(1000, 'ABC123', 'Petrol', 200, 200,
          1000, '2025 07 30', '2025 02 18', 'B', 8,
              12, 12, True, 1)


