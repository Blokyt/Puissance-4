
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
        self.lastmove = False

# afficher le tableau

    def display_board():

        print("\n"*10)

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

        for win_loose in ["1","2"] :

            for ligne in Ligne.list_inst_ligne :
                for i in range(len(ligne.ligne)-3):
                    if ligne.ligne[i:i+3] == [win_loose]*3 and ligne.ligne[i+3] == "0" :
                        Ligne.choose_ligne_token(i+4, "2")
                        return

            for ligne in range(len(ligne1.ligne)) :
                for i in range(len(ligne1.ligne)-4):
                    temp = [Ligne.list_inst_ligne[i+x].ligne[ligne] for x in range(3)]
                    if temp == [win_loose]*3 and Ligne.list_inst_ligne[i+3].ligne[ligne] =="0" :
                        Ligne.choose_ligne_token(ligne+1, "2")
                        return

            for ligne in range(len(ligne1.ligne)-3) :
                for i in range(len(ligne1.ligne)-4):
                    temp = [Ligne.list_inst_ligne[i+x].ligne[ligne+1*x] for x in range(3)]
                    if temp == [win_loose]*3 and Ligne.list_inst_ligne[i+3].ligne[ligne+1*3] == "0":
                        Ligne.choose_ligne_token(ligne+4, "2")
                        return

            for ligne in range(3, len(ligne1.ligne)) :
                for i in range(len(ligne1.ligne)-4):
                    temp = [Ligne.list_inst_ligne[i+x].ligne[ligne-1*x] for x in range(3)]
                    if temp == [win_loose]*3 and Ligne.list_inst_ligne[i+3].ligne[ligne-1*3] == "0":
                        Ligne.choose_ligne_token(ligne-2, "2")
                        return


        # si on ne peut pas bloquer une win ou win jouer aléatoirement

        choix = randint(2,6)
        while Ligne.list_inst_ligne[len(Ligne.list_inst_ligne)-1].ligne[int(choix)-1] in ["1", "2"] :
            choix = randint(1,7)
        else :
            Ligne.choose_ligne_token(choix, "2")

    def action(joueur):
        global turn
        global running
        choix = input("\n > ")
        if choix.isdigit():
            colonne = int(choix)
            if colonne > 7 :
                colonne = 7
            elif colonne < 1 :
                colonne = 1
            for ligne in Ligne.list_inst_ligne :
                if Ligne.list_inst_ligne[len(Ligne.list_inst_ligne)-1].ligne[colonne-1] in ["1", "2"] :
                    return
            Ligne.choose_ligne_token(colonne, joueur)
            if running == True and game_mode == "2" :
                time.sleep(uniform(0.3, 1.5))
                Ligne.ia_move()
        elif choix == "stop":
            running = False
            return
        else :
            pass

# deposer jeton

    def choose_ligne_token(colonne, player):

        for ligne in Ligne.list_inst_ligne :
            if ligne.ligne[colonne-1] == "1" or ligne.ligne[colonne-1] == "2" or ligne.ligne[colonne-1] == color4+player+reset  :
                pass
            else :
                ligne.ligne[colonne-1] = player
                break
        Ligne.verification_win(ligne.ligne[colonne-1], player)

# verification win

    def verification_win(colonne, player):

        Ligne.horrizontal_win(player)

        for ligne in range(len(ligne1.ligne)) :
            Ligne.win_diag(0, ligne, player)

        for ligne in range(len(ligne1.ligne)-3) :
            Ligne.win_diag(1, ligne, player)

        for ligne in range(3, len(ligne1.ligne)) :
            Ligne.win_diag(-1, ligne, player)

        if running == True :

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
        Ligne.display_board()
        global running
        if player == "1":
            print("\n"+color1+"BLUE"+reset+color3+" WIN"+reset+"\n")
        else :
            print("\n"+color2+"RED"+reset+color3+" WIN"+reset+"\n")
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

print("\n"+color1+" 1"+reset+" : Local\n"+color1+" 2"+reset+" : Contre l'IA")
game_mode = input("\n > ")
if not game_mode == "1" and not game_mode == "2" :
    running = False
else :
    Ligne.display_board()


while running :
    if game_mode == "1" and running :
        Ligne.action("1")
        if running :
            Ligne.action("2")
    elif game_mode == "2" and running :
        Ligne.action("1")
