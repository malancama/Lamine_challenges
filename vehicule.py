class Vehicle:
    def __init__(self, year, brand, color, wheels, consumption, fuel):
        self.year = year
        self.brand = brand
        self.color = color
        self.wheels = wheels
        self.consumption = consumption
        self.fuel = fuel
        self.kilometers = 0
        self.speed = 0

    def start(self):
        print(f"{self.brand} démarré.")
        # Démarrez le chronomètre ici

    def stop(self):
        print(f"{self.brand} arrêté.")

    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} accélère à {self.speed} km/h.")

    def brake(self):
        self.speed -= 10
        print(f"{self.brand} freine à {self.speed} km/h.")

class Car(Vehicle):
    def __init__(self, year, brand, color, wheels, consumption, fuel, doors):
        super().__init__(year, brand, color, wheels, consumption, fuel)
        self.doors = doors

    def open_doors(self):
        print(f"Les portes de la {self.brand} sont ouvertes.")

class Motorbike(Vehicle):
    def __init__(self, year, brand, color, wheels, consumption, fuel, helmet):
        super().__init__(year, brand, color, wheels, consumption, fuel)
        self.helmet = helmet

    def wear_helmet(self):
        print(f"Enfilez votre casque pour conduire la {self.brand}.")

# Instanciation d'un véhicule
mon_vehicule = Vehicle(year=2022, brand="Toyota", color="Bleu", wheels=4, consumption=8.5, fuel="Essence")
# Instanciation d'une voiture
ma_voiture = Car(year=2020, brand="Honda", color="Rouge", wheels=4, consumption=7.0, fuel="Essence", doors=4)
# Instanciation d'une moto
ma_moto = Motorbike(year=2021, brand="Harley-Davidson", color="Noire", wheels=2, consumption=5.0, fuel="Essence", helmet=True)

#exemple d'utilisation de véhicule
mon_vehicule.start()
mon_vehicule.accelerate()
mon_vehicule.brake()
mon_vehicule.stop()

#exemple d'utilisation de car
ma_voiture.start()
ma_voiture.accelerate()
ma_voiture.brake()
ma_voiture.stop()

#exemple d'utilisation de Motorbike
ma_moto.start()
ma_moto.accelerate()
ma_moto.accelerate()
ma_moto.brake()
ma_moto.brake()
ma_moto.stop()