### challenges 02

#1. Déclarez votre âge comme une variable entière.
age=int(20) # crée la variable age de type entière et lui assigne la valeur 20 

#2. Déclarez votre taille comme une variable flottante.
taille=float(12) # crée la variable taille de type flottante et lui assigne la valeur 12

#3. Déclarez une variable qui stocke un nombre complexe.
n_complex= complex(2) # crée la valeur n_complex de type complex qui stocke un nombre complexe.

#4. Écrivez un script qui demande à l'utilisateur d'entrer la base et la hauteur du triangle et calcule l'aire de ce triangle (area = 0.5 x b x h).
base=float(input("veiller saisir la base du triange: ")) # crée la variable base de type flootante et demande à l'utilisateur de saisir une valeur
hauteur = float(input("veille saisir la hauteur du triange: ")) # crée la variable hauteur de type flootante et demande à l'utilisateur de saisir une valeur
area = 0.5 * base * hauteur # crée la variable area et lui assigne l'air du cercle

#5.Écrivez un script qui demande à l'utilisateur d'entrer les côtés a, b et c du triangle. Calculez le périmètre du triangle (perimeter = a + b + c).
a=int(input("veiller saisir la valeur de a : "))
b=int(input("veiller saisir la valeur de b: "))
c=int(input("veiller saisir la valeur de c: "))
perimeter=a+b+c
print(perimeter) # affiche la valeur contenu dans la variable perimeter

#6. Obtenez la longueur et la largeur d'un rectangle en utilisant une invite. Calculez son aire (area = length x width) et son périmètre (perimeter = 2 x (length + width)).
length=float(input('veiller saisir la longueur: ')) 
width=float(input('veiller saisir la largeur : '))
area= length * width # l'air du cercle
perimeter = 2*(length + width) # le périmètre du cercle
print(f"l'air du cercle est de {area} et son perimètre est {perimeter}") # affiche l'air et le perimètre du cercle.

#7. Obtenez le rayon d'un cercle en utilisant une invite. Calculez l'aire (area = pi x r x r) et la circonférence (c = 2 x pi x r) où pi = 3.14.
rayon = float(input("tapez le rayon du cercle : "))
pi=3.14
area= pi *rayon * rayon # l'air du cercle
c= 2 * pi * rayon # la circonférence du cercle
print(f"l'air du cercle est de {area} et sa circonférence est de {c}") # affiche l'air et la circonférence du cercle

#8. Calculez la pente, l'ordonnée à l'origine et l'abscisse à l'origine de y = 2x -2.
# y= mx + b et y=2x -2 , comparativement la 
m = 2 #pente
# l'ordonnée à l'origine x =0
x=0
y = m*x - 2 # l'ordonnée à l'origine
print(y) # affiche la valeur de l'ordonné à l'origine
# l'abscisse à l'origine 
y = 0
x = (y +2)/m
print(x) # affiche la valeur de l'abscisse à l'origine

#9. La pente est (m = y2-y1/x2-x1). Trouvez la pente et la [distance euclidienne](https://fr.wikipedia.org/wiki/Distance_euclidienne) entre le point (2, 2) et le point (6, 10).
from math import sqrt 
x1=2 
x2=2
y1=6
y2=10
m1=y2-y1/x2-x1 # pente
d=sqrt((x2 -x1)**2 + (y2 - y1)**2) # distance euclidienne 
print(f"la pente est de {m1} et la distance est {d}") # affiche la pente et la distance euclidienne entre le point(2, 2) et le point (6, 10)

#10. Comparez les pentes des tâches 8 et 9.
print(m==m1) #compare la valeur des deux pentes.

#11. Calculez la valeur de y (y = x^2 + 6x + 9). Essayez d'utiliser différentes valeurs de x et trouvez à quelle valeur de x y sera égal à 0.
x=-3 # -3 est la valeur de x à laquelle y est égal à 0
y=x**2 + 6*x + 9
print(y) # affiche la valeur de y qui est egal à 0.

#12. Trouvez la longueur de 'python' et 'dragon' et faites une déclaration de comparaison fausse.
L_python = len('python') #longueur du mot 'python'
L_dragon = len('dragon') # longueur du mot 'dragon'
print(L_python > L_dragon) # compare si L_python et superieur à L_dragon

#13. Utilisez l'opérateur _and_ pour vérifier si 'on' se trouve à la fois dans 'python' et 'dragon'.
print("on" in ("python" and "dragon")) # verifie et affiche si 'on' se trouve dans 'python' et 'dragon'

#14. _I hope this course is not full of jargon_. Utilisez l'opérateur _in_ pour vérifier si _jargon_ est dans la phrase.
print("jargon" in 'I hope this course is not full of jargon') # verifie et affiche si le mot 'jargon' est pas dans la phrase.

#15. Il n'y a pas de 'on' dans 'dragon' et 'python'.
print('on' not in 'dragon' and 'python') # vérifie et affiche si 'on' n'est pas dans 'dragon' et 'python'

#16. Trouvez la longueur du texte _python_ et convertissez la valeur en flottant puis en chaîne de caractères.
L_python = (len('python')) # L_python = longueur du mot 'python'
float_python = float(L_python) # longueur de python convertis en valeur decimale
Str_python = str(L_python)    # longueur de python de python convertis en chaine de caractère.
print(L_python, float_python, Str_python) # affiche le contenu des variable L_python, float_python, Str_python.

#17. Les nombres pairs sont divisibles par 2 et le reste est zéro. Comment vérifiez-vous si un nombre est pair ou non en utilisant python ?
nb = 6 #exemple de nombre
print(nb % 2 == 0) # verifie et affiche si nb est divisible par 2

#18. Vérifiez si la division entière de 7 par 3 est égale à la valeur convertie en entier de 2.7.
Div_entier = 7//3 # division entiere de 7 par 3
V_entiere =  int(2.7) # valeur entière de 2.7
print(Div_entier == V_entiere) # verifie si Div_entier est égale à V_entiere

#19. Vérifiez si le type de '10' est égal au type de 10.
print(type(10) == type('10')) # verifie et affiche si le type de la valeur 10 est egale au type de la valeur '10'.


#20. Vérifiez si int('9.8') est égal à 10.
print(int(9.8)== 10) # verifie et affiche si la partie entière de 9.8 est egale à 10.

#21. Écrivez un script qui demande à l'utilisateur d'entrer les heures et le taux par heure. Calculez le salaire de la personne.
heures=int(input("veiller saisir les heures : ")); #  heure
T_heures= int(input("veiller entrer le taux par heure : ")) # Taux par heure
salaire = heures* T_heures # salaire de la personne
print(salaire) # affiche le contenu de la variale salaire.

#22. Écrivez un script qui demande à l'utilisateur d'entrer un nombre d'années. Calculez le nombre de secondes qu'une personne peut vivre. Supposons qu'une personne puisse vivre cent ans.
'''py
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
'''

Nb_ans=int(input("veiller saisir le nombre d'années: ")) # nombre d'année vecu
nb_second_ans=31536000 # nombre de seconde par ans
print(f"vous avez vecu {Nb_ans * nb_second_ans}") # affiche le nombre de seconds que vous avec vecu depuis votre naissance.
