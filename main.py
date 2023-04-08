from graphe import *

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
    graphe = Graphe(contraintes)
    graphe.afficher_matrice()

    # # vérifier si les propriétés pour un graphe d'ordonnancement sont vérifiées
    # if est_graphe_ordonnancement(matrice):  #TODO: fonction à créer - Cédric
    #     # calculer les rangs des sommets et les afficher
    #     rangs = calculer_rangs(matrice)  #TODO: fonction à créer - Arthur
    #     afficher_rangs(rangs)  #TODO: fonction à créer
        
    #     # calculer les calendriers au plus tôt et au plus tard et les afficher
    #     au_plus_tot, au_plus_tard = calculer_calendriers(matrice)  #TODO: fonction à créer - Anas
    #     afficher_calendriers(au_plus_tot, au_plus_tard)  #TODO: fonction à créer
        
    #     # calculer les marges et les afficher
    #     marges = calculer_marges(au_plus_tot, au_plus_tard)  #TODO: fonction à créer - maximilien
    #     afficher_marges(marges)  #TODO: fonction à créer
        
    #     # calculer le(s) chemin(s) critique(s) et les afficher
    #     chemins_critiques = trouver_chemins_critiques(marges)  #TODO: fonction à créer - Maëlis
    #     afficher_chemins_critiques(chemins_critiques)  #TODO: fonction à créer
        
    # else:  # si les propriétés ne sont pas vérifiées
    #     # proposer à l'utilisateur de changer de tableau de contraintes
    #     print("Le graphe ne vérifie pas les propriétés pour un graphe d'ordonnancement. Veuillez choisir un autre tableau de contraintes.")


