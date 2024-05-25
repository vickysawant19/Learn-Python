class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def moves(self):
        print("moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")



mycar = Vehicle("tesla","M2")

print(mycar.make,mycar.model)
mycar.get_make_model()
mycar.moves()

your_car = Vehicle("cadilag","Escalate")

your_car.get_make_model()
your_car.moves()

class Airplane(Vehicle):
    def __init__(self, make, model,faa_id):
        super().__init__(make, model)
        self.faa_id : faa_id
    def moves(self):
        print('Files along....')

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")


class GolfCart(Vehicle):
    pass


cessna = Airplane('cessna','skyhaunk',"N-12323")
mack = Truck('mack','Pinacal')
golfVagan = GolfCart('Yamaha','gc100')

cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

golfVagan.get_make_model()
golfVagan.moves()

print("\n\n")

for v in (mycar,your_car,cessna,golfVagan,mack):
    v.get_make_model()
    v.moves()