#exemple d'utilisation de la méthode format
from constants import BONJOUR

# user = input("Entrez votre nom d'utilisateur : ")
# progression = get_weekly-progress(user)

# message_de_bienvenue = BONJOUR.format(prenom=user, nombre_messages=progression)

# print(message_de_bienvenue)

##############################
######CALCULATRICE############

# from constants import RESULTAT

a = input("Entrez un premier nombre : ")
b = input("Entrez un deuxième nombre : ")
addition = f"Le résultat de l'addition de {a} et {b} est égal à {int(a) + int(b)}" # utiliser la conversion en nombre int() car la fonction input() retourne toujours une chaine de caractères
# addition = RESULTAT.format(nombre_1=nombre_1, nombre_2=nombre_2, nombre_3=nombre_3)

print(addition)

a = int(input("Entrez un premier nombre : ")) #utiliser la conversion en nombre int() car la fonction input() retourne toujours une chaine de caractères
b = int(input("Entrez un deuxième nombre : ")) #utiliser la conversion en nombre int() car la fonction input() retourne toujours une chaine de caractères

addition = f"Le résultat de l'addition de {a} et {b} est égal à {a + b}" 
# addition = RESULTAT.format(nombre_1=nombre_1, nombre_2=nombre_2, nombre_3=nombre_3)

print(addition)