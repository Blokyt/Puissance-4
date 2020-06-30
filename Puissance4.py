
from random import *

from colored import *

import time

color1 = fg('cyan')
color2 = fg('red')
color3 = fg('green')
color4 = fg(172)
color5 = fg(162)
color6 = fg(17)
reset = attr('reset')

# logique

class Ligne():

    list_inst_ligne = []

    def __init__(self):
        self.ligne = ["0","0","0","0","0","0","0"]
        self.list_inst_ligne.append(self)

    def initialize_board():
        for ligne in Ligne.list_inst_ligne:
            ligne.ligne = ["0","0","0","0","0","0","0"]

# afficher le tableau

    def display_board(colonne, player, color=fg(0)):

        if player == "2":
            color = color5
        elif player == "1":
            color = color1



        print("\n"*10)
        numéro_colonne = " "+"|".join([f"{color4 + str(i) + reset}" for i in range(1, 8)])

        triangle_list = ["▾","▾","▾","▾","▾","▾","▾"]
        triangle_list[colonne-1] = color+triangle_list[colonne-1]+reset
        triangle = " "+" ".join(triangle_list)

        x = 1
        print(numéro_colonne)
        print(triangle)

        for element in Ligne.list_inst_ligne:
            ligne = Ligne.list_inst_ligne[len(Ligne.list_inst_ligne)-x].ligne.copy()
            while "1" in ligne :
                    ligne[ligne.index("1")] = color1+"1"+reset
            while "2" in ligne :
                ligne[ligne.index("2")] = color2+"2"+reset

            tableau = "|".join(ligne)

            print(" "+tableau)
            x += 1

        triangle_list = ["▴","▴","▴","▴","▴","▴","▴"]
        triangle_list[colonne-1] = color+triangle_list[colonne-1]+reset
        triangle = " "+" ".join(triangle_list)


        print(triangle)
        print(numéro_colonne)

#chosir ligne

    def ia_move():

        # verifie si l'ia peut empecher l'adversaire de gagner ou de gagner elle meme

        for win_loose in ["2","1"] :

            #horizontale devant

            for ligne in Ligne.list_inst_ligne :
                for i in range(len(ligne.ligne)-3):
                    if ligne.ligne[i:i+3] == [win_loose]*3 and ligne.ligne[i+3] == "0" :
                        Ligne.choose_ligne_token(i+4, "2")
                        return print("\ndebug : horizontale devant")

                    if ligne.ligne[i:i+3] == [win_loose]*2+["0"] and ligne.ligne[i+3] == win_loose :
                        Ligne.choose_ligne_token(i+3, "2")
                        return print("\ndebug : horizontale milieu +")

                    if ligne.ligne[i:i+3] == [win_loose]+["0"]+[win_loose] and ligne.ligne[i+3] == win_loose :
                        Ligne.choose_ligne_token(i+2, "2")
                        return print("\ndebug : horizontale milieu -")


            #horizontale derrière

                for i in range(1, len(ligne.ligne)-2):
                    if ligne.ligne[i:i+3] == [win_loose]*3 and ligne.ligne[i-1] == "0" :
                        Ligne.choose_ligne_token(i, "2")
                        return print("\ndebug : horizontale derrière")

            # verticale

            for ligne in range(len(ligne1.ligne)) :
                for i in range(len(ligne1.ligne)-4):
                    temp = [Ligne.list_inst_ligne[i+x].ligne[ligne] for x in range(3)]
                    if temp == [win_loose]*3 and Ligne.list_inst_ligne[i+3].ligne[ligne] =="0" :
                        Ligne.choose_ligne_token(ligne+1, "2")
                        return print("\ndebug : vertical")

            #diagonales

            # droite haut

            for num in [0, 1]:
                for ligne in range(num, len(ligne1.ligne)-3) :
                    for i in range(num, len(ligne1.ligne)-4):
                        temp = [Ligne.list_inst_ligne[i+x].ligne[ligne+1*x] for x in range(3)]
                        if num == 0 :
                            if temp == [win_loose]*3 and Ligne.list_inst_ligne[i+3].ligne[ligne+3] == "0":
                                Ligne.choose_ligne_token(ligne+4, "2")
                                return print("\ndebug : droite haut")

            # droite bas

                        else :
                            if temp == [win_loose]*3 and Ligne.list_inst_ligne[i-1].ligne[ligne-1] == "0":
                                Ligne.choose_ligne_token(ligne, "2")
                                return print("\ndebug : droite bas")

            # gauche haut

                for ligne in range(3,len(ligne1.ligne)-num) :
                    for i in range(num, len(ligne1.ligne)-4):
                        temp = [Ligne.list_inst_ligne[i+x].ligne[ligne-1*x] for x in range(3)]
                        if num == 0 :
                            if temp == [win_loose]*3 and Ligne.list_inst_ligne[i+3].ligne[ligne-3] == "0":
                                Ligne.choose_ligne_token(ligne-2, "2")
                                return print("\ndebug : gauche haut")

            # gauche bas

                        else :
                            if temp == [win_loose]*3 and Ligne.list_inst_ligne[i-1].ligne[ligne+1] == "0":
                                Ligne.choose_ligne_token(ligne+2, "2")
                                return print("\ndebug : gauche bas")


        # si on ne peut pas bloquer une win ou win jouer "aléatoirement"

        choix = None

        con = randint(0,6)
        if not con :
            choix = randint(3,5)
        else :
            con = randint(0,1)
            if not con :
                choix = randint(2,6)
            else :
                choix = randint(1,7)

        while Ligne.list_inst_ligne[len(Ligne.list_inst_ligne)-1].ligne[choix-1] in ["1", "2"] :
            choix = randint(1,7)
        else :
            Ligne.choose_ligne_token(choix, "2")
            return print("\ndebug : random")

    def action(joueur):
        global running, turnpass
        choix = input("\n > ")
        print(joueur)
        if choix == "ia" :
            Ligne.ia_move()
        elif choix.isdigit():
            colonne = int(choix)
            if colonne > 7 :
                colonne = 7
            elif colonne < 1 :
                colonne = 1
            for ligne in Ligne.list_inst_ligne :
                if Ligne.list_inst_ligne[len(Ligne.list_inst_ligne)-1].ligne[colonne-1] in ["1", "2"] :
                    return
            turnpass = True
            Ligne.choose_ligne_token(colonne, joueur)
            if running == True and game_mode == "2" :
                time.sleep(uniform(0.3, 1.5))
                Ligne.ia_move()
        elif choix == "back":
            running = False

        else :
            Ligne.action(joueur)

