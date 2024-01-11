# A class that can be used to represent a car.
class Car():
    # Simple attempt to model a car
    def __init__(self,make, model, year):
        # Initialize attributes
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # Return a neatly formatted descriptive name
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        # Print a statement showing a car's mileage
        print("This car has " + str(self.odometer_reading) + " miles on it")
    def update_odometer(self, mileage):
        # Adding a logic to the update_odometer
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
   

class Electric_Car(Car):
    def __init__(self,make,model,year,battery):
        super().__init__(make,model,year)
        self.battery = battery()
        

# my_new_car = Car('lamboghini', 'a4', 2023)
# print(my_new_car.get_descriptive_name())

# # Updating odometer reading
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()
# print('\n')
# my_used_car = Car('Subaru', 'outback', 2015)   
# print(my_used_car.get_descriptive_name()) 
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
