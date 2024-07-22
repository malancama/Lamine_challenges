## Challenge 13 - Véhicules

#![](https://images.unsplash.com/photo-1521706887145-1c0edacadb25?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1268&q=80)
#Photo par [chuttersnap](https://unsplash.com/photos/d271d_SOGR8)

## Objectifs
#Héritage et propriétés

## Directives
#1. Écrire une classe `Vehicle` :
#- Un véhicule est défini par les attributs `year`, `brand`, `color`, `wheels`, `consumption`, `fuel`, `kilometers`. Il a aussi `speed` qui est toujours zéro lorsque le véhicule est instancié.
#- Écrire des méthodes pour `start`, `stop`, `accelerate` et `brake` avec un incrément ou un décrément de la vitesse de 10 à chaque fois que la méthode est appelée.



        
#2. Démarrer un chronomètre lorsque le véhicule `start` et arrêter le chronomètre lorsque le véhicule `stop`. Pendant ce temps, mettre à jour les `kilometers` et le `fuel` en fonction de la conduite (`speed`, `accelerate` et `stop`).

#3. Écrire deux nouvelles classes `Car` et `Motorbikes`. Imaginer ce qui pourrait changer dans les attributs et les méthodes.

#4. Revoir l'accès au contrôle dans toutes les classes précédentes.

#Votre programme doit être écrit dans `vehicle.py`. Vous devez pouvoir instancier des cercles et jouer avec eux directement depuis votre console iPython.
class Vehicle:
    def __init__(self, year, brand, color, wheels, consumption, fuel, kilometers):
        self.year = year
        self.brand = brand
        self.color = color
        self.wheels = wheels
        self.consumption = consumption
        self.fuel = fuel
        self.kilometers = kilometers
        self.speed = 0

    def start(self):
        print(f"{self.brand} started!")

    def stop(self):
        print(f"{self.brand} stopped!")

    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} accelerated to {self.speed} km/h")

    def brake(self):
        self.speed -= 10
        print(f"{self.brand} slowed down to {self.speed} km/h")

# Exemple d'utilisation
# my_car = Vehicle(year=2022, brand="Tesla", color="Blue", wheels=4, consumption=15, fuel="Electric", kilometers=5000)
# my_car.start()
# my_car.accelerate()
# my_car.brake()
# my_car.stop()
