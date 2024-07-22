## 💻 Challenges 07

#1. Créez un dictionnaire vide appelé `dog`.
dog={}

#2. Ajoutez `name`, `color`, `breed`, `legs`, `age` au dictionnaire `dog`.
dog.update([('name','lamine'), ('color','red'), ('breed',''),('legs',''), ('age',22)])
print(dog)

#3. Créez un dictionnaire `student` et ajoutez `first_name`, `last_name`, `gender`, `age`, `marital_status`, `skills`, `country`, `city` et `address` comme clés du dictionnaire.
student={'first_name': 'lamine', 'last_name':'camara', 'gender':'homme', 'age':'23', 'marital_status':'celibataire', 'skills':['IT_dev'], 'country':'Guinée', 'city':'Conakry', 'address': 'Nassouroulaye' }

#4. Obtenez la longueur du dictionnaire `student`.
L_dict=len(student)
print(L_dict)

#5. Obtenez la valeur de `skills` et vérifiez le type de données, cela devrait être une liste.
student['skills']
print(student['skills']) # juste pour voir les valeur de skills

#6. Modifiez les valeurs de skills en ajoutant une ou deux compétences.
student['skills'] +=['IT_Administrator','IT_network']
print(student['skills'])

#7. Obtenez les clés du dictionnaire sous forme de liste.
Liste_keys=list(student.keys())
print(f" voici les cles du dictionnaire \n{Liste_keys}")

#8. Obtenez les valeurs du dictionnaire sous forme de liste.
Liste_valeurs=list(student.values())
print(f" voici les valeurs du dictionnaire \n{Liste_valeurs}") # juste voir les valeurs

#9. Changez le dictionnaire en une liste de tuples en utilisant la méthode _items()_.
L_tuple=tuple(student.items())
print(L_tuple)

#10. Supprimez un des éléments du dictionnaire.
student.pop('skills')
print(student)
#11. Supprimez un des dictionnaires.
del [dog]

#🎉 CONGRATULATIONS ! 🎉