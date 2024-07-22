## 💻 Challenges 09

### Niveau 1

#1. Déclarez une fonction _add_two_numbers_. Elle prend deux paramètres et renvoie une somme.
def add_two_numbers(a, b):
    somme=print(a + b)
    return somme

add_two_numbers(2, 5)

#2. L'aire d'un cercle se calcule comme suit : area = π x r x r. Écrivez une fonction qui calcule _area_of_circle_.
def area_of_circle(pi, r):
    area= pi * r * r
    return area
print(f'l\'air du cercle est de : {area_of_circle(3.14, 3):.2f}')


#3. Écrivez une fonction appelée add_all_nums qui prend un nombre arbitraire d'arguments et les additionne. Vérifiez si tous les éléments de la liste sont de type nombre. Sinon, donnez un retour d'information raisonnable.
def add_all_nums(*args):
    somme = 0
    for nb in args:
        if not isinstance(nb, (int, float)):
            return f"cette valeur '{nb}' n'est pas un nombre"
        else:
            somme += nb
    return somme
somme_correcte = add_all_nums(8, 9, 12, 66)
print(somme_correcte)

#4. La température en °C peut être convertie en °F en utilisant cette formule : °F = (°C x 9/5) + 32. Écrivez une fonction qui convertit °C en °F, _convert_celsius_to_fahrenheit_.
def onvert_celsius_to_fahrenheit(C):
    F=(C * 9/5) + 32
    return F
print(onvert_celsius_to_fahrenheit(12))

#5. Écrivez une fonction appelée check-season, elle prend un paramètre de mois et renvoie la saison : Automne, Hiver, Printemps ou Été.
def check_season(mois):
    saison = {'Automne':['janvier','fevrier', 'mars'],
              'Hiver':['avril','mai','juin'],
              'Printemps':['juillet','aout','septembre'],
              'ete':['novembre','décembre','octobre']
              }
    
    modif_month=mois.lower()
    for k, v in saison.items():
        if modif_month in v:
            return k
    print("la valeur n'exite pas")
mois=input('veiller saisir la valeur du mois: ')
saison= check_season(mois)
if saison:
    print(saison)

#6. Écrivez une fonction appelée calculate_slope qui renvoie la pente d'une équation linéaire.
def calculate_slope(x1, y1, x2, y2):
    # Calcul de la différence en y et en x
    y = y2 - y1
    x = x2 - x1
    
    # Calcul de la pente
    pente = y / x
    return pente
# Exemple d'utilisation
x1, y1 = 2, 2
x2, y2 = 4, 7
slope_result = calculate_slope(x1, y1, x2, y2)
print(f"La pente est : {slope_result}")

#7. Une équation quadratique se calcule comme suit : ax² + bx + c = 0. Écrivez une fonction qui calcule l'ensemble des solutions d'une équation quadratique, _solve_quadratic_eqn_.
#for exemple 
from math import sqrt
def solve_quadratic_eqn(a,b,c):
    delta=b**2 -4*a*c
    if delta > 0:
        x1 =(-b+sqrt(delta))/2*a
        x2 =(-b-sqrt(delta))/2*a
        print(f'X1 = {x1:.2f}\nX2={x2:.2f}')
    if delta <0:
        print('pas de solution')
    else:
        x2=-b/2*a
        x1=-b/2*a
        print(f'X1=X2 = {x1:.2f}')
    return 
solve_quadratic_eqn(1, 4, 4)

#8. Déclarez une fonction nommée print_list. Elle prend une liste comme paramètre et affiche chaque élément de la liste.
def print_list(liste=['lion','chat','souris','arbre']):
    print('------------- voici la liste des animaux ---------------')
    L_liste=[print(i) for i in liste]
    return L_liste

print_list()
#9. Déclarez une fonction nommée reverse_list. Elle prend un tableau comme paramètre et renvoie le tableau inversé (utilisez des boucles).
def reverse_list(tableau):
    L_tableau=[j for j in reversed(tableau)]
    return L_tableau

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]


#10. Déclarez une fonction nommée  `capitalize_list_items`. Elle prend une liste comme paramètre et renvoie une liste d'éléments en majuscules.
def capitalize_list_items(M_liste):
    majuscule=[x.upper() for x in M_liste]
    return majuscule
