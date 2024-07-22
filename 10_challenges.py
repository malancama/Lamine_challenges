"""
Height requirements ckecking in a theme park.
"""

def main():
    # TODO: Demandez la taille de l'utilisateur en centimètres et stockez le résultat dans une variable : height
    height=int(input('veiller entrer votre taille: '))

    # TODO : afficher "Désolé, vous êtes trop petit pour ce manège. Essayez un autre carrousel."
    # si la taille est inférieure à 100 (exclus)
    if height < 100:
        print('Désolé, vous êtes trop petit pour ce manège.')

    # TODO : afficher "Profitez de votre tour !" si la taille est supérieure ou égale à 100 et inférieure ou égale à 150
    elif 150 >=height >=100:
        print('Profiter de votre tour !')

    # TODO : afficher "Désolé, vous êtes trop grand pour celui-ci !" si la taille est supérieure à 150 (exclus)

    else:
        print('Désolé, vous êtes trop grand pour celui-ci !')

if __name__ == '__main__':
    main()

# Challenge 10 - Carrousel

#![](https://images.unsplash.com/photo-1471893110745-5c1b1f2dff57?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)
#Photo par [Tim Gouw](https://unsplash.com/photos/eaO9vgYkTOQ)

## Objectifs
#Vérification des exigences de taille dans un parc à thème.

## Directives
#Ouvrez `carrousel_ride.py` avec votre éditeur de texte et suivez les instructions.
