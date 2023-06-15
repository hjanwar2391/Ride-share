from abs import ABC, abstractmethod
from datetime import datetime


class Ride_Sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders =[]
        self.drivers =[]
        self.rides = []

    
    def add_rider(self, rider):
        self.riders.append(rider)
    
    def add_driver(self, driver):
        self.drivers.append(driver)


class User(ABC):
    def __init__(self,name, email, nid) ->None:
        self.name= name
        self.email= email
        self.nid= nid
        self.wallet= 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, email, nid, current_location,initial_amount) -> None:
        self.cururent_ride=None
        self.wallet = initial_amount
        self.cururent_location = current_location
        super().__init__(name, email, nid)
    
    def display_profile(self):
        print(f"rider:with name: {self.name}")

    def load_cash(self, amount):
        if amount > 0:
            self.wallet+=amount

    def update_location(self,current_location)
        self.cururent_location = current_location

    def request_ride(self, destination,location = None):
        if not self.current_ride:

            ride_request = Ride_Request(self,destination)
            ride_matcher =  Ride_Matching()
            self.cururent_ride= ride_matcher(ride_request)

class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location=current_location
        self.wallet= 0
    
    def display_profile(self):
        print(f'driver name: {self.name} and email: {self.email}')
    
    def accept_ride(self, ride):
        ride.set_driver(self)


class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location= start_location
        self.end_location=end_location
        self.driver=None
        self.rider= None
        self.start_time= None
        self.end_time= None
        self.estimated_fare=None

    
    def set_driver(self, driver):
        self.driver=driver
    
    def start_ride(self):
        self.start_time= datetime.now()

    def end_ride(self, amount):
        self.end_time= datetime.now()
        self.rider.wallet-= self.estimated_fare
        self.driver.wallet += self.estimated_fare


class Ride_Request:
    def __init__(self, rider,end_location) -> None:
        self.rider = rider
        self.end_location = end_location

class Ride_Matching:
    def __int__(self) -> None
        self.available_drivers = []

    def find_driver(self, ride_request):
        if len(self.available_drivers)>0:
            # TODO: find the closest driver of the rider
            driver = self.available_drivers[0]
            ride= Ride(ride_request.rider.current_location, ride_request. end_location)
            driver.accept_ride(ride)
            return ride

class Vehicle(ABC):
    speed = {
        'car':50,
        'bike':60,
        'cng':15
    }

    def __init__(self, vehicle_type, license_plate, rate) => None:
        self.vehicle_type= vehicle_type
        self.license_plate=license_plate
        self.rate = rate
        self.status = 'available'

    @abstractmethod
    def start_drive(self):
        pass


class car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate):
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = 'unavalable'
    
class Bike(Vehicle):