print(capitalize_list_items(['lion','chat','tigre','panthère','giraffe']))
#11. Déclarez une fonction nommée `add_item`. Elle prend une liste et un paramètre d'élément. Elle renvoie une liste avec l'élément ajouté à la fin.
def add_item(food_staff, element):
    food_staff.append(element)
    ajout=food_staff
    return ajout

#py
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
#py

#12. Déclarez une fonction nommée `remove_item`. Elle prend une liste et un paramètre d'élément. Elle renvoie une liste avec l'élément supprimé.
def remove_item(R_liste, element):
    R_liste.remove(element)
    E_sup=R_liste
    return E_sup
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango')) 
#py
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
#

#13. Déclarez une fonction nommée sum_of_numbers. Elle prend un paramètre de nombre et additionne tous les nombres dans cette plage.
def sum_of_numbers(nb):
    addition=sum(range(nb+1))
    return addition

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
#

#14. Déclarez une fonction nommée sum_of_odds. Elle prend un paramètre de nombre et additionne tous les nombres impairs dans cette plage.

def sum_of_odds(nb):
    total = 0
    for i in range(nb + 1):
        if i % 2 != 0:
            total += i
    return total

print(f" la somme des nombres impairs est égale à : {sum_of_odds(4)}")

#15. Déclarez une fonction nommée sum_of_even. Elle prend un paramètre de nombre et additionne tous les nombres pairs dans cette plage.
def sum_of_even(nb):
    total = 0
    for i in range(nb + 1):
        if i % 2 == 0:
            total += i
    return total

print(f" la somme des nombres pairs est égale à : {sum_of_even(4)}")
    
### Exercises: Level 2

#1.  Déclarez une fonction nommée evens_and_odds. Elle prend un entier positif comme paramètre et compte le nombre de nombres pairs et impairs.
def evens_and_odds(nb):
    pair=[]
    impair=[]
    
    for n in range(nb+1):
        if n % 2 == 0:
            pair.append(n)
        else:
            impair.append(n)
    return f"The number of odds are {len(pair)} \nThe number of evens are {len(impair)} "

print(evens_and_odds(100))
'''py
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
'''

#1. Appelez votre fonction factorial, elle prend un nombre entier comme paramètre et renvoie la factorielle du nombre.

def calc_factorielle(n):
    fact = 1
    for i in range(2,n+1):
        fact = fact * i
    return fact

print(calc_factorielle(3))
#1.  Appelez votre fonction _is_empty_, elle prend un paramètre et vérifie s'il est vide ou non.
def is_empty(any_structure):
    if any_structure:
        print("La structure n'est pas vide.")
        return False
    else:
        print("La structure est vide.")
        return True
    
ma_liste = []
is_empty(ma_liste)  

#1. Écrivez différentes fonctions qui prennent des listes. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

def calculate_mean(liste):
    """
    Calcule la moyenne (la valeur moyenne) des éléments dans la liste.
    """
    return sum(liste) / len(liste)

