class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        long_name = self.make + ' ' + str(self.year) + ' ' + self.model
        return long_name
    
    def fill_gas_tank(self):
        print("This car needs a gas tank!")

class Battery():
    def __init__(self,battery_health = 70):
        # initialize the battery attributes
        self.battery_health = battery_health

    def describe_battery(self):
        print("The car's battery is " + str(self.battery_health) + " " + "kw/h")

    # Overriding fill_gas_tank method from parent class Car
    def fill_gas_tank(self):
        print("This car does not need a gas tank!")

    def get_range(self):
        # describes the range a car can go depending on its battery health
        if self.battery_health == 70:
            range = 240
        elif self.battery_health >= 70:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on full charge."
        print(message)
    

# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method 
# should check the battery size and set the capacity to 85 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and 
# then call get_range() a second time after upgrading the battery. You should 
# see an increase in the car’s range

    def upgrade_battery(self):
        if self.battery_health != 85:
            self.battery_health = 85

    

class Electric_Car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        # Using instance of a class as an attribute
        self.battery = Battery()

# my_tesla = Electric_Car("tesla", "mode S", 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_tesla.battery.fill_gas_tank()


# print("........................................................................")
# my_audi = Car("audi","model Y",2011)
# print(my_audi.get_descriptive_name())
# my_audi.fill_gas_tank()

my_ludi = Electric_Car("ludi", "model W", 2023)
print("Cars' range before upgrade")
my_ludi.battery.get_range()
my_ludi.battery.upgrade_battery()
print("Car's range after ugrade")
my_ludi.battery.get_range()
