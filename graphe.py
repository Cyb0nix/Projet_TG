import copy
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
            cptRang = 0

            for j in range(self.N + 2): # Pour chaque colonne
                for i in range(self.N + 2): # Pour chaque ligne
                    if self.matrice[i][j] != '*': 
                        cptRang += 1       
                self.rangs[j] = cptRang # On ajoute le rang de la tâche j
                cptRang = 0
            return self.rangs

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
            print("\n")
            
            
            
            
            
def date_au_plus_tot(rang, edges, task_durations):

    date_plus_tot = []

    for i in range(len(rang)):
        add = []
        if i == 0:
            add.append(int(rang[i].split(',')[1]))  
            add.append(int(rang[i].split(',')[0])) 
            add.append("--")  
            add.append(0)  
            date_plus_tot.append(add)
        else:
            predecessors = []
            for edge in edges:
                if edge[1] == int(rang[i].split(',')[0]):
                    predecessors.append(str(edge[0]) + "->" + str(edge[1]))
            if len(predecessors) == 1:
                if predecessors[0].split("->")[0] != "0":
                    duration = task_durations[int(predecessors[0].split("->")[0]) - 1]
                else:
                    duration = 0
                for u in date_plus_tot:
                    if u[1] == int(predecessors[0].split("->")[0]):
                        somme = int(u[-1]) + duration
                add = []
                add.append(int(rang[i].split(',')[1]))  
                add.append(int(rang[i].split(',')[0]))  
                add.append(predecessors)  # Successeur
                add.append(somme)  # Dates par Successeur
                date_plus_tot.append(add)

            else:
                compare_dates = []
                for x in range(len(predecessors)):
                    if int(predecessors[x].split("->")[0]) != 0:
                        duration = task_durations[int(predecessors[x].split("->")[0]) - 1]
                    else:
                        duration = 0
                    for u in date_plus_tot:
                        if u[1] == int(predecessors[x].split("->")[0]):
                            somme = int(u[-1]) + duration
                            duration = 0
                    compare_dates.append(somme)

                maxi = max(compare_dates)

                add = []
                add.append(int(rang[i].split(',')[1]))  
                add.append(int(rang[i].split(',')[0]))  
                add.append(predecessors) 
                add.append(maxi)  
                date_plus_tot.append(add)

    return date_plus_tot





    def date_au_plus_tard(rang, triplets, task_duration, date_tot):
    # inverser le rang et date_tot
    rang_inverse = rang[::-1]
    date_tot_inverse = date_tot[::-1]
    date_plus_tard = []

    for i, r in enumerate(rang_inverse):
        add = [int(r.split(',')[1]), int(r.split(',')[0]), "--"]

        # Trouver les successeurs de la tÃ¢che
        successeur = [f"{t[0]}->{t[1]}" for t in triplets if t[0] == add[1]]

        if len(successeur) == 1:
            duration = task_duration[int(successeur[0].split("->")[0]) - 1] if int(successeur[0].split("->")[0]) != 0 else 0
            date_successeur = next(d[-1] for d in date_plus_tard if d[1] == int(successeur[0].split("->")[1]))
            diff = date_successeur - duration
            add += [diff]
        else:
            compare_date = []
            for s in successeur:
                duration = task_duration[int(s.split("->")[0]) - 1] if int(s.split("->")[0]) != 0 else 0
                date_successeur = next(d[-1] for d in date_plus_tard if d[1] == int(s.split("->")[1]))
                diff = date_successeur - duration
                compare_date.append(diff)
            mini = min(compare_date)
            add += [mini]

        date_plus_tard.append(add)

    # inverser date_plus_tard et remettre la structure originale
    date_plus_tard = date_plus_tard[::-1]
    date_plus_tard = [[d[0], d[1], d[2], date_tot_inverse[i][-1], d[3]] for i, d in enumerate(date_plus_tard)]

    return date_plus_tard
