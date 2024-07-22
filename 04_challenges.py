
### resolution 4


### Level 1

#1. Déclarez une liste vide.
liste=[]
#2. Déclarez une liste avec plus de 5 éléments.
liste=['django', 'numpy','pandas','wordpress', 'bootstrap']

#3. Trouvez la longueur de votre liste.
len(liste)

#4. Obtenez le premier élément, l'élément du milieu et le dernier élément de la liste.
liste[::2]

#5. Déclarez une liste appelée mixed_data_types, mettez-y votre(name, age, height, marital status, address)
mixed_data_types = ["lamine", 12, 1.80, "celibataire", "Cosa"]

#6. Déclarez une variable de liste nommée it_companies et assignez-lui les valeurs initiales Facebook, Google, Microsoft, Apple, IBM, Oracle et Amazon.
it_companies =["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle" , "Amazon"]

#7. Imprimez la liste en utilisant _print()_
print(it_companies)

#8. Imprimez le nombre d'entreprises dans la liste.
print(len(it_companies))

#9. Imprimez la première, la moyenne et la dernière entreprise.
print(it_companies[::3])

#10. Imprimez la liste après avoir modifié l'une des entreprises.
it_companies[2]= 'Microsoft'
print(it_companies)

#11. Ajoutez une entreprise IT à it_companies.
it_companies.append('Tesla')

#12. Insérez une entreprise IT au milieu de la liste des entreprises.
it_companies.insert(4, 'huawai')

#13. Changez l'un des noms des it_companies en majuscules (IBM excluded!)
M_it=it_companies[3].upper()
print(M_it)

#14. Joignez les it_companies avec une chaîne de caractères '#;&nbsp; '
'#;&nbsp; '.join(it_companies)

#15. Vérifiez si une certaine entreprise existe dans la liste it_companies.
"Microsoft" in it_companies # verifie si _Microsoft_ dans la liste it_companies.

#16. Triez la liste en utilisant la méthode sort().
it_companies.sort() # trie la liste par croissant

#17. Inversez la liste dans l'ordre décroissant en utilisant la méthode reverse().
it_companies.reverse() # trie la liste par ordre decroissant

#18. Coupez les 3 premières entreprises de la liste.
it_companies[3:] # coupe les trois premières entreprises de la liste

#19. Coupez les 3 dernières entreprises de la liste.
it_companies[:-3] # coupe les trois dernière entreprises de la liste.

#20.  Coupez l'entreprise ou les entreprises IT du milieu de la liste.
milieu=len(it_companies)//2
test=(it_companies[:milieu] + it_companies[milieu +1:],it_companies[:milieu -1] + it_companies[milieu +1:] )[len(it_companies) % 2 ==0]
print(test)

#21. Supprimez la première entreprise IT de la liste.
it_companies.pop(0)

#22. Supprimez l'entreprise ou les entreprises IT du milieu de la liste.
del(it_companies[3:4])

#23. Supprimez la dernière entreprise IT de la liste.
it_companies.pop(-1)

#24. Supprimez toutes les entreprises IT de la liste.
it_companies.clear()

#25. Détruisez la liste des entreprises IT.
del(it_companies)

#26. Joignez les listes suivantes :
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
'''py
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
'''

#27. Après avoir joint les listes dans la question 26. Copiez la liste jointe et assignez-la à une variable full_stack. Ensuite, insérez `Python` et `SQL` après `Redux`.
full_stack = front_end
full_stack.extend(['python','SQL'])


### Level 2

#1. Voici une liste des âges de 10 étudiants :


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]


#- Triez la liste et trouvez l'âge minimum et maximum.
ages.sort()
min_age= min(ages) #minimum
max_age = max(ages) #maximum

#- Ajoutez de nouveau l'âge minimum et l'âge maximum à la liste.
ages.extend([min_age, max_age])

#- Trouvez l'âge médian (un élément du milieu ou deux éléments du milieu divisés par deux).
ages.sort()# pour trier la liste
G = sum(ages)//len(ages)
D = sum(ages)//len(ages)
median= (G+D)//2
print(median) # juste pour voir la medianne

#- Trouvez l'âge moyen (somme de tous les éléments divisée par leur nombre).
moyen = sum(ages)//len(ages)
print(moyen)
#- Trouvez l'écart des âges (max moins min).
ecart= max_age - min_age
print(ecart) # voir l'ecart

#- Comparez la valeur de (min - moyenne) et (max - moyenne), utilisez la méthode _abs()_.
abs(min_age) == abs(moyen)
abs(max_age) == abs(moyen)

#1. Trouvez le(s) pays du milieu dans la [liste des pays](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py).
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
  'mino'
]
milieu=len(countries)//2
V_condition= len(countries) % 2 ==0
#test=(countries[milieu], countries[milieu -1:milieu +1] )[V_condition]
#print(test)
#2. Divisez la liste des pays en deux listes égales si le nombre est pair, sinon ajoutez un pays de plus à la première moitié.
liste1=countries[milieu:] ; liste2=countries[:milieu]
if V_condition==False:
    if liste1 > liste2:
      liste2.append('lamine')
      print(f'----liste 1--{len(liste1)}')
      print(liste1)
      print(f'-----liste 2-----{len(liste2)}')
      print(liste2)
      print('niveau 2')
        
    else:
        liste1.append('lamine')
        print(f'----liste 1--{len(liste1)}')
        print(liste1)
        print(f'-----liste 2-----{len(liste2)}')
        print(liste2)
        print('niveau 3')
else:   
    print(f'----liste 1--{len(liste1)}')
    print(liste1)
    print(f'-----liste 2-----{len(liste2)}')
    print(liste2)
    print('niveau 1')


#3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Déballez les trois premiers pays et le reste en tant que pays scandinaves.
pays= ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
pays_scandinaves=pays[3:]
pays_deballe=pays[:3]
print('---------pays scandinaves-------')
print(pays_scandinaves)
print('---------pays deballer-------')
print(pays_deballe)


#🎉 CONGRATULATIONS ! 🎉

