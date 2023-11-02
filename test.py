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

number = input("Entrez un nombre :")
print(number)

print(type(number))

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
    print(str(i).zfill(2))    