def calculate_median(liste):
    """
    Calcule la médiane (la valeur du milieu) des éléments dans la liste.
    """
    sorted_list = sorted(liste)
    n = len(sorted_list)
    if n % 2 == 0:
        middle1 = sorted_list[n // 2 - 1]
        middle2 = sorted_list[n // 2]
        return (middle1 + middle2) / 2
    else:
        return sorted_list[n // 2]

def calculate_mode(liste):
    """
    Calcule le mode (la valeur la plus fréquente) des éléments dans la liste.
    """
    from collections import Counter
    count_dict = Counter(liste)
    max_count = max(count_dict.values())
    mode_list = [key for key, value in count_dict.items() if value == max_count]
    return mode_list

def calculate_range(liste):
    """
    Calcule l'étendue (la différence entre la valeur maximale et minimale) des éléments dans la liste.
    """
    return max(liste) - min(liste)

def calculate_variance(liste):
    """
    Calcule la variance des éléments dans la liste.
    """
    mean = calculate_mean(liste)
    squared_diff_sum = sum((x - mean) ** 2 for x in liste)
    return squared_diff_sum / len(liste)

def calculate_std(liste):
    """
    Calcule l'écart-type des éléments dans la liste.
    """
    variance = calculate_variance(liste)
    return variance ** 0.5



### Exercises: Level 3

#1. Écrivez une fonction appelée is_prime, qui vérifie si un nombre est premier.
def is_prime(N):
    estPremier=1
    for i in range(2, int(N/2)):
        if (N%i==0):
            estPremier=0
            break
    if estPremier==1 :
        print(N, 'est un nombre premier')
    else:
        print(N, 'est un nombre non premier')
is_prime(12)

#2. Écrivez des fonctions qui vérifient si tous les éléments sont uniques dans la liste.
def unique(liste):
    if len(set(liste)) == len(liste):
        print('Les éléments sont uniques.')
    else:
        print('Ils ne sont pas uniques.')

unique(['lamine', 'camara', 'camara'])
#3. Écrivez une fonction qui vérifie si tous les éléments de la liste sont du même type de données.
def meme_type(liste):
    for element in liste:
        if not isinstance(element, type(liste[0])):
            return 'Ils ne sont pas du même type.'
    return 'Ils sont du même type.'
meme = meme_type([1, 3, 1.4])
print(meme)


#5. Allez dans le dossier data et accédez au fichier countries-data.py.
from data import countries
print(countries)
'''
import os
chemin = "C:/Users/HP/Desktop/students/data"
nom_fichier ="countries.py"
if os.path.exists(os.path.join(chemin,nom_fichier)):
    with open(os.path.join(chemin,nom_fichier), 'r', encoding="utf-8") as fichier:
        contenu = fichier.read()
        print(contenu) 
else:
    print(f"Le fichier '{nom_fichier}' n'existe pas dans le dossier '{chemin}'.")
'''



#6. Créez une fonction appelée les langues les plus parlées dans le monde. Elle doit renvoyer les 10 ou 20 langues les plus parlées dans le monde par ordre décroissant.

def langues_plus_parlees(chemin, nom_fichier, n=10):
    try:
        with open(f"{chemin}/{nom_fichier}", "r", encoding="utf-8") as fichier:
            liste_pays = eval(fichier.read())  
            langues = {}  
            for pays in liste_pays:
                for langue in pays.get("languages", []):
                    langues[langue] = langues.get(langue, 0) + 1

            # Trie les langues par nombre de locuteurs décroissant
            langues_triees = sorted(langues.items(), key=lambda x: x[1], reverse=True)

            # Renvoie les n premières langues
            return [langue for langue, _ in langues_triees[:n]]

    except FileNotFoundError:
        return f"Le fichier {nom_fichier} n'a pas été trouvé."

# Exemple d'utilisation
chemin = "C:/Users/HP/Desktop/students/data"
nom_fichier = "countries.py"
langues_top_10 = langues_plus_parlees(chemin, nom_fichier, n=10)
print(langues_top_10)




#7. Créez une fonction appelée les pays les plus peuplés. Elle doit renvoyer les 10 ou 20 pays les plus peuplés par ordre décroissant.
def pays_plus_peuples(chemin, nom_fichier, n=10):

    try:
        with open(f"{chemin}/{nom_fichier}", "r", encoding="utf-8") as fichier:
            liste_pays = eval(fichier.read())  # Évalue le contenu du fichier en tant que liste de dictionnaires
            pays_population = {}  # Dictionnaire pour stocker la population par pays

            for pays in liste_pays:
                nom_pays = pays.get("name", "")
                population = pays.get("population", 0)
                pays_population[nom_pays] = population

            # Trie les pays par population décroissante
            pays_tries = sorted(pays_population.items(), key=lambda x: x[1], reverse=True)

            # Renvoie les n premiers pays
            return [pays for pays, _ in pays_tries[:n]]

    except FileNotFoundError:
        return f"Le fichier {nom_fichier} n'a pas été trouvé."

# Exemple d'utilisation
chemin = "C:/Users/HP/Desktop/students/data"
nom_fichier = "countries.py"
pays_top_10 = pays_plus_peuples(chemin, nom_fichier, n=10)
print(pays_top_10)




#- Créez une fonction appelée most_spoken_languages. Elle doit renvoyer les 10 ou 20 langues les plus parlées dans le monde par ordre décroissant.


#- Créez une fonction appelée most_populated_countries. Elle doit renvoyer les 10 ou 20 pays les plus peuplés par ordre décroissant.



#🎉 CONGRATULATIONS ! 🎉