# deposer jeton

    def choose_ligne_token(colonne, player):
        for ligne in Ligne.list_inst_ligne :
            if ligne.ligne[colonne-1] == "1" or ligne.ligne[colonne-1] == "2" :
                pass
            else :
                ligne.ligne[colonne-1] = player
                break
        Ligne.verification_win(ligne.ligne[colonne-1], player)
        if running == True :
            Ligne.display_board(colonne, player)

# verification win

    def verification_win(colonne, player):

        Ligne.horrizontal_win(player)

        for ligne in range(len(ligne1.ligne)) :
            Ligne.win_diag(0, ligne, player)

        for ligne in range(len(ligne1.ligne)-3) :
            Ligne.win_diag(1, ligne, player)

        for ligne in range(3, len(ligne1.ligne)) :
            Ligne.win_diag(-1, ligne, player)



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

ligne6 = Ligne()
ligne5 = Ligne()
ligne4 = Ligne()
ligne3 = Ligne()
ligne2 = Ligne()
ligne1 = Ligne()

running = True

# game loop
player1 = "1"
player2 = "2"
game_mode = "1"
turnpass = False

def display_menu():
    print("\n"*5)
    print("\n"+color1+" 1"+reset+" : Local\n"+color1+" 2"+reset+" : Contre l'IA\n"+color1+" 3"+reset+" : Exit")
    menu()

def menu():
    global game_mode, running, turnpass, player1, player2
    game_mode = input("\n > ")
    if game_mode == "1" or game_mode == "2" :
        turnpass = False
        running = True
        player1 = "1"
        player2 = "2"
        Ligne.initialize_board()
        Ligne.display_board(4, None)
    elif game_mode == "3"  :
        running = False
    else :
        menu()

display_menu()

while running :
    if game_mode == "1" and running :
        turnpass = False
        Ligne.action(player1)
        if not running :
            display_menu()
        else :
            if turnpass :
                player1, player2  = player2, player1

    elif game_mode == "2" and running :
        Ligne.action("1")
        if not running :
            display_menu()
