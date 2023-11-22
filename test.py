print("Hello World!")
print("Hello Friend!")
print("Je m'appelle Public Enemy !")
a=5
b=7
print(a+b)
print ('Elle s\'appelle Rowland, Kelly Rowland')
print("\u2764")
c = str(10)
print(c)
c= int(10)
print (c+a+b)
"""Affectations parallèles"""
a,b,c = 10,14,20
print(a+b+c)
"""Affectations multiples"""
a=b=c=5
print(a+b+c)
"""Singletons : True/False, nombres entre -5 et 256"""
c=500
print(id(c))
print(id(c))
a=5
print(id(a))
print(id(a))

print(id(400))
print(id(400))

"""Type des Objets """

c = 14
print (type(c))

d = "12"
print(type(d))

e = 12.2
print(type(e))
   

""" Fonction Input et typage d'objets"""

"""number = input("Entrez un nombre :")
print(number)

print(type(number))"""

""" Concaténation de variables"""

"""exercices""" 
a = "J'ai une classe de " + str(30) + " élèves"   # ou sans concaténation "J'ai une classe de 30 élèves" 
b = str(10) + " + 5  est égal à " + str(15)  # sans concaténation "10 + 5 est égal à 15"
c =  10 + int("5")  # sans concaténation 10 + 5
d =  "L'addition de 10 + 5 est égale à: " + str(10 + 5)  #sans concaténation "L'addition de 10 + 5 est égale à 15"

print(a)
print(b)
print(c)
print(d)

"""Manipuler les chaines de caractères"""
#Changer la casse
a = "Bonjour".upper()

print(a)

a = a.lower()

print(a)

a= a.capitalize()

print(a)

a = "bonjour tout le monde !"
a= a.title()

print(a)

#Remplacer des éléments

a = "Bonjour".replace("jour", "soir")

print(a)

a = "Bonjour, bonjour, bonjour".replace("jour", "soir")

print(a)

a = "Bonjour, bonjour, bonjour".replace(",", "/")

print(a)

#remplacer
a = "Bonjour bonjour bonjour".replace(" ", "")

print(a)
print(a.replace("jour", "soir"))

#enlever 
a="  Bonjour tout le monde  ".strip("tout le monde")
print(a)

a="  Bonjour tout le monde  ".rstrip("tout le monde")
print(a)

a="Bonjour tout le monde  ".lstrip("monde")
print(a)

#Séparer et joindre
list = "1, 2, 3, 4, 5".split(", ")

print(list)
print(", ".join(list))

list = "1, 2, 3, 4, 5".split(", ")
 
print("3".join(list))

#Remplir de zéros

a="5".zfill(2) 

print(a)
a="5".zfill(4)
print(a)

for i in range(10):
    print(i)
    
for i in range(10):
    print(str(i).zfill(4))    
    
    """Méthodes "is" (lower/upper/digit/title) Chaine de Caractères"""
a =  "BONJOUR".islower()

print(a)

a =  "bonjour".islower()

print(a)

a =  "BONJOUR".isupper()

print(a)

a =  "bonjour".isupper()

print(a)

a =  "bonjour tout le monde".istitle()

print(a)

a =  "Bonjour Tout Le Monde".istitle()

print(a)

a =  "Bonjour vous 5".isdigit()

print(a)

a =  "5".isdigit()

print(a)

#Compter le nombre d'occurences
"""Méthode 'count' """
a = "Ce soir c'est un soir pour dire Bonsoir".count("soir")

print(a)

a = "Ce soir c'est un soir pour dire Bonsoir".count(" soir") #placer un espace avant le mot recherché pour ne pas avoir comptabilisé 'soir' de 'bonsoir'

print(a)

#Trouver une substring avec 'find" ou 'index'

a = "Ce soir c'est un soir pour dire Bonsoir".find("soir")

print(a) # comptabilise à partir de quel caractère apparait la substring recherchée

a = "Ce soir c'est un soir pour dire Bonsoir".index("soir")

print(a) # comptabilise à partir de quel caractère apparait la substring recherchée

a = "Ce soir c'est un soir pour dire Bonsoir".find("jour") #quand la substring est introuvable la valeur retournée est '-1', quand la méthode index est utilisée et que la substring est introuvable => erreur 

print(a)

a = "Ce soir c'est un soir pour dire Bonsoir".rfind("soir") #quand la méthode 'rfind' est utilisée, c'est la 1ère occurrence de la substring qui est recherchée en partant de la droite de la chaine de caractères initiale. la méthode 'lfind' n'existe pas car la recherche se fait déjà automatiquement au début de la chaine de caractère initiale avec 'find'

