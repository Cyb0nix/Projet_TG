class Graphe:
    
        def __init__(self, contraintes):
            self.N = len(contraintes)
            self.duree = {}
            self.rangs = {}
            self.matrice = self.creer_matrice(contraintes)
    
        # Créer la matrice des valeurs à partir des contraintes
        def creer_matrice(self, contraintes):
            # Créer une matrice carrée de taille N+2 pour représenter le graphe,
            # en ajoutant les deux sommets fictifs a et w
            self.N = len(contraintes)
            matrice = [["*" for j in range(self.N+2)] for i in range(self.N+2)]
    
            # Remplir la matrice avec les valeurs correspondantes
            for ligne in contraintes:
                tache_info = ligne.split()
                tache = int(tache_info[0])
                duree = int(tache_info[1])
                self.duree[tache] = duree
            
            for ligne in contraintes:
                contraintes = []
                tache_info = ligne.split()
                tache = int(tache_info[0])
                if len(tache_info) > 2:
                    contraintes = list(map(int, tache_info[2:]))
                if contraintes == []:
                    matrice[0][tache] = 0
                else:
                    for c in contraintes:
                        matrice[c][tache] = self.duree[c]
    
            return matrice
    
        # Afficher la matrice des valeurs
        def afficher_matrice(self):
            print("Matrice des valeurs")
            print("    ", end="")
            
            for i in range(self.N+1): # affichage des numéros de colonne
                if i < 10:
                    print(" " + str(i) + "  ", end="")
                else:
                    print(str(i) + "  ", end="")
            
            print("\n", end='')

            for i in range(self.N+1): # affichage des numéros de ligne
                if i < 10:
                    print(" " + str(i) + " ", end="")
                else:
                    print(str(i) + " ", end="")

                for j in range(self.N+1): # affichage des valeurs
                    if j < 10:
                        print("  " + str(self.matrice[i][j]) + " ", end="")
                    else:
                        print("  " + str(self.matrice[i][j]) + " ", end="")
                print()

        # Calculer les rangs de chaque tâche
        def calculer_rangs(self):
            cptRang = 0

            for j in range(self.N + 1): # Pour chaque colonne
                for i in range(self.N + 1): # Pour chaque ligne
                    if self.matrice[i][j] != '*': 
                        cptRang += 1       
                self.rangs[j] = cptRang # On ajoute le rang de la tâche j
                cptRang = 0
            return self.rangs

        # Affiche les rangs de chaque tâche
        def afficher_rangs(self):
            print("\nEtat  | ", end="")

            for j in range(self.N + 1): # print les taches
                print(str(j) + " | ", end="")

            print("\nRang  | ", end="")

            for j in range(self.N + 1): # print les rangs
                if j >= 10:
                    print(" " + str(self.rangs[j]) + " | ", end="")
                else:
                    print(str(self.rangs[j]) + " | ", end="")
            print("\n")