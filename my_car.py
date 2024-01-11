import car
import inheritance

my_new_car1 = car.Car('Elantra', 'GT4', 2023)
print(my_new_car1.get_descriptive_name())

bmw = inheritance.Battery(100)
bmw.describe_battery()

tesla = inheritance.Electric_Car("Tesla", "Model Y", 2021)
tesla.battery.fill_gas_tank()