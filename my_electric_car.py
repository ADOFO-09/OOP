from inheritance import Electric_Car, Battery

Tesla = Electric_Car("Tesla", "SY4", 2023)
print(Tesla.get_descriptive_name())

audi = Battery(90)
audi.describe_battery()
audi.get_range()  