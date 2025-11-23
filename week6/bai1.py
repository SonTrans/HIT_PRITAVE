
class Manufacturer:
    def __init__(a,identity, location):
        a.identity = identity
        a.location = location
    def describe(a):
        print(f"{a.location} + {a.identity}")
class Device(Manufacturer):
    def __init__(a,name, price,identity, location):
        a.name = name
        a.price = price
        super().__init__(identity,location)
    def describe(a):
        print(f"Name : {a.name} - Price : {a.price} Identity : {a.identity} - Location : {a.location}")
device1 = Device(name="mouse", price=2.5, identity=9725, location="Vietnam") 
device1.describe()
device2 = Device(name="monitor", price=12.5, identity=11, location="Germany") 
device2.describe()


