## 💻 Challenges 06


# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


### Level 1

#1. Trouvez la longueur de l'ensemble it_companies.
len(it_companies)
#2. Ajoutez 'Twitter' à it_companies.
it_companies.add('Twitter')
print(it_companies)
#3. Insérez plusieurs entreprises IT à la fois dans l'ensemble it_companies.
it_companies=it_companies.union({'Tulip','Nimba'})
print(it_companies)
#4. Supprimez l'une des entreprises de l'ensemble it_companies.
it_companies.pop()

#5. Quelle est la différence entre `remove` et `discard` ?

# sont tous des fonction qui supprime mais la différence est que si  l'élément n'est pas présent dans l'ensemble, discard ne fait rien, tandis que remove génère une erreur.

### Level 2

#1. Joignez A et B.
print('jonction de A et B',A | B)
#2. Trouvez l'intersection de A et B.
print('intersection de A et B',A.intersection(B))

#3. A est-il un sous-ensemble de B ?
if A<=B:
    print('A est un sous ensembe de B')
else:
    print('A n\'est pas un sous ensemble de B')
#4. A et B sont-ils des ensembles disjoints ?
A.isdisjoint(B)
#5. Joignez A avec B et B avec A.
A | B
#6. Quelle est la différence symétrique entre A et B ?
S_dif=A.symmetric_difference(B)
print(S_dif)
#7. Supprimez complètement les ensembles.
del A
del B
### Exercises: Level 3

#1. Convertissez les âges en un ensemble et comparez la longueur de la liste et de l'ensemble, lequel est plus grand ?
E_age=set(age)
if len(age)>len(E_age):
    print('age est plus grand')
elif len(age)<len(E_age):
    print('ensemble age est plus grand')
else:
    print('il sont egale')

#2. Expliquez la différence entre les types de données suivants : string, list, tuple et set.
#string : utiliser la representation des chaines de caractères,
#list: utilise une liste d'objet
#tuple: collection d'objet mais qui ne sont pas modifiable
#set: est aussi une collection d'objet unique

#3. _I am a teacher and I love to inspire and teach people._ Combien de mots uniques ont été utilisés dans la phrase ? Utilisez les méthodes split et set pour obtenir les mots uniques.
phrase='I am a teacher and I love to inspire and teach people'
S_phrase = phrase.split(' ')
print(f' {len(set(S_phrase))} mots unique on été utilisé dans cette phrase')
#🎉 CONGRATULATIONS ! 🎉
