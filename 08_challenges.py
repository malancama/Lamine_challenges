## 💻 Challenges 08:

### Level 1

#1. Obtenez l'entrée utilisateur en utilisant input("Enter your age: "). Si l'utilisateur a 18 ans ou plus, donnez un retour : `You are old enough to learn to drive.`. Si l'utilisateur a moins de 18 ans, donnez un retour pour indiquer le nombre d'années manquantes. Exemple de sortie :
'''sh
Enter your age: 30
You are old enough to learn to drive.
sh
Enter your age: 15
You need 3 more years to learn to drive.
'''

age=int(input('veiller saisir votre age: '))
if age >=18:
     print("Tu es assez grand pour apprendre à conduire.")
else:
     print(f"Tu as besoin de  {18 - age} ans de plus pour apprendre à conduire.")
#2. Comparez les valeurs de my_age et your_age en utilisant if ... else. Qui est le plus âgé (moi ou vous) ? Utilisez input("Enter your age: ") pour obtenir l'âge en entrée. Vous pouvez utiliser une condition imbriquée pour imprimer 'year' pour une différence d'un an, 'years' pour des différences plus importantes, et un texte personnalisé si my_age = your_age. Exemple de sortie :

'''
    Enter your age: 30
    You are 5 years older than me.
'''
my_age=23
your_age= int(input('veiller entrer votre age: '))
compare=abs(my_age-your_age)
phrase=f"I'm {compare} years older than you"
ages=(phrase.replace('years','year'), phrase)[compare >1]
if my_age > your_age:
    print(ages)
elif my_age < your_age:
    print(ages.replace('I\'m', 'You are').replace('you','me'))
else: 
    print('we are equal')

#3. Obtenez deux nombres de l'utilisateur en utilisant une invite d'entrée. Si a est plus grand que b, renvoyez a is greater than b, si a est plus petit que b, renvoyez a is smaller than b, sinon renvoyez a is equal to b. Exemple de sortie :

a=int(input('Enter number one: '))
b=int(input('Enter number two: '))
if a>b:
     print(f'{a} is greater than {b}')
elif a<b:
     print(f'{a} is smaller than {b}')
else:
     print(f'{b} is equal to {b}')

'''
    Enter number one: 4
    Enter number two: 3
    4 is greater than 3
'''

### Level 2

#1. Écrivez un code qui attribue une note aux étudiants en fonction de leurs scores :
scores=int(input('Entrer votre score: '))
if 80 < scores < 100:
     print('A')
elif 70<scores < 89:
     print('B')
elif 60<scores < 69:
     print('C')
elif 50< scores < 59:
     print('D')
elif 0< scores<49:
     print('F')
else:
     print('cette note n\'existe pas')
'''sh
        80-100, A
        70-89, B
        60-69, C
        50-59, D
        0-49, F
'''
#2. Vérifiez si la saison est Automne, Hiver, Printemps ou Été. Si l'utilisateur saisit

automne=['Septembre', 'Octobre', 'Novembre']
hiver= ['Décembre', 'Janvier', 'Février']
printemps = ['Mars', 'Avril', 'Mai']
Ete=['Juin', 'Juillet', 'Août']
mois=input('veiller saisir le mois: ')
if mois in automne:
     print('automne')
elif mois in hiver:
     print('hiver')
elif mois in printemps:
     print('printemps')
elif mois in Ete:
     print('Eté')
else:
     print('existe pas')
     print('veiller bien verifier le mot saisi')
'''
Septembre, Octobre ou Novembre, la saison est Automne.
Décembre, Janvier ou Février, la saison est Hiver.
Mars, Avril ou Mai, la saison est Printemps.
Juin, Juillet ou Août, la saison est Été.
'''
#3.  La liste suivante contient quelques fruits :
'''sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
'''
#Si un fruit n'existe pas dans la liste, ajoutez-le à la liste et imprimez la liste modifiée. Si le fruit existe, imprimez 'Ce fruit existe déjà dans la liste.')
fruits = ['banana', 'orange', 'mango', 'lemon']
S_fruits= input('veiller saisir un fruit: ')
if S_fruits in fruits:
     print('Ce fruit existe déjà dans la liste')
else:
     fruits +=[S_fruits]
     print(fruits)

### Exercises: Level 3

#1. Voici un dictionnaire `person`. N'hésitez pas à le modifier !


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#* Vérifiez si le dictionnaire person a la clé `skills`, si oui, imprimez la compétence du milieu dans la liste `skills`.
if 'skills' in person.keys():
     print(person['skills'][2:-2])
#* Vérifiez si le dictionnaire person a la clé `skills`, si oui, vérifiez si la personne a la compétence 'Python' et imprimez le résultat.
if 'skills' in person.keys():
    if 'python' in person['skills']:
          print('oui il a la compétence')
    else:
        print('non il n\'a pas cette compètence')
    
#* Si les compétences de la personne incluent uniquement JavaScript et React, imprimez 'Il est un développeur front end', si les compétences de la personne incluent `Node`, `Python`, `MongoDB`, imprimez 'Il est un développeur back end', si les compétences de la personne incluent `React`, `Node` et `MongoDB`, imprimez 'Il est un développeur fullstack', sinon imprimez 'titre inconnu' - pour des résultats plus précis, d'autres conditions peuvent être imbriquées !

if len(person['skills']) == len(['JavaScript','React']) and ('JavaScript' in person['skills'] and 'React' in person['skills']):
     print("Il est un développeur front end")
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print("Il est un développeur back end")
    if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print("Il est un développeur fullstack")
else:
    print("titre inconnu")
#* Si la personne est mariée et vit en Finlande, imprimez les informations dans le format suivant :
if person['is_marred']==True and person['country']=='Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")

'''py
    Asabeneh Yetayeh lives in Finland. He is married.
'''

#🎉 CONGRATULATIONS ! 🎉
