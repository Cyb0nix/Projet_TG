def creer_matrice(contraintes):
    
    # Déterminer le nombre de tâches N
    N = len(contraintes)

    # Créer une matrice carrée de taille N+2 pour représenter le graphe,
    # en ajoutant les deux sommets fictifs a et w
    graphe = [[0 for j in range(N+2)] for i in range(N+2)]

    # Remplir la matrice avec les valeurs correspondantes
    for ligne in contraintes:
        tache_info = ligne.split()
        tache = int(tache_info[0])
        duree = int(tache_info[1])
        contraintes = []
        if len(tache_info) > 2:
            contraintes = list(map(int, tache_info[2:]))
        # Ajouter la tâche et ses contraintes à la matrice
        graphe[0][tache] = 0
        graphe[tache][tache] = duree
        for c in contraintes:
            graphe[c][tache] = 0
        graphe[tache][N+1] = 0

    return graphe

def afficher_matrice(matrice):
    # Afficher la matrice
    for ligne in matrice:
        print(ligne)