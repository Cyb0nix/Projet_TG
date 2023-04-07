from tool import *

while True: # boucle infinie
    # demande à l'utilisateur s'il veut tester un tableau de contraintes
    decision = input("Voulez-vous tester un tableau de contraintes ? (oui/non)")
    if decision.lower() == "non":  # si l'utilisateur ne veut plus tester
        break  # sortir de la boucle

# sinon, demander à l'utilisateur de choisir un tableau de contraintes
nom_fichier = input("Choisissez le nom du fichier contenant les contraintes à traiter : ")

# lire le fichier et stocker les contraintes en mémoire
contraintes = []
with open(nom_fichier, 'r') as f:
    for ligne in f:
        contraintes.append(ligne.strip())

# créer la matrice correspondant au graphe et l'afficher
matrice = creer_matrice(contraintes)  # fonction à créer
afficher_matrice(matrice)  # fonction à créer

# vérifier si les propriétés pour un graphe d'ordonnancement sont vérifiées
if est_graphe_ordonnancement(matrice):  # fonction à créer
    # calculer les rangs des sommets et les afficher
    rangs = calculer_rangs(matrice)  # fonction à créer
    afficher_rangs(rangs)  # fonction à créer
    
    # calculer les calendriers au plus tôt et au plus tard et les afficher
    au_plus_tot, au_plus_tard = calculer_calendriers(matrice)  # fonction à créer
    afficher_calendriers(au_plus_tot, au_plus_tard)  # fonction à créer
    
    # calculer les marges et les afficher
    marges = calculer_marges(au_plus_tot, au_plus_tard)  # fonction à créer
    afficher_marges(marges)  # fonction à créer
    
    # calculer le(s) chemin(s) critique(s) et les afficher
    chemins_critiques = trouver_chemins_critiques(marges)  # fonction à créer
    afficher_chemins_critiques(chemins_critiques)  # fonction à créer
    
else:  # si les propriétés ne sont pas vérifiées
    # proposer à l'utilisateur de changer de tableau de contraintes
    print("Le graphe ne vérifie pas les propriétés pour un graphe d'ordonnancement. Veuillez choisir un autre tableau de contraintes.")


# créer la matrice correspondant au graphe et l'afficher