print(a)

#Chercher au début et à la Fin de chaine

a = "image.png".startswith("image") 

print(a)

a = "image.png".startswith("fichier") 

print(a)

a = "image.png".endswith("png") 

print(a)

a = "image.png".endswith("jpg") 

print(a) 

""" Opérateurs"""
#Opérateurs mathématiques 

print (10 + 7) 

print (5-2)

print (5 * 2)

print (12 / 3 ) # donne un float

print("Hello" + "Dolly") #Concaténation

print("Funky" * 2)

##Modulo ( reste d'une division)
print(15 % 3) #reste 0
print(15 % 6) #reste 3

#Division entière
print(14//3) #donne l'entier le plus proche

#opérateur "puissance" = **

print(3**2) #9

#Opérateurs d'assignation
    ##Incrémentation
i = 0

for i in range(3):
    i+=1
    print("la valeur de i = " + str(i))

#Opérateurs de comparaison
## < > <= >= == !=
### Différence entre == et is

a = [1, 2, 3]
b = [1, 2, 3]

print (a == b) # True

print (a is b) # False car l'adresse de l'objet en mémoire de a et b est différente sauf pour des valeurs entre -5 et 256

print(id(a))
print(id(b))

a =10
b=10
print (a == b)
print (a is b) #true car case mémoire équivalente car nombre compris entre -5 et 256

a = - 4
b = -4
c = 256
d = 256

print (a == b)
print (c == d)
print (a is b) 
print (c is d)#true car case mémoire équivalente car nombre compris entre -5 et 256

a = - 6
b = -6
c = 300
d = 300

print (a == b)
print (c == d)
print (a is b) 
print (c is d)#false car nombre non compris entre -5 et 256, bizarrement retourne True

"""Mise en forme (formater ou concaténer) des chaines de caractères pour y insérer des variables """



 #avec la méthode f-string

a = "Dolly"
b = f"Hello {a} !"
print(b)

#Pas besoin de conversion telle que str(a) ou str(b) 
a = 3
b = 5

c = f"La multiplication de {a} par {b} est égale à {a * b}"
print(c)


#avec la méthode format

age = 237 
phrase = "J'ai {} ans".format(age)
print(phrase)

age = 97
prenom = "albert" 
phrase = "J'ai {} ans et je m'appelle {}".format(age, prenom)
print(phrase)


## avec indentifiant

age = 375 
phrase = "J'ai {a} ans".format(a=age)
print(phrase)

age = 237
prenom = "glinglin" 
phrase = "J'ai {} ans et je m'appelle {name}".format(age,name=prenom)
print(phrase)

 ## avec des indices
age = 237
prenom = "glinglin" 
phrase = "J'ai {0} ans et je m'appelle {1}".format(age, prenom)
print(phrase)

## Résumé
protocole = "https://"
nom_du_site = "twitter"
extension = "com"
#avec opérateur +

url = protocole + "www." + nom_du_site +"." + extension

print(url)

#avec méthode format

url = "{}www.{}.{}".format(protocole, nom_du_site, extension)

print(url)

url = "{proto}www.{domaine}.{ext}".format(proto=protocole, domaine=nom_du_site, ext="com")

print(url)

#avec f-string = la plus simple

url = f"{protocole}www.{nom_du_site}.{extension}"

print(url) 

#Particularité de la méthode format

##constants.py


##main.py

"""Structures Conditionnelles"""
#Introduction
## Une condition retourne un booléen

age = 54

if age >= 18 :
    print( f"Vous avez {age} ans, vous êtes donc majeur")

age = int(input("Quel age avez-vous ? "))

if age >= 18:
    print( f"Vous avez {age} ans, vous êtes donc majeur !")
elif age < 18:
    print("Dsl, vous n'avez pas accès à ce contenu car vous êtes mineur !")

user = "admin" 
  
if user =="admin":
    print("Accès Autorisé")
elif user == "root":    
    print("Accès Autorisé")
else:
    print("Accès Refusé")
    
note = 19

if note <= 10 :
    print("Vous avez moins que la moyenne !")
elif note > 10 and note <= 14:
    print("Vous avez la moyenne !")
elif note > 14 and note < 18:
    print("Bravo, vous faites partie des meilleurs !!!")
else:
    print("Bravo vous êtes le mieux noté !!!")
    
    
#Les Opérateurs ternaires   

## version normale en 5 lignes
age =25

if age >= 18:
    majeur = True 
else:
    majeur = False
    
    
## version ternaire en 2 lignes, seulement valable pour une structure if / else 

age = 30 

majeur = True if age >= 18 else False

#opérateurs logiques (and, or, not)
## version normale 
password = "admin"
if user == "admin":
    if password == "admin":
        print("Access Granted")
        
## version opérateur logique 
if user == "admin" and password == "admin":
    print("Access Granted")
    
### Toutes les conditions doivent être vraies

7 > 2 and 7 < 15

### priorité au and par rapport au or
7 > 2 and  7 < 10 or 7 > 12
###  True            False => False

7 > 2 and  (7 < 10 or 7 > 12)
###True et   True  ou False => True

# Opérateur not 
## notTrue => False
## notFalse => True

if not user == "admin":
    print("Access Denied")
    
    
"""Erreurs rencontrées"""

#Erreur de syntaxe ou syntax error
 ## For i in range(10):
    ##print(i)
 ## erreur de syntaxe sur le for qui ne s'écrit pas avec une majuscule

 ##Sensibilité à la casse
  ### Oubli des 2 points
  ###for i in range(10)

 ##Mots réservés:
  ### 

  ##Oubli des guillemets
  
#Erreurs d'éxécution, runtime errors

    ##NameError : une variable non définie
    
    ##TypeError : variable non convertie en "int"  ou "str" 
    ## par exemple a ="2" + 2
     ### erreur de concaténation, on ne peut concaténer des str à des str et non des int
     
#Erreurs sémantiques 

""" Modules et Fonctions """
###############################
########## Modules ############

# Modules random ( pour générer des nbres aléatoires) et os ( pour gérer les fichiers du systeme d'exploitation)

#Module random et fonction randint

import random

nbre = random.randint(0, 1)

print("La fonct° randint = " + str(nbre)) #retourne soit 0 soit 1

# La fonction uniform

import random

nbre = random.uniform(0, 1)

print("La fonct° uniform = " + str(nbre)) # retourne un nombre décimal (float) aléatoire entre 0 et 1

# La fonction randrange

import random

nbre = random.randrange(325)

print("La fonct° randrange " + str(nbre)) # retourne un nombre aléatoire entre 0 et 324 325 étant exclu

nbre = random.randrange(0, 511, 10)

print("la fonc° randrange avec pas de 10 = " + str(nbre)) # retourne un nombre aléatoire entre 0 et 510 (511 étant exclu) avec un pas de 10  

#Module os utilisé pour créer et supprimer des dossiers

import os

chemin = "/Users/berny/formationPython"

dossier = os.path.join(chemin, "dossier", "test")

print(dossier)

#Fonction mkdir pour 1 dossier, Fonction makedirs pour 1 dossier et 1 ou plusieurs sous-dossiers

## 1ère méthode structure conditionnelle
if not os.path.exists(dossier): #si dossier n'existe pas
    
    os.makedirs(dossier)
    
## 2ème méthode 
### os.makedirs(dossier, exist_ok=True)

 #Fonction removedirs pour supprimer un dossier
if os.path.exists(dossier):
    os.removedirs(dossier)
    
#Fonctions dir et help

import random

#print(dir(random))

help(random.randint)

#Fonction pprint affiche les fonctions du module random par ordre alphabétique
from pprint import pprint

pprint(dir(random))

#Les objets "callable"

import pprint

print(callable(pprint)) #retourne False car le module pprint n'est pas appelable

from pprint import pprint 
print(callable(pprint)) #retourne True car la fonction pprint est appelable

import os
from pprint import pprint
#print(os.name())#retourne 'str' object is not callable 
print(os.name)

"""Les Listes"""

liste = [1, 2, 3, 4, 5]

print(liste[2]) #Avec indice, retourne 3

#liste = [250, "Python", True]

#print(liste[2])

# Pour définir une variable le terme 'list' est réservé, on peut utiliser 'liste' à la place

##Ajouter et enlever des éléments à une liste
###Pour ajouter 1 élément on utilise la méthode append

liste.append(6)
print(liste)
###Pour ajouter plusieurs éléments on utilise la méthode extend

liste.extend([7,8,9])
print(liste)

###Pour enlever 1 élément on utilise la méthode remove

liste.remove(9)
print(liste)

##Récupérer un élément grace à son indice

["Python", "C#", "Java"]
#indice 0    1     2
#       -3   -2   -1  indices négatifs

##slice
liste = ["Python", "C#", "Java", "JS", "Php"]

print(liste[0:3])

print(liste[1:2])

print(liste[:]) #retourne la liste intégralement

print(liste[:-1]) #exclusion du dernier indice, retourne jusqu'à l'avant dernier 

print(liste[:-2]) #exclusion du dernier indice, retourne jusqu'à l'avant-avant dernier 

print(liste[2:]) #retourne à partir de l'indice 2 jusqu'à la fin de la liste

###Avec le pas :

print(liste[::2]) #rien avant les 1ers ':' signifie qu'on part du début
#rien avant le 2ème ':' signifie qu'on va jusqu'à la fin
#le dernier nombre '2' signifie qu'on retourne un élément sur 2 dans la liste

print(liste[1::2]) #on commence à l'indice 1 et on retourne un élément sur 2 

print(liste[1:-2:2]) #on commence à l'indice 1 et on retourne un élément sur 2 en excluant les 2 derniers indices

print(liste[::-1]) #On retourne en partant du début, on va jusqu'au dernier indice ... "-1" indique que la liste est inversée

print(liste[1:-1]) #On retourne en excluant ce qu'il y a avant l'indice 1 et le dernier indice ... 

##Autres méthodes sur les listes
### Méthode index, permet de récupérer la position d'un élément dans une liste

employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"] #classés par ordre d'arrivée dans l'entreprise
resultat = employes.index("Max")
print(resultat)

###Méthode count, permet de compter le nombre d'occurence dans une liste

employes = ["Carlos", "Max", "Martine", "Patrick", "Alex", "Carlos"] #classés par ordre d'arrivée dans l'entreprise
resultat = employes.count("Carlos")
print("Carlos apparait " + str(resultat) + " fois dans la liste")

###Méthode sort, permet de trier une liste par odre alphabétique

employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"] #classés par ordre d'arrivée dans l'entreprise
resultat = employes.sort() 

print(resultat) #retourne 'None'

employes.sort() #trie directement notre liste sans passer par une variable intermédiaire pour stocker la valeur de fin
print(employes) 

#### Avec la fonction sorted(), on a besoin d'une variable pour récupérer le résultat

employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]

