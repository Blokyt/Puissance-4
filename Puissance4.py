
from random import *

from colored import *

import time

color1 = fg('cyan')
color2 = fg('red')
color3 = fg('green')
color4 = fg(172)
reset = attr('reset')

# logique

class Ligne():

    list_inst_ligne = []

    def __init__(self, name):
        self.name = name
        self.ligne = ["0","0","0","0","0","0","0"]
        self.list_inst_ligne.append(self)

# afficher le tableau

    def display_board():

        numéro_colonne = "|".join([f"{color4 + str(i) + reset}" for i in range(1, 8)])

        x = 1

        print(numéro_colonne)

        for inst in Ligne.list_inst_ligne:
            ligne = Ligne.list_inst_ligne[len(Ligne.list_inst_ligne)-x].ligne.copy()
            while "1" in ligne :
                ligne[ligne.index("1")] = color1+"1"+reset
            while "2" in ligne :
                ligne[ligne.index("2")] = color2+"2"+reset
            tableau = "|".join(ligne)
            print(tableau)
            x += 1

        print(numéro_colonne)

#chosir ligne

    def ia_move():

        # blocage

        for ligne in Ligne.list_inst_ligne :
            for i in range(len(ligne.ligne)-3):
                if ligne.ligne[i:i+3] == ["1"]*3 and ligne.ligne[i+3] == "0" :
                    print("debug bloque")
                    Ligne.choose_ligne_token(i+4, "2")
                    Ligne.verification_win("ia")
                    return

        # winnage

        for ligne in Ligne.list_inst_ligne :
            for i in range(len(ligne.ligne)-3):
                if ligne.ligne[i:i+3] == ["2"]*3 and ligne.ligne[i+3] == "0" :
                    print("debug win")
                    Ligne.choose_ligne_token(i+4, "2")
                    Ligne.verification_win("ia")
                    return

        # si on ne peut pas bloquer une win ou win jouer aléatoirement

        choix = randint(1,7)
        while Ligne.list_inst_ligne[len(Ligne.list_inst_ligne)-1].ligne[int(choix)-1] in ["1", "2"] :
            print("debug choix")
            choix = randint(1,7)
        else :
            Ligne.choose_ligne_token(choix, "2")
            Ligne.verification_win("ia")

    def action():
        global turn
        global running
        choix = input("\n > ")
        if choix.isdigit():
            for ligne in Ligne.list_inst_ligne :
                if Ligne.list_inst_ligne[len(Ligne.list_inst_ligne)-1].ligne[int(choix)-1] in ["1", "2"] :
                    Ligne.action()
            Ligne.choose_ligne_token(int(choix), "1")
            Ligne.verification_win("player")
        elif choix == "stop":
            running = False
            return
        else :
            Ligne.action()

# deposer jeton

    def choose_ligne_token(colonne, player):

        if colonne > 7 :
            colonne = 7
        elif colonne < 1 :
            colonne = 1

        for ligne in Ligne.list_inst_ligne :

            if ligne.ligne[colonne-1] == "1" or ligne.ligne[colonne-1] == "2" :
                pass
            else :
                ligne.ligne[colonne-1] = player
                break

# verification win

    def verification_win(player):

        Ligne.horrizontal_win(player)

        for ligne in range(len(ligne1.ligne)) :
            Ligne.win_diag(0, ligne, player)

        for ligne in range(len(ligne1.ligne)-3) :
            Ligne.win_diag(1, ligne, player)

        for ligne in range(3, len(ligne1.ligne)) :
            Ligne.win_diag(-1, ligne, player)

        Ligne.display_board()

# diagonales

    def win_diag(calc, ligne, player):
        for i in range(len(ligne1.ligne)-4):
            temp = [Ligne.list_inst_ligne[i+x].ligne[ligne+calc*x] for x in range(4)]
            if temp == ['1']*4 or temp == ['2']*4:
                Ligne.surbrillance_win(calc, i, ligne)
                Ligne.win(player)
                break

# horizontale

    def horrizontal_win(player):

        for ligne in Ligne.list_inst_ligne :
            for i in range(len(ligne.ligne)-3):
                if ligne.ligne[i:i+4] == ["1"]*4 or ligne.ligne[i:i+4] == ["2"]*4:
                    for itération in range(4) :
                        ligne.ligne[i] = color3+ligne.ligne[i]+reset
                        i +=1
                    Ligne.win(player)
                    break

# mettre en surbrillance la ligne de 4

    def surbrillance_win(lign_op, i, ligne):
        for itération in range(4) :
            Ligne.list_inst_ligne[i].ligne[ligne] = color3+Ligne.list_inst_ligne[i].ligne[ligne]+reset
            i +=1
            ligne += lign_op

# si victoire

    def win(player):
        global running
        if player == "player":
            print("\n"+color3+"     WIN"+reset+"\n")
        else :
            print("\n"+color2+"    LOOSE"+reset+"\n")
        running = False

# instansiation des lignes

ligne6 = Ligne(6)
ligne5 = Ligne(5)
ligne4 = Ligne(4)
ligne3 = Ligne(3)
ligne2 = Ligne(2)
ligne1 = Ligne(1)

running = True

# game loop
Ligne.display_board()
while running :
    if running == True :
        Ligne.action()
        if running == True :
            time.sleep(0.5)
            Ligne.ia_move()
