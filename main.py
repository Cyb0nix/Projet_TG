from graphe import *

while True: # boucle infinie
    # demande à l'utilisateur s'il veut tester un tableau de contraintes
    decision = input("Voulez-vous tester un tableau de contraintes ? (oui/non)")
    if decision.lower() == "non":  # si l'utilisateur ne veut plus tester
        break  # sortir de la boucle

    # sinon, demander à l'utilisateur de choisir un tableau de contraintes
    nom_fichier = input("Choisir le numéro du tableau de contraintes à traiter : ")

    # lire le fichier et stocker les contraintes en mémoire
    contraintes = []
    with open("./Tables/table "+nom_fichier+".txt", 'r') as f:
        for ligne in f:
            contraintes.append(ligne.strip())
    f.close()
    

   

    # créer la matrice correspondant au graphe et l'afficheroui
    graphe = Graphe(contraintes)
    graphe.name = nom_fichier
    f = open("./Traces/trace_"+nom_fichier+".txt", "a")
    f.close()
    graphe.afficher_matrice(graphe.matrice)

    # vérifier si les propriétés pour un graphe d'ordonnancement sont vérifiées
    if graphe.est_graphe_ordonnancement():
        # calculer les rangs des sommets et les afficher
        graphe.calculer_rangs() 
        graphe.afficher_rangs()
        
        # # calculer les calendriers au plus tôt et au plus tard et les afficher
        graphe.calculer_calendriers()
        graphe.afficher_calendriers()
        
        # # # calculer les marges et les afficher
        graphe.calcul_marge()
        graphe.afficher_marge()
        
        # # calculer le(s) chemin(s) critique(s) et les afficher
        graphe.trouver_chemins_critiques()
        graphe.afficher_chemins_critiques()
        
    else:  # si les propriétés ne sont pas vérifiées
        # proposer à l'utilisateur de changer de tableau de contraintes
        print("Le graphe ne vérifie pas les propriétés pour un graphe d'ordonnancement. Veuillez choisir un autre tableau de contraintes.")