resultat = sorted(employes)

print(resultat)

#### la fonction reverse() agit comme sort(), pas besoin d'une variable pour récupérer le résultat. Le tri inversé se fait directement

employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]

print("L'ordre d'arrivée des employés dans l'entreprise est le suivant " + str(employes))

employes.reverse()

print("L'ordre d'arrivée inversé des employés est le suivant " + str(employes))

### Résumé : index, count, sort, sorted, reverse

#Enlever un élément de la liste grace à son index
##Méthode pop
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]

employes.pop(-1) # on enlève le dernier ou .pop(4) si on sait qu'il y a 5 éléments dans la liste

print(employes)

employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]

element = employes.pop(-1)

print("L'élément qui a été enlevé est : " + str(element))

##Pour enlever tous les éléments de la liste
#Méthode clear vide notre liste

employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]

employes.clear()

print(employes)

#Méthode join pour joindre les éléments d'une liste

liste = ["Python", "est", "un", "tout", "nouveau", "langage", "pour", "moi"]

resultat= " ".join(liste)

print(resultat)

resultat= "\n".join(liste)

print(resultat)

liste = ["Python", "est", "un", "tout", "nouveau", "langage", "pour", "moi"]

print(liste)

## Séparer une chaine de caractères
###Méthode split 

