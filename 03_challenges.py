## 💻 Challenges 03

#1. Concaténez les chaînes de caractères 'Thirty', 'Days', 'Of', 'Python' en une seule chaîne, 'Thirty Days Of Python'.
chaine = 'Thirty ' + 'Days ' + 'Of ' + 'Python' # 


#2. Concaténez les chaînes de caractères 'Coding', 'For' , 'All' en une seule chaîne, 'Coding For All'.
C_coding='Coding ' + 'For ' + 'All'


#3. Déclarez une variable nommée company et assignez-lui la valeur initiale "Coding For All".
company='Coding For All' # crée la variable company et lui assigne la valeur "Coding For All"

#4. Imprimez la variable company en utilisant _print()_.
print(company) # affiche la variable company

#5. Imprimez la longueur de la chaîne company en utilisant la méthode _len()_ et _print()_.
print(len(company)) # affiche la longueur de la variable company

#6. Changez tous les caractères en majuscules en utilisant la méthode _upper()_.
Mj_company=company.upper() # crée une variable Mj_company et lui assigne methode qui transforme les caractères de la variable company en majuscules.

#7. Changez tous les caractères en minuscules en utilisant la méthode _lower()_.
Mi_company= company.lower() # crée une variable Mi_company et lui assigne methode qui transforme les caractères de la variable company en miniscules.

#8. Utilisez les méthodes capitalize(), title(), swapcase() pour formater la valeur de la chaîne _Coding For All_.
 # crée une variable chaine_C et lui assigne la valeur "Coding For All"
"Coding For All".capitalize() # methode qui transforme le 1er caractère de chaine_C en majuscule.
"Coding For All".title() # methode qui transforme le 1er caractère de chaque mot de chaine_C en majuscule. 
"Coding For All".swapcase() # methode qui inverse la case : faire le contraire d'une methode precedente.

#9. Coupez (slice) le premier mot de la chaîne _Coding For All_.
 # crée une variable qui stock la chaine de caractère _Coding For All_
"Coding For All"[:6] # affiche le premier mot de la chaine _Coding For All_.

#10. Vérifiez si la chaîne _Coding For All_ contient le mot Coding en utilisant les méthodes index, find ou autres méthodes.
"Coding For All ".find('Coding') # verifie si la chaine contient le mot _Coding_.
"Coding For All".index('Coding') # verifie et affiche si la chaine contient le mot _Coding_.

#11. Remplacez le mot coding dans la chaîne 'Coding For All' par Python.
"Coding For All".replace("Coding","Python" ) # remplace et affiche le mot coding dans la variable chaine_D par python 

#12. Changez Python for Everyone en Python for All en utilisant la méthode replace ou d'autres méthodes.
"Python for Everyone".replace("Everyone", "All") # remplace et affiche le mot _Everyone_ dans la chaine par _All_ 

#13. Divisez la chaîne 'Coding For All' en utilisant l'espace comme séparateur (split()).
"Coding For All".split(" ") 

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" divisez la chaîne au niveau de la virgule.
"Facebook, Google, Microsoft, Apple, IBM".split(",") 

#15. Quel est le caractère à l'index 0 dans la chaîne _Coding For All_.
"Coding For All"[0] 

#16. Quel est le dernier index de la chaîne _Coding For All_.
"Coding For All"[-1] # affiche 

#17. Quel caractère se trouve à l'index 10 dans la chaîne "Coding For All".
"Coding For All"[10] 

#18. Créez un acronyme ou une abréviation pour le nom 'Python For Everyone'.
acro = [i[0] for i in "Python For Everyone".split(' ')]
''.join(acro)

#19. Créez un acronyme ou une abréviation pour le nom 'Coding For All'.
abv= [n[0] for n in "Coding For All".split(' ')]
''.join(abv)

#20. Utilisez l'index pour déterminer la position de la première occurrence de C dans Coding For All.
"Coding For All".index('C')

#21. Utilisez l'index pour déterminer la position de la première occurrence de F dans Coding For All.
"Coding For All".index('F')

#22. Utilisez rfind pour déterminer la position de la dernière occurrence de l dans Coding For All People.
"Coding For All People".rfind('l')

#23. Utilisez index ou find pour trouver la position de la première occurrence du mot 'because' dans la phrase suivante : 'You cannot end a sentence with because because because is a conjunction'.
"You cannot end a sentence with because because because is a conjunction".find('because')

#24. Utilisez rindex pour trouver la position de la dernière occurrence du mot because dans la phrase suivante : 'You cannot end a sentence with because because because is a conjunction'.
"You cannot end a sentence with because because because is a conjunction".rindex('because')

#25. Coupez la phrase 'because because because' dans la phrase suivante : 'You cannot end a sentence with because because because is a conjunction'.
coupe = 'You cannot end a sentence with because because because is a conjunction'.split('because')
''.join(coupe)

#26. Trouvez la position de la première occurrence du mot 'because' dans la phrase suivante : 'You cannot end a sentence with because because because is a conjunction'.
'You cannot end a sentence with because because because is a conjunction'.find('because')

#27. Coupez la phrase 'because because because' dans la phrase suivante : 'You cannot end a sentence with because because because is a conjunction'.
coupe2 = 'You cannot end a sentence with because because because is a conjunction'.split('because')
''.join(coupe2)

#28. La chaîne '\'Coding For All' commence-t-elle par une sous-chaîne _Coding_ ?
'\'Coding For All'.startswith('Coding')


#29. La chaîne 'Coding For All' se termine-t-elle par une sous-chaîne _coding_ ?
'Coding For All'.endswith('coding')

#30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, supprimez les espaces à gauche et à droite dans la chaîne donnée.
'&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;'.strip()

#32. La liste suivante contient les noms de certaines bibliothèques python : ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Joignez la liste avec une chaîne de caractères hash avec espace.
' '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'])

#33. Utilisez la séquence d'échappement de nouvelle ligne pour séparer les phrases suivantes.
print("I am enjoying this challenge.\nI just wonder what is next.")

'''py
    I am enjoying this challenge.
    I just wonder what is next.
    '''
#34. Utilisez la séquence d'échappement de tabulation pour écrire les lignes suivantes.
print('Name\tAge\tCountry\tcity\nAsabeneh\t250\tFinland\tCity')  
'''py
    Name      Age     Country   City
    Asabeneh  250     Finland   Helsinki
'''

#35. Utilisez la méthode de formatage de chaîne pour afficher ce qui suit :
radius =10
area=3.14 * radius **2
print("The area of a circle with radius {0} is  {1} meters square".format(radius, int(area)))
print(f"The area of a circle with radius {radius} is {area} meters square")
'''sh
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
'''

#36. Réalisez ce qui suit en utilisant les méthodes de formatage de chaîne :

nb1=8 ; nb2= 6
print(f" {nb1} + {nb2} = {nb1 + nb2}")
print(f"{nb1} - {nb2} = {nb1 - nb2}")
print(f"{nb1} * {nb2} = {nb1 * nb2}")
print(f"{nb1} / {nb2} = {(nb1 / nb2):.2f}")
print(f"{nb1} % {nb2} = {nb1 % nb2}")
print(f"{nb1} // {nb2} = {nb1 // nb2}")
print(f"{nb1} ** {nb2} = {nb1 ** nb2}")
'''sh
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''
'''
🎉 CONGRATULATIONS ! 🎉
'''
