class Vehicles():

    def __init__ (self, name, with_engine):
        self.name = name
        self.with_engine = with_engine
    def identify_myself (self):
        return "Hy I'm Parents of All Vehicles, My name is " + self.name + ", " + "My Engine Status is " + "'" + self.with_engine + "'"    
    

class Bikes(Vehicles):
    def __init__ (self, name, with_engine, wheel_count):
        super().__init__ (name, with_engine)
        self.wheel_count = wheel_count
    def identify_myself (self):
        return "Hy I,m Bike , My name is " + self.name + ", " + "My Engine Status is " + "'" + self.with_engine + "'" + "," + " I Have " + self.wheel_count + " Wheel(s)"

class Cars(Vehicles):
    def __init__ (self, name, with_engine, wheel_count, engine_type):
        super().__init__ (name, with_engine)
        self.wheel_count = wheel_count
        self.engine_type = engine_type
    def identify_myself (self):
        return "Hy I,m Car , My name is " + self.name + ", " + "My Engine Status is " + "'" + self.with_engine + "'" + "," + " I Have " + self.wheel_count + " Wheel(s)" + ", My Engine Type = " + self.engine_type

class Buses(Vehicles):
    def __init__ (name, with_engine, wheel_count, private_bus):
        super().__init__ (name, with_engine)
        self.wheel_count = wheel_count
        self.private_bus = private_bus
        return "Hy I,m Bus" + "[" + self.private_bus + "]" + " , " + "My name is" + self.name + ", " + "My Engine Status is " + "'" + self.with_engine + "'" + "," + " I Have " + self.wheel_count + " Wheel(s)"

parent = Vehicles('Gerobak', 'no engine')
sepeda_pedal = Bikes('Pedal Bikes', 'no engine', '2')
sepeda_motor = Bikes('Motor Bikes', 'with engine', '2')
mobil_sport = Cars('Sport Cars', 'with engine', '4', 'V9')
mobil_pickup = Cars ('Pickup Cars', 'with engine', '4', 'Solar')
# trans_Jakarta = Buses ('Trans Jakarta', 'with engine', '4', 'Public Bus')
bus_sekolah = Buses ('School Bus', 'with engine', '4', 'Private Bus')
print(parent.identify_myself())
print(sepeda_pedal.identify_myself())
print(sepeda_motor.identify_myself())
print(mobil_sport.identify_myself())
print(mobil_pickup.identify_myself())
# print(trans_Jakarta.identify_myself())
# print(bus_sekolah.identify_myself())