'''
The Factory Design Pattern is a creational pattern that provides an interface for creating objects but allows subclasses to alter the type of objects that will be created. 
It helps encapsulate object creation logic, making the code more maintainable, scalable, and flexible.

Why Use Factory Pattern?
    Encapsulation of Object Creation → The calling code does not need to know the concrete class.
    Loose Coupling → The code depends on an interface or base class rather than specific implementations.
    Scalability → Easy to add new classes without modifying existing code.

Factory Pattern in Python
    Step 1: Define an Abstract Class (or Base Class)
    This acts as a blueprint for different types of objects.

    Step 2: Implement Concrete Classes
    These are the actual implementations of the abstract class.

    Step 3: Implement a Factory Method
    The factory method creates and returns an instance of the required class.
'''

from abc import ABC, abstractmethod

# Step 1: Define an abstract class
class Vehicle(ABC):
    @abstractmethod
    def create(self):
        pass

# Step 2: Implement concrete classes
class Car(Vehicle):
    def create(self):
        return "Car Created"

class Bike(Vehicle):
    def create(self):
        return "Bike Created"

class Truck(Vehicle):
    def create(self):
        return "Truck Created"

# Step 3: Implement Factory Class
class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        # Reflection: Dynamically fetch the class from global scope
        vehicle_class = globals().get(vehicle_type.capitalize())  # "car" → "Car"
        if vehicle_class and issubclass(vehicle_class, Vehicle):
            return vehicle_class()  # Instantiate dynamically
        return None

# Step 4: Client Code
if __name__ == "__main__":
    vehicle_type = input("Enter vehicle type (car/bike/truck): ").strip().lower()
    vehicle = VehicleFactory.get_vehicle(vehicle_type)
    
    if vehicle:
        print(vehicle.create())
    else:
        print("Invalid vehicle type")