courses = "Citron, Oranges, Spiruline, Huile de Foie de Morue, Huile de Ricin, Dentifrice"


courses = courses.split(", ") 

print(courses)

#Opérateurs d'appartenance
## in, not in

users = ["Pierre", "Paul", "Jacques", "Marie"]
if "Paul" in users:
    print("Bonjour Paul, comment vas-tu ?")
    
if "Paul" in users:
    users.remove("Paul")
    print(users)
    
#Listes imbriquées


liste = ["Python", ["Java", "C++", ["C"]], ["Ruby"]]

#Pour retourner Ruby 

print (liste[2]) #retourne la liste Ruby


print(liste[1][1]) #retourne C++


print(liste[1][2]) #retourne la liste C

print(liste[1][-1]) #retourne la liste C

print(liste[1][-1][0]) #retourne C

print(liste[0][0]) #retourne P, 1er élément de Python

print(liste[1][0][0]) #retourne J, 1er élément de Java

print(liste[2][0][0]) #retourne R, 1er élément de Ruby

## Une chaine de caractères est aussi une liste :

print(liste[2][0][0:2]) #retourne Ru grâce au slice ':' qui sont les 2 premières lettres du 1er élément de Ruby

print(liste[2][0][2:4]) #retourne by grâce au slice ':' qui sont les 2 dernières lettres du 1er élément de Ruby

