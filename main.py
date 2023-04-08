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
    with open("./Tables/"+nom_fichier, 'r') as f:
        for ligne in f:
            contraintes.append(ligne.strip())

    # créer la matrice correspondant au graphe et l'afficher
    graphe = Graphe(contraintes)
    graphe.afficher_matrice()

    # # vérifier si les propriétés pour un graphe d'ordonnancement sont vérifiées
    # if graphe.est_graphe_ordonnancement():  #TODO: fonction à créer - Cédric
    #     # calculer les rangs des sommets et les afficher
    #     graphe.calculer_rangs()  #TODO: fonction à créer - Arthur
    #     graphe.afficher_rangs(rangs)  #TODO: fonction à créer
        
    #     # calculer les calendriers au plus tôt et au plus tard et les afficher
    #     graphe.calculer_calendriers()  #TODO: fonction à créer - Anas
    #     graphe.afficher_calendriers()  #TODO: fonction à créer
        
    #     # calculer les marges et les afficher
    #     graphe.calculer_marges()  #TODO: fonction à créer - maximilien
    #     graphe.afficher_marges()  #TODO: fonction à créer
        
    #     # calculer le(s) chemin(s) critique(s) et les afficher
    #     graphe.trouver_chemins_critiques()  #TODO: fonction à créer - Maëlis
    #     graphe.afficher_chemins_critiques()  #TODO: fonction à créer
        
    # else:  # si les propriétés ne sont pas vérifiées
    #     # proposer à l'utilisateur de changer de tableau de contraintes
    #     print("Le graphe ne vérifie pas les propriétés pour un graphe d'ordonnancement. Veuillez choisir un autre tableau de contraintes.")


