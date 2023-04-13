import copy
class Graphe:

        def __init__(self, contraintes):

            self.N = len(contraintes)
            self.name = ""
            self.duree = {}
            self.rangs = {}
            self.arcs = 0
            self.matrice = self.creer_matrice(contraintes)
            self.dates_au_plus_tot = [0 for i in range(self.N+2)]
            self.dates_au_plus_tard = [0 for i in range(self.N+2)]
            self.marges = [0 for i in range(self.N + 2)]
            self.Chemin_critique = []


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
                    self.arcs += len(contraintes)

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

            #affichage comme un jeu de triplets
            f = open("./Traces/A5_trace_"+self.name+".txt", "a")
            print("* Création du graphe d’ordonnancement :")
            f.write("* Création du graphe d’ordonnancement :\n")
            print(str(self.N+2)+" sommets")
            f.write(str(self.N+2)+" sommets\n")
            print(str(self.arcs)+" arcs")
            f.write(str(self.arcs)+" arcs\n")
            for i in range(len(matrice)):
                for j in range(len(matrice)):
                    if matrice[i][j] != "*":
                        print(str(i)+" -> "+str(j)+" = " + str(self.duree[i]))
                        f.write(str(i)+" -> "+str(j)+" = " + str(self.duree[i])+"\n")
            print()
            f.write("\n")

            print("Matrice des valeurs")
            f.write("Matrice des valeurs\n")
            print("    ", end="")
            f.write("    ")
            for i in range(len(matrice)):
                if i < 10:
                    print(" " + str(i) + "  ", end="")
                    f.write(" " + str(i) + "  ")
                else:
                    print(str(i) + "  ", end="")
                    f.write(str(i) + "  ")

            print("\n", end='')
            f.write("\n")
            for i in range(len(matrice)):
                if i < 10:
                    print(" " + str(i) + " ", end="")
                    f.write(" " + str(i) + " ")
                else:
                    print(str(i) + " ", end="")
                    f.write(str(i) + " ")
                for j in range(len(matrice)):
                    if j < 10:
                        print("  " + str(matrice[i][j]) + " ", end="")
                        f.write("  " + str(matrice[i][j]) + " ")
                    else:
                        print("  " + str(matrice[i][j]) + " ", end="")
                        f.write("  " + str(matrice[i][j]) + " ")
                print()
                f.write("\n")
            f.close()


        def est_graphe_ordonnancement(self):
            f = open("./Traces/A5_trace_"+self.name+".txt", "a")
            # Vérifier que le graphe ne contient pas de circuit
            print("* Détection de circuit")
            f.write("* Détection de circuit\n")
            print("* Méthode d’élimination des sommets sans prédécesseurs")
            f.write("* Méthode d’élimination des sommets sans prédécesseurs\n")
            if self.contient_circuit():
                print("Le graphe contient un circuit.")
                f.write("Le graphe contient un circuit.\n")
                f.close()
                return False
            else:
                print("\nLe graphe ne contient pas de circuit.")
                f.write("\nLe graphe ne contient pas de circuit.\n")

            # Vérifier que le graphe ne contient pas d'arcs à valeur négative
            if self.contient_arcs_negatifs():
                print("Le graphe contient des arcs à valeur négative.")
                f.write("Le graphe contient des arcs à valeur négative.\n")
                f.close()
                return False
            else:
                print("Le graphe ne contient pas d'arcs à valeur négative.")
                f.write("Le graphe ne contient pas d'arcs à valeur négative.\n")

            print("\nLe graphe est un graphe d'ordonnancement.")
            f.write("\nLe graphe est un graphe d'ordonnancement.\n")
            f.close()
            return True

        #Détection de circuit avec la méthode de suppression des sommets sans prédécesseurs
        def contient_circuit(self):
            f = open("./Traces/A5_trace_"+ self.name +".txt", "a")
            # Créer une copie de la matrice
            matrice_copie = copy.deepcopy(self.matrice)

            # Tant qu'il reste des sommets dans la matrice
            while len(matrice_copie) > 0:
                # Trouver le premier sommet sans prédécesseur
                sommet = self.trouver_sommet_sans_predecesseur(matrice_copie)

                # Si aucun sommet n'a été trouvé, le graphe contient un circuit
                if sommet == None:
                    print("il n'y a plus de sommets sans predecesseur")
                    f.write("il n'y a plus de sommets sans predecesseur\n")
                    f.close()
                    return True

                # Supprimer le sommet de la matrice
                matrice_copie = self.supprimer_sommet(matrice_copie, sommet)
            f.close()
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
            f = open("./Traces/A5_trace_"+self.name+".txt", "a")
            print("\nSuppresion du sommet :",(len(self.matrice)-len(matrice_copie)))
            f.write("\nSuppresion du sommet :"+str((len(self.matrice)-len(matrice_copie)))+"\n")
            # Supprimer la ligne du sommet
            matrice_copie.pop(sommet)
            
            # Supprimer la colonne du sommet
            for i in range(len(matrice_copie)):
                matrice_copie[i].pop(sommet)
            
            # Afficher la liste des sommets restants
            print("Sommets restants :", end=" ")
            f.write("Sommets restants :")
            for i in range((len(self.matrice) - len(matrice_copie)),len(self.matrice)):
                print(i, end=" ")
                f.write(str(i)+" ")

            f.close()
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
            # Initialiser les rangs
            for i in range(self.N + 2):
                self.rangs[i] = -1

            # Sommets fictifs a et w
            self.rangs[0] = 0

            temp = []

            # Calculer les rangs des sommets
            for j in range(1, self.N + 2):
                max_rang = 0
                for i in range(self.N + 2):
                    if self.matrice[i][j] != "*":
                        # si le numéro de la colonne est plus grand que le numéro de la ligne
                        if j > i:
                            # Trouver le rang maximum des prédécesseurs du sommet i
                            max_rang = max(max_rang, self.rangs[i] + 1)
                        else:
                            # sinon ca veut dire que nous n'avons pas encore calculé le rang du sommet i
                            # ajouter la valeur du sommet dans une liste temporaire
                            # empecher d'ajouter le sommet a plusieurs reprises
                            if j not in temp:
                                temp.append(j)
                self.rangs[j] = max_rang

            # si la liste temporaire n'est pas vide
            if temp:
                # Calculer les rangs des sommets dans la liste temporaire
                for t in range(len(temp)):
                    max_range = 0
                    for i in range(self.N + 2):
                        if self.matrice[i][temp[t]] != "*":
                            # Trouver le rang maximum des prédécesseurs du sommet i
                            max_range = max(max_range, self.rangs[i] + 1)
                            self.rangs[temp[t]] = max_range

            # Trier les rangs par ordre croissant
            sorted_rangs = sorted(self.rangs, key=lambda x: (x == -1, x))
            return sorted_rangs

        # Affiche les rangs de chaque tâche
        def afficher_rangs(self):
            f = open("./Traces/A5_trace_" + self.name + ".txt", "a")
            print("\nSommet | ", end="")
            f.write("\nSommet | ")

            # trier les sommets par leur rang
            sommets_tries = sorted(range(self.N + 2), key=lambda x: self.rangs[x])

            for j in sommets_tries:  # print les taches
                if j < 10:
                    print(" " + str(j) + "  | ", end="")
                    f.write(" " + str(j) + "  | ")
                else:
                    print(str(j) + "  | ", end="")
                    f.write(str(j) + "  | ")

            print("\nRang   | ", end="")
            f.write("\nRang   | ")

            for i in sommets_tries:  # print les rangs
                if self.rangs[i] < 10:
                    print(" " + str(self.rangs[i]) + "  | ", end="")
                    f.write(" " + str(self.rangs[i]) + "  | ")
                else:
                    print(str(self.rangs[i]) + "  | ", end="")
                    f.write(str(self.rangs[i]) + "  | ")
            print("\n")
            f.write("\n")
            f.close()

        # Calculer les calendriers
        def calculer_calendriers(self):
            # Calculer les calendriers
            self.calculer_dates_au_plus_tot()
            self.calculer_dates_au_plus_tard()


        # Calculer le calendrier au plus tôt
        def calculer_dates_au_plus_tot(self):

            # Trier les sommets par ordre croissant de rangs
            sorted_nodes = sorted(range(self.N + 2), key=lambda x: self.rangs[x])

            # Calculer les dates au plus tôt en utilisant l'ordre des rangs
            for k in sorted_nodes :
                for j in range(self.N + 2):
                    for i in range(self.N + 2):
                        if self.matrice[i][j] != "*":
                            self.dates_au_plus_tot[j] = max(self.dates_au_plus_tot[j],
                                                            self.dates_au_plus_tot[i] + self.matrice[i][j])

        # Calculer le calendrier au plus tard
        def calculer_dates_au_plus_tard(self):
            # Initialisation des dates au plus tard
            for i in range(self.N+2):
                self.dates_au_plus_tard[i] = -1

            self.dates_au_plus_tard[self.N+1] = self.dates_au_plus_tot[self.N+1]

            sorted_nodes = sorted(range(self.N + 2), key=lambda x: self.rangs[x])

            for k in sorted_nodes:
                for j in range(self.N+1, 0, -1): # Parcours des colonne en ordre inverse
                    for i in range(self.N+2): # Parcours des ligne
                        if self.matrice[i][j] != '*':
                            if self.dates_au_plus_tard[i] >= 0:
                                self.dates_au_plus_tard[i] = min(self.dates_au_plus_tard[i], self.dates_au_plus_tard[j] - self.matrice[i][j])
                            else :
                                self.dates_au_plus_tard[i] = self.dates_au_plus_tard[j] - self.matrice[i][j]
        
        # Afficher les calendriers
        def afficher_calendriers(self):
            f = open("./Traces/A5_trace_" + self.name + ".txt", "a")
            print("Dates- | ", end="")
            f.write("Dates- | ")


            # Trier les sommets par ordre croissant de rangs
            sorted_nodes = sorted(range(self.N + 2), key=lambda x: self.rangs[x])

            for j in sorted_nodes:
                if self.dates_au_plus_tot[j] < 10:
                    print(" " + str(self.dates_au_plus_tot[j]) + "  | ", end="")
                    f.write(" " + str(self.dates_au_plus_tot[j]) + "  | ")
                else:
                    print(str(self.dates_au_plus_tot[j]) + "  | ", end="")
                    f.write(str(self.dates_au_plus_tot[j]) + "  | ")

            print("\nDates+ | ", end="")
            f.write("\nDates+ | ")
            for j in sorted_nodes:
                if self.dates_au_plus_tard[j] < 10:
                    print(" " + str(self.dates_au_plus_tard[j]) + "  | ", end="")
                    f.write(" " + str(self.dates_au_plus_tard[j]) + "  | ")
                else:
                    print(str(self.dates_au_plus_tard[j]) + "  | ", end="")
                    f.write(str(self.dates_au_plus_tard[j]) + "  | ")
            print()
            f.write("\n")
            f.close()

        def calcul_marge(self):
            # Calculer les marges
            for i in range(self.N + 1):
                self.marges[i] = self.dates_au_plus_tard[i] - self.dates_au_plus_tot[i]


        def afficher_marge(self):
            # Afficher les marges
            f = open("./Traces/A5_trace_"+self.name+".txt", "a")
            print("\nMarge  | ", end="")
            f.write("\nMarge  | ")

            # Trier les sommets par ordre croissant de rangs
            sorted_nodes = sorted(range(self.N + 2), key=lambda x: self.rangs[x])
            for j in sorted_nodes:
                if self.marges[j] < 10:
                    print(" "+str(self.marges[j]) + "  | ", end="")
                    f.write(" "+str(self.marges[j]) + "  | ")
                else:
                    print(str(self.marges[j]) + "  | ", end="")
                    f.write(str(self.marges[j]) + "  | ")
            print("\n")
            f.write("\n")
            f.close()


        def trouver_chemins_critiques(self):
            # Calcul des chemins critique
            for i in range(len(self.marges)):
                if self.marges[i] == 0:
                    self.Chemin_critique.append(i)

        def afficher_chemins_critiques(self):
            f = open("./Traces/A5_trace_"+self.name+".txt", "a")
            print("Le(s) chemin(s) critique(s) : ")
            f.write("Le(s) chemin(s) critique(s) : \n")

            for i in range(len(self.Chemin_critique)-1):
                print(str(self.Chemin_critique[i]) + "(" + str(self.duree[self.Chemin_critique[i]]) + ") --> ", end="")
                f.write(str(self.Chemin_critique[i]) + "(" + str(self.duree[self.Chemin_critique[i]]) + ") --> ")
            
            print(str(self.Chemin_critique[len(self.Chemin_critique)-1]), end="\n")
            f.write(str(self.Chemin_critique[len(self.Chemin_critique)-1]) + "\n")
            f.close()