"""Les erreurs communes aux débutants"""

#1/les parenthèses, au lieu des crochets, utilisées pour récupérer un élément d'une liste ( ou tuple)

#2/l'utilisation directe de la valeur qu'on souhaite enlever et non de l'indice ...Par exemple liste = [3, 1, 9]  => pour enlever la valeur '3' on écrit liste.remove(3) et non liste.remove(0)
liste = [3, 1, 9, 3] 

# faux liste[0].remove()

liste.remove(3) #enlève la 1ère occurence et non le 2ème '3'

print(liste)

liste = [3, 1, 9]
#Pour enlever une valeur grace à son indice, on utilise la fonction pop ... pour enlever 3 par exemple on utilsise l'indice 0

liste.pop(0)

print(liste)

"""Les méthodes et autres fonctions utiles"""

#La diff entre méthodes et fonctions

## Une méthode est une fonction qui appartient à un objet

## fonction sorted(liste) != méthode liste.sort() , les 2 trient une liste mais

liste = [5, 3, 9, 7, 1]

sorted(liste) 
print(liste)

liste = sorted(liste) 
print(liste)

liste = [5, 3, 9, 7, 1]
liste.sort()
print(liste)

# Les objets muables et immuables (ou mutables et immutables)

## Objets Muables = listes, dictionnaires, sets

## Objets Immuables = chaines de caractères, nombres

liste.append(6) # ajoute directement 6 à la liste grace à la méthode append()car une liste est muable

print(liste)

titre = "around the world in a day".title() # on place la chaine de caractères immuable dans une variable intermédiaire sinon on ne pourra pas traiter la méthode title()

print(titre)


""" Fonctions supplémentaires """

#Fonction len
## Avec chaine de caractères

print(len("Javascript")) # retourne 10, le nombre de caractères à l'intérieur du mot Javascript

## Avec liste

print(len([1, 2 , 3])) # retourne 3, le nombre d 'éléments contenus dans la liste 

#Fonctions round, min, max

print(round(1.2)) # arrondi à 1

print(round(1.8)) # arrondi à 2


## avec nombres
print("la plus petite valeur de la liste est : " + str(min([1, 2 , 3]))) # retourne la plus petite valeur de la liste

print("la plus grande valeur de la liste est : " +  str(max([1, 2 , 3]))) # retourne la plus grande valeur de la liste

## avec chaine de caractères
print("la plus petite valeur de la liste est : " + (min("abcdz"))) # retourne la plus petite valeur de la liste

print("la plus grande valeur de la liste est : " +  (max("abcdz"))) # retourne la plus grande valeur de la liste

## Fonction sum() à n'utiliser qu'avec des listes numériques

a = sum([10, 20, 25])

print("La somme de la liste a = " + str(a))

## Fonction range() à utiliser pour les boucles 
a = 1
for loop in range(5):
    print(a)
   
    
a = 0
    
for loop in range(2, 5):
    print(a) # retourne 0 de la 2ème à la 4ème fois le nombre 5 dans la fonction range(2, 5) est exclus
    
### Exercice Mot de Passe

mdp = input("Entrez un mot de passe (min 8 caractères) : ") #alphanumérique

mdp_trop_court = "votre mot de passe est trop court."
if len(mdp) == 0: #aucun mot de passe rentré
    mdp_trop_court = mdp_trop_court.upper()
    print(mdp_trop_court)
elif len(mdp) > 0 and len(mdp) < 8:  
    mdp_trop_court = mdp_trop_court.capitalize()
    print(mdp_trop_court)
elif mdp.isdigit():
    print("Votre mot de passe ne contient que des nombres.")
else:
    print("Inscription Terminée.")
    
""" Les Boucles """
# La Boucle for 
## Répète une opération un certain nombre de fois
## Parcourt des structures de données

#for element in liste:
    #print(element)

for i in  [0, 1, 2, 3, 4, 7, 9]:
    print(i)
    
for lettre in "Python":
    print(lettre)
    
for i in range(4):
    print("Bring the noise")
    
    
# La Boucle while
## while condition:
##    print("Bonjour !")
### Une boucle while est éxécutée tant qu'une condition est vraie
### Attention aux boucles infinies

i = 0 #initialisation de la variable

while i < 4:
    print("Bring The NoiseGate !!!")
    i += 1 # Placer une limite obligatoire pour ne pas créer une boucle infinie

continuer = "o"
while continuer =="o":
    print("On continue ...")
    continuer = input("Voulez-vous continuer ? o/n ")
    


    
    
