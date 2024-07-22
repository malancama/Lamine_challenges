## Challenge 12 - Compte Bancaire

#![](https://images.unsplash.com/photo-1534322869500-14fc9f5f5767?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1650&q=80)
#Photo par [rawpixel](https://unsplash.com/photos/LTxCtKYw-_E)

## Objectifs
#Modéliser un compte bancaire pour améliorer vos compétences en POO.

## Directives
#1. Écrire une classe `Account` :
#- Le compte a quelques données, typiquement le `name` du titulaire du compte, le `account_number`, et le `balance` actuel (2000 par défaut).
#- Trois opérations que nous pouvons effectuer avec un compte sont `withdraw` de l'argent, `deposit` de l'argent sur le compte, et `dump` (imprimer) les données du compte.

#Instancier deux comptes pour Ross et Rachel avec des numéros de compte aléatoires. Déposer et retirer de l'argent plusieurs fois. Ensuite, afficher les informations sur les deux comptes. La sortie devrait ressembler à ceci :

''' python
ross_account.dump()
Ross, 9502018482, 1350
rachel_account.dump()
Rachel, 1945729572, 3450
'''

#2. Essayez maintenant d'instancier directement des comptes bancaires depuis votre console iPython et jouez avec eux. Astuce : vous devrez peut-être utiliser un `import` tout en étant dans le dossier approprié.

#Votre programme doit être écrit dans `bank_account.py`.
from bank_account import Account

# Instanciation des comptes pour Ross et Rachel
ross_account = Account("Ross", "123456")
rachel_account = Account("Rachel", "789012")

# Déposer et retirer de l'argent
ross_account.depot(1000)
ross_account.retrait(500)
rachel_account.depot(1500)
rachel_account.retrait(200)

# Afficher les informations sur les comptes
print("\nInformations sur le compte de Ross:")
ross_account.info()
print("\nInformations sur le compte de Rachel:")
rachel_account.info()
