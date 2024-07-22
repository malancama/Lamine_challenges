## 💻 Challenges 05

### Level 1

#1. Créez un tuple vide.
Tuple = ()
#2. Créez un tuple contenant les noms de vos sœurs et de vos frères (des frères et sœurs imaginaires sont acceptables).
N_Frere=('sana','samso')
N_Soeur=('oumou','mama','hawa','fatim')

#3. Joignez les tuples des frères et sœurs et assignez-le à siblings.
siblings=N_Frere + N_Soeur

#4. Combien de frères et sœurs avez-vous ?
L_siblings=len(siblings)
print(f"j'ai {L_siblings} frères et soeurs")
#5. Modifiez le tuple siblings et ajoutez le nom de votre père et de votre mère et assignez-le à family_members.
siblings += ('Maman', 'papa')
family_members = siblings


### Level 2

#1. Déballez siblings et parents à partir de family_members.
siblings = family_members[-2:]
parents= family_members[:-2]
#2. Créez des tuples fruits, vegetables et animal products. Joignez les trois tuples et assignez-les à une variable appelée food_stuff_tp.
fruits=('mangue','orange') ; vegetables=('choux','salade', 'marcronie','marmites') ; animal= ('chèvre','poulet')
food_stuff_tp= fruits + vegetables + animal

#3. Changez le tuple food_stuff_tp en une liste food_stuff_lt.
food_stuff_lt = list(food_stuff_tp)

#4. Coupez l'élément ou les éléments du milieu du tuple food_stuff_tp ou de la liste food_stuff_lt.

milieu=len(food_stuff_lt)//2
test=(food_stuff_lt[:milieu] + food_stuff_lt[milieu +1:],food_stuff_lt[:milieu -1] + food_stuff_lt[milieu +1:] )[len(food_stuff_lt) % 2 ==0]
print(test)

#5. Coupez les trois premiers éléments et les trois derniers éléments de la liste food_stuff_lt.
food_stuff_lt[3:-3]
#6. Supprimez complètement le tuple food_stuff_tp.
del(food_stuff_tp)
#7. Vérifiez si un élément existe dans le tuple :
'mangue' in food_stuff_tp
#- Vérifiez si 'Estonia' est un pays nordique.
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
  print('Estonia est un pays nordique')
else:
  print('Estonia n\'pas un pays nordique')
#- Vérifiez si 'Iceland' est un pays nordique.
if 'Iceland' in nordic_countries:
  print('Iceland est un pays nordique')
else:
  print('Iceland n\'est pas un pays nordique')

  '''py
  nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
  '''
