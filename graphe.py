import copy
class Graphe:
    
        def __init__(self, contraintes):
            self.N = len(contraintes)
            self.duree = {}
            self.rangs = {}
            self.matrice = self.creer_matrice(contraintes)
            self.dates_au_plus_tot = [0 for i in range(self.N+2)]
            self.dates_au_plus_tard = [0 for i in range(self.N+2)]
    
        # Créer la matrice des valeurs à partir des contraintes
        def creer_matrice(self, contraintes):
            # Créer une matrice carrée de taille N+2 pour représenter le graphe,
            # en ajoutant les deux sommets fictifs a et w
         
            matrice = [["*" for j in range(self.N+2)] for i in range(self.N+2)]
 
    
            # Remplir la matrice avec les valeurs correspondantes
            for ligne in contraintes:
                tache_info = ligne.split()
                tache = int(tache_info[0])
                duree = int(tache_info[1])
                self.duree[0] = 0
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
            
            for i in range(len(matrice)):
                for j in range(len(matrice)):
                    #vérifie si le sommet est un sommet final si le sommet est un sommet final et que ce n'est pas le sommet w, on le relie au sommet w avec la durée de la tache
                    if matrice[i][j] != "*":
                        break
                    else:
                        #si le sommet est un sommet final et que ce n'est pas le sommet w, on le relie au sommet w avec la durée de la tache
                        if j == len(matrice)-1 and i != len(matrice)-1:
                            matrice[i][j] = self.duree[i]
    
            return matrice
    
        def afficher_matrice(self,matrice):
            print("Matrice des valeurs")
            print("    ", end="")
            for i in range(len(matrice)):
                if i < 10:
                    print(" " + str(i) + "  ", end="")
                else:
                    print(str(i) + "  ", end="")
            
            print("\n", end='')
            for i in range(len(matrice)):
                if i < 10:
                    print(" " + str(i) + " ", end="")
                else:
                    print(str(i) + " ", end="")
                for j in range(len(matrice)):
                    if j < 10:
                        print("  " + str(matrice[i][j]) + " ", end="")
                    else:
                        print("  " + str(matrice[i][j]) + " ", end="")
                print()


        def est_graphe_ordonnancement(self):
            # Vérifier que le graphe ne contient pas de circuit
            
    
            if self.contient_circuit():
                print("Le graphe contient un circuit.")
                return False
            
            
            # Vérifier que le graphe ne contient pas d'arcs à valeur négative
            if self.contient_arcs_negatifs():
                print("Le graphe contient des arcs à valeur négative.")
                return False

            print("Le graphe est un graphe d'ordonnancement.")
            return True
        
        #Détection de circuit avec la méthide de suppression des sommets sans prédécesseurs
        def contient_circuit(self):
            # Créer une copie de la matrice
            matrice_copie = copy.deepcopy(self.matrice)
           
            # Tant qu'il reste des sommets dans la matrice
            while len(matrice_copie) > 0:
                # Trouver le premier sommet sans prédécesseur
                sommet = self.trouver_sommet_sans_predecesseur(matrice_copie)
    
                # Si aucun sommet n'a été trouvé, le graphe contient un circuit
                if sommet == None:
                    print("il n'y a plus de sommets sans predecesseur")
                    return True
    
                # Supprimer le sommet de la matrice
                matrice_copie = self.supprimer_sommet(matrice_copie, sommet)

            return False
        
        def trouver_sommet_sans_predecesseur(self, matrice_copie):
            for i in range(len(matrice_copie)):
                for j in range(len(matrice_copie)):
                    # Si le sommet a un prédécesseur, passer au sommet suivant
                    if matrice_copie[j][i] != "*":
                        break
                    else:
                        # Si le sommet n'a pas de prédécesseur, le retourner
                        if j == len(matrice_copie) - 1:
                            return i
            return None
        
        def supprimer_sommet(self, matrice_copie, sommet):

            print("Suppresion du sommet :",(len(self.matrice)-len(matrice_copie)))
            # Supprimer la ligne du sommet
            matrice_copie.pop(sommet)
            
            # Supprimer la colonne du sommet
            for i in range(len(matrice_copie)):
                matrice_copie[i].pop(sommet)
            return matrice_copie
        
            
        def contient_arcs_negatifs(self):
            
            # Vérifier que chaque arc a une valeur positive
            for i in range(len(self.matrice)):
                for j in range(len(self.matrice)):
                    if self.matrice[i][j] != "*" and self.matrice[i][j] < 0:
                        return True
            return False

        # Calculer les rangs de chaque tâche
        def calculer_rangs(self):
            # Créer une copie de la matrice
            matrice_copie = copy.deepcopy(self.matrice)
            rangs = [0] * len(matrice_copie)
            rang = 0

            # Tant qu'il reste des sommets dans la matrice
            while len(matrice_copie) > 0:
                # Trouver le premier sommet sans prédécesseur
                sommet = self.trouver_sommet_sans_predecesseur(matrice_copie)

                # Si aucun sommet n'a été trouvé, le graphe contient un circuit
                if sommet == None:
                    print("il n'y a plus de sommets sans predecesseur")
                    return True

                # Supprimer le sommet de la matrice
                matrice_copie = self.supprimer_sommet(matrice_copie, sommet)
                rangs[sommet] = rang
                rang += 1

            self.rangs = rangs
            

        # Affiche les rangs de chaque tâche
        def afficher_rangs(self):
            print("\nEtat  | ", end="")

            for j in range(self.N + 2): # print les taches
                print(str(j) + " | ", end="")

            print("\nRang  | ", end="")

            for j in range(self.N + 2): # print les rangs
                if j >= 10:
                    print(" " + str(self.rangs[j]) + " | ", end="")
                else:
                    print(str(self.rangs[j]) + " | ", end="")
            
            
            
        def calculer_calendriers(self):
            
            
            # Calculer les calendriers
            self.calculer_dates_au_plus_tot()
            # self.calculer_dates_au_plus_tard()


        
        def calculer_dates_au_plus_tot(self):
            #calculer dates au plus tot
            for j in range(self.N + 2): # Pour chaque colonne
                for i in range(self.N + 2): # Pour chaque ligne
                    if self.matrice[i][j] != '*':
                        self.dates_au_plus_tot[j] = max(self.dates_au_plus_tot[j], self.dates_au_plus_tot[i] + self.matrice[i][j])

        
        # def calculer_dates_au_plus_tard(self):
        #     #TODO






            
            
            
        
        



                        
        
        
        def afficher_calendriers(self):
            print("\nDates-| ", end="")
            for j in range(self.N + 2):
                if j < 10:
                    print(str(self.dates_au_plus_tot[j]) + " | ", end="")
                else:
                    print(str(self.dates_au_plus_tot[j]) + " | ", end="")

            print("\nDates+| ", end="")
            for j in range(self.N + 2):
                if j < 10:
                    print(str(self.dates_au_plus_tard[j]) + " | ", end="")
                else:
                    print(str(self.dates_au_plus_tard[j]) + " | ", end="")
            print("\n")




