"""
Control the movements of a basic robot
"""
import math

def main():
    pass

if __name__ == '__main__':
    main()

# Challenge 11 - I Robot

#![](https://images.unsplash.com/photo-1472457897821-70d3819a0e24?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1349&q=80)
#Photo par [Daniel Cheung](https://unsplash.com/photos/cPF2nlWcMY4)

## Objectifs
#Contrôler les mouvements d'un robot basique

## Directives
#Le robot commence au point d'origine (0,0). Il peut se déplacer vers le HAUT, le BAS, la GAUCHE et la DROITE avec un nombre de pas donné.

#Écrire un programme pour calculer la distance de la position actuelle après une séquence de mouvements et le point d'origine. Si la distance est un flottant, alors imprimez simplement l'entier le plus proche.

#Le programme devrait fonctionner comme ceci :

'''
Initial position: (0, 0)
What's your next move?
>> up 5
New position : (0, 5)
What's your next move?
>> right 4
New position : (4, 5)
What's your next move?
>> down 11
New position : (4, -6)
What's your next move?
>> left 1
New position : (3, -6)
What's your next move?
>> quit
Distance from origin: 7


#Votre programme doit être écrit dans `i_robot.py`. Vous devrez peut-être utiliser une méthode du module `math`.
'''
from i_robot import Robot


def main():
    robot = Robot(0, 0)
    robot.start()
    print("Initial position: ", robot.position)
    while robot.moving:
        move = input("What's your next move? \n>> ")
        if move == "quit":
            robot.stop()
            # Si la distance est un flottant, 
            # alors imprimez simplement l'entier le plus proche.
            print(f"Distance from origin: {round(robot.distance)}")
            break
        action, pas = move.split()
        pas = int(pas)
        if action == "up":
            robot.up(pas)
        if action == "right":
            robot.right(pas)
        if action == "down":
            robot.down(pas)
        if action == "left":
            robot.left(pas)

    """
Initial position: (0, 0)
What's your next move?
>> up 5
New position : (0, 5)
What's your next move?
>> right 4
New position : (4, 5)
What's your next move?
>> down 11
New position : (4, -6)
What's your next move?
>> left 1
New position : (3, -6)
What's your next move?
>> quit
Distance from origin: 7
    """

if __name__ == '__main__':
    main()