''' Challenge 01 '''

### résolution : Niveau 01

1. # Écrivez un commentaire en python disant '1000 TeachLeaders python programming'.
# 1000 TeachLeaders python programming

2. # Déclarez une variable first_name et assignez-lui une valeur.
first_name= 'Mohamed lamine' 
print(first_name) 

3. # Déclarez une variable last_name et assignez-lui une valeur.
last_name ='Camara' 
print(last_name) 
4. # Déclarez une variable full_name et assignez-lui une valeur.
full_name = first_name + last_name 
print(full_name) 

5. #Déclarez une variable country et assignez-lui une valeur.
country = 'Guinée' 
print(country) 

6. # Déclarez une variable city et assignez-lui une valeur.
city = 'Conakry' 
print(city) 

7. #Déclarez une variable age et assignez-lui une valeur.
age = 23 
print(age) 

8. # Déclarez une variable year et assignez-lui une valeur.
year = 2024 
print(year) 

9. #Déclarez une variable is_married et assignez-lui une valeur.
is_married =True 
print(is_married) 

10. # Déclarez une variable is_true et assignez-lui une valeur.
is_true = False 
print(is_true) 

11. # Déclarez une variable is_light_on et assignez-lui une valeur.
is_light_on = True 
print(is_light_on) 

12. # Déclarez plusieurs variables sur une seule ligne.
nom = last_name ; prenom = first_name ; age = age 
print(nom, prenom, age) 
### résolution : Niveau 2
1. #Vérifiez le type de données de toutes vos variables en utilisant la fonction intégrée type().
print(type(first_name)) # affiche le type de valeur contenue dans la variable first_name
print(type(last_name)) # affiche le type de valeur contenue dans la variable last_name
print(type(full_name)) # affiche le type de valeur contenue dans la variable full_name
print(type(country)) # affiche le type de valeur contenue dans la variable country
print(type(city)) # affiche le type de valeur contenue dans la variable city
print(type(age)) # affiche le type de valeur contenue dans la variable age
print(type(year)) # affiche le type de valeur contenue dans la variable year
print(type(is_married)) # affiche le type de valeur contenue dans la variable is_married
print(type(is_true)) # affiche le type de valeur contenue dans la variable is_true
print(type(is_light_on)) # affiche le type de valeur contenue dans la variable is_light_on

2. #En utilisant la fonction intégrée _len()_, trouvez la longueur de votre prénom.
L_prenom=len(first_name) 
print(f"la longueur de votre prénom est : {L_prenom}")


3. #Comparez la longueur de votre prénom et de votre nom de famille.
L_nom = len(last_name) 
print(L_prenom==L_nom) 

4. #Déclarez 5 comme num_one et 4 comme num_two.
num_one=5 
num_two=4 

#    1. Additionnez num_one et num_two et assignez la valeur à une variable total.
total = num_one + num_two 
print(total) 

#    2. Soustrayez num_two de num_one et assignez la valeur à une variable diff.
diff = num_one - num_two 
print(diff) 

#    3. Multipliez num_two et num_one et assignez la valeur à une variable product.
product = num_two * num_one 
print(product) 

#    4. Divisez num_one par num_two et assignez la valeur à une variable division.
division = num_one/num_two 
print(division) 

#    5. Utilisez la division par modulo pour trouver num_two divisé par num_one et assignez la valeur à une variable remainder.
remainder = num_two % num_one 
print(remainder) 

#    6. Calculez num_one à la puissance de num_two et assignez la valeur à une variable exp.
exp = num_one ** num_two 
print(exp) 

#    7. Trouvez la division entière de num_one par num_two et assignez la valeur à une variable floor_division.
floor_division = num_one // num_two 
print(floor_division) 

#5. Le rayon d'un cercle est de 30 mètres.
rayon = 30 
#    1. Calculez l'aire d'un cercle et assignez la valeur à une variable nommée _area_of_circle_.
area_of_circle = 3.14 * rayon * rayon 
print(area_of_circle) 

#    2. Calculez la circonférence d'un cercle et assignez la valeur à une variable nommée _circum_of_circle_.
circum_of_circle = 2*3.14*rayon 
print(circum_of_circle) 

#    3. Prenez le rayon comme entrée utilisateur et calculez l'aire.
rayon = float(input('veiller saisir la valeur du rayon: ')) 
area_of_circle = 3.14 * rayon * rayon 
print(area_of_circle) 

#6. Utilisez la fonction intégrée input pour obtenir le prénom, le nom de famille, le pays et l'âge d'un utilisateur et stockez la valeur dans les variables correspondantes.
first_name=input('veiller entrer le prénom: ') 
last_name =input('veiller entrer le nom de famille: ') 
country =input('veiller entrer le nom du pays: ') 
age= int(input("veiller saisir l'age de l'utilisateur: ")) 
print(f'Prénom: {first_name} \nNom: {last_name} \nPays: {country} \nAge: {age}') 

#7. Exécutez help('keywords') dans le shell Python ou dans votre fichier pour vérifier les mots réservés ou mots-clés de Python.
'''help> keywords # saisir le mot help et en plus keywords pour vérifier les mots réservés ou mots-clés de python.
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield

'''