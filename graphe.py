class Graphe:
    
        def __init__(self, contraintes):
            self.N = len(contraintes)
            self.duree = {}
            self.matrice = self.creer_matrice(contraintes)
    
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
    
        def afficher_matrice(self):
            print("Matrice des valeurs")
            print("    ", end="")
            for i in range(self.N+2):
                if i < 10:
                    print(" " + str(i) + "  ", end="")
                else:
                    print(str(i) + "  ", end="")
            print("\n", end='')
            for i in range(self.N+2):
                if i < 10:
                    print(" " + str(i) + " ", end="")
                else:
                    print(str(i) + " ", end="")
                for j in range(self.N+2):
                    if j < 10:
                        print("  " + str(self.matrice[i][j]) + " ", end="")
                    else:
                        print("  " + str(self.matrice[i][j]) + " ", end="")
                print()
