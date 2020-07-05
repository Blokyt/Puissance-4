
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

class Ligne():

    list_inst_ligne = []

    def __init__(self):
        self.ligne = []
        self.list_inst_ligne.append(self)

class Menu():

    # affiche les différents game_mode

    def display_menu():
        print("\n"*3)
        print("\n"+color1+" 1"+reset+" : Local\n"+color1+" 2"+reset+" : Contre l'IA\n"+color1+" 3"+reset+" : IA VS IA\n"+color1+" 4"+reset+" : Exit")
        Menu.menu()

    # choix du mode

    def menu():
        global game_mode, running, turnpass, player1, player2, ia
        game_mode = input("\n > ")
        if game_mode == "1" or game_mode == "2" or game_mode == "3" :
            turnpass = False
            running = True
            ia1 = "1"
            ia2 = "2"
            player1 = "1"
            player2 = "2"
            Board.initialize_board()
            Board.display_board(4, None)
        elif game_mode == "4"  :
            running = False
        else :
            Menu.menu()

class Board():

    # reinitialise chaque ligne

    def initialize_board():
        for ligne in Ligne.list_inst_ligne:
            ligne.ligne = ["0","0","0","0","0","0","0"]

    def display_board(colonne, player, color=fg(0)):

        # permet d'indiquer ou et qui à jouer le dernier coup

        if player == "2":
            color = color5
        elif player == "1":
            color = color1

        # affichage des lignes

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

class Ia():

    def ia_move(ia):
        # verifie si l'ia peut empecher l'adversaire de gagner ou de gagner elle meme ou autre
        for win_loose in ["2","1"] :
            #horizontale devant
            for hauteur in range(len(ligne1.ligne)-1):
                for i in range(len(ligne1.ligne)-3):
                    temp = Ligne.list_inst_ligne[hauteur].ligne[i:i+4]
                    if hauteur > 1 :
                        if temp == [win_loose]*3+["0"] and Ligne.list_inst_ligne[hauteur-2].ligne[i+3] == "0" or temp == [win_loose]*3+["0"] and not Ligne.list_inst_ligne[hauteur-1].ligne[i+3] == "0" :
                            Token.place_token(i+4, ia)
                            return print("\ndebug : horizontale devant haut")

                        if temp == ["0"]+[win_loose]*3 and Ligne.list_inst_ligne[hauteur-2].ligne[i] == "0" or temp == ["0"]+[win_loose]*3 and not Ligne.list_inst_ligne[hauteur-1].ligne[i] == "0":
                            Token.place_token(i+1, ia)
                            return print("\ndebug : horizontale derrière haut")

                        if temp == [win_loose]*2+["0"]+[win_loose] and Ligne.list_inst_ligne[hauteur-2].ligne[i+2] == "0" or temp == [win_loose]*2+["0"]+[win_loose] and not Ligne.list_inst_ligne[hauteur-1].ligne[i+2] == "0" :
                            Token.place_token(i+3, ia)
                            return print("\ndebug : horizontale milieu + haut")

                        if temp == [win_loose]+["0"]+[win_loose]*2 and Ligne.list_inst_ligne[hauteur-2].ligne[i+1] == "0" or temp == [win_loose]+["0"]+[win_loose]*2 and not Ligne.list_inst_ligne[hauteur-1].ligne[i+1] == "0" :
                            Token.place_token(i+2, ia)
                            return print("\ndebug : horizontale milieu - haut")

                    if hauteur == 1 :
                        if temp == [win_loose]*3+["0"] and not Ligne.list_inst_ligne[hauteur-1].ligne[i+3] == "0" :
                            Token.place_token(i+4, ia)
                            return print("\ndebug : horizontale devant middle")

                        if temp == ["0"]+[win_loose]*3 and not Ligne.list_inst_ligne[hauteur-1].ligne[i] == "0" :
                            Token.place_token(i+1, ia)
                            return print("\ndebug : horizontale derrière middle")

                        if temp == [win_loose]*2+["0"]+[win_loose] and not Ligne.list_inst_ligne[hauteur-1].ligne[i+2] == "0" :
                            Token.place_token(i+3, ia)
                            return print("\ndebug : horizontale milieu + middle")

                        if temp == [win_loose]+["0"]+[win_loose]*2 and not Ligne.list_inst_ligne[hauteur-1].ligne[i+1] == "0" :
                            Token.place_token(i+2, ia)
                            return print("\ndebug : horizontale milieu - middle")

                    elif hauteur == 0 :
                        if temp == [win_loose]*3+["0"] :
                            Token.place_token(i+4, ia)
                            return print("\ndebug : horizontale devant bas")

                        if temp == ["0"]+[win_loose]*3 :
                            Token.place_token(i+1, ia)
                            return print("\ndebug : horizontale derrière bas")

                        if temp == [win_loose]*2+["0"]+[win_loose]:
                            Token.place_token(i+3, ia)
                            return print("\ndebug : horizontale milieu + bas")

                        if temp == [win_loose]+["0"]+[win_loose]*2 :
                            Token.place_token(i+2, ia)
                            return print("\ndebug : horizontale milieu - bas")

                # verticale

            for ligne in range(len(ligne1.ligne)) :
                for i in range(len(ligne1.ligne)-4) :
                    temp = [Ligne.list_inst_ligne[i+x].ligne[ligne] for x in range(4)]
                    if temp == [win_loose]*3+["0"] :
                        Token.place_token(ligne+1, ia)
                        return print("\ndebug : vertical")

                #diagonales

                # droite haut

            for ligne in range(len(ligne1.ligne)-3) :
                for i in range(len(ligne1.ligne)-4):
                    temp = [Ligne.list_inst_ligne[i+x].ligne[ligne+1*x] for x in range(4)]
                    if temp == [win_loose]*3+["0"] and Ligne.list_inst_ligne[i+1].ligne[ligne+3] == "0" or temp == [win_loose]*3+["0"] and not Ligne.list_inst_ligne[i+2].ligne[ligne+3] == "0" :
                        Token.place_token(ligne+4, ia)
                        return print("\ndebug : droite haut")

                    if temp == [win_loose]*2+["0"]+[win_loose] and Ligne.list_inst_ligne[i].ligne[ligne+2] == "0" or temp == [win_loose]*2+["0"]+[win_loose] and not Ligne.list_inst_ligne[i+1].ligne[ligne+2] == "0" :
                        Token.place_token(ligne+3, ia)
                        return print("\ndebug : droite middle +")
                        # droite bas

                    if temp == ["0"]+[win_loose]*3 :
                        Token.place_token(ligne+1, ia)
                        return print("\ndebug : droite bas")

                    if temp == [win_loose]+["0"]+[win_loose]*2 :
                        Token.place_token(ligne+2, ia)
                        return print("\ndebug : droite middle -")

                # gauche haut

            for ligne in range(3,len(ligne1.ligne)) :
                for i in range(len(ligne1.ligne)-4):
                    temp = [Ligne.list_inst_ligne[i+x].ligne[ligne-1*x] for x in range(4)]
                    if temp == [win_loose]*3+["0"] and Ligne.list_inst_ligne[i+1].ligne[ligne-3] == "0" or temp == [win_loose]*3+["0"] and not Ligne.list_inst_ligne[i+2].ligne[ligne-3] == "0" :
                        Token.place_token(ligne-2, ia)
                        return print("\ndebug : gauche haut")

                    if temp == [win_loose]*2+["0"]+[win_loose] and Ligne.list_inst_ligne[i].ligne[ligne-2] == "0" or temp == [win_loose]*2+["0"]+[win_loose] and not Ligne.list_inst_ligne[i+1].ligne[ligne-2] == "0" :
                        Token.place_token(ligne-1, ia)
                        return print("\ndebug : gauche middle +")

                        # gauche bas

                    if temp == ["0"]+[win_loose]*3 :
                        Token.place_token(ligne+1, ia)
                        return print("\ndebug : gauche bas")

                    if temp == [win_loose]+["0"]+[win_loose]*2 :
                        Token.place_token(ligne, ia)
                        return print("\ndebug : gauche middle -")

            # si on ne peut pas bloquer une win ou win jouer "aléatoirement"

        for win_loose in ["2","1"] :
            for hauteur in range(1, 4):
                for i in range(len(ligne1.ligne)-2):
                    temp = Ligne.list_inst_ligne[hauteur-1].ligne[i:i+3]
                    if temp == ["0"]+[win_loose]+["0"] :
                        if i+2 < 4 :
                            Token.place_token(i+3, ia)
                            return print("\ndebug : nexto right")
                        elif i+2 > 4 :
                            Token.place_token(i+1, ia)
                            return print("\ndebug : nexto left")

        choix = randint(1,7)

        while Ligne.list_inst_ligne[len(Ligne.list_inst_ligne)-1].ligne[choix-1] in ["1", "2"] :
            choix = randint(1,7)
        else :
            Token.place_token(choix, ia)
            return print("\ndebug : random")

class User():

    def user_move(joueur):
        global running, game_mode, player1, player2
        if running == True :
            choix = input("\n > ")
            print(joueur)
            if choix == "ia" :
                Ia.ia_move(joueur)
            elif choix.isdigit():
                colonne = int(choix)
                if colonne > 7 :
                    colonne = 7
                elif colonne < 1 :
                    colonne = 1
                for ligne in Ligne.list_inst_ligne :
                    if ligne1.ligne[colonne-1] in ["1", "2"] :
                        return
                player1, player2  = player2, player1

                Token.place_token(colonne, joueur)

            elif choix == "back":
                running = False

            else :
                User.user_move(joueur)

class Token():

    def place_token(colonne, player):

        for ligne in Ligne.list_inst_ligne :
            if ligne.ligne[colonne-1] in ["1","2"] :
                pass
            else :
                ligne.ligne[colonne-1] = player
                break
        Win_condition.is_win(colonne, player)
        if running == True :
            Board.display_board(colonne, player)

class Win_condition():

        # verification win

        def is_win(colonne, player):

            Win_condition.draw()

            Win_condition.horrizontal(player, colonne)

            for ligne in range(len(ligne1.ligne)) :
                Win_condition.diag(0, ligne, player, colonne)

            for ligne in range(len(ligne1.ligne)-3) :
                Win_condition.diag(1, ligne, player, colonne)

            for ligne in range(3, len(ligne1.ligne)) :
                Win_condition.diag(-1, ligne, player, colonne)

        # diagonale

        def diag(calc, ligne, player, colonne):
            for i in range(len(ligne1.ligne)-4):
                temp = [Ligne.list_inst_ligne[i+x].ligne[ligne+calc*x] for x in range(4)]
                if temp == ['1']*4 or temp == ['2']*4:
                    Win_condition.light_diag(calc, i, ligne)
                    Win_condition.win(player, colonne)
                    break

        # horizontale

        def horrizontal(player, colonne):

            for ligne in Ligne.list_inst_ligne :
                for i in range(len(ligne.ligne)-3):
                    if ligne.ligne[i:i+4] == ["1"]*4 or ligne.ligne[i:i+4] == ["2"]*4:

                        # light horizontal

                        for itération in range(4) :
                            ligne.ligne[i] = color3+ligne.ligne[i]+reset
                            i +=1

                        Win_condition.win(player, colonne)

                        break

        # mettre en surbrillance la diag de 4

        def light_diag(lign_op, i, ligne):
            for token in range(4) :
                Ligne.list_inst_ligne[i].ligne[ligne] = color3+Ligne.list_inst_ligne[i].ligne[ligne]+reset
                i +=1
                ligne += lign_op

        # si victoire

        def win(player, colonne):
            Board.display_board(colonne, player)
            global running
            if player == "1":
                print("\n"+color1+"BLUE"+reset+color3+" WIN"+reset+"\n")
            else :
                print("\n"+color2+"RED"+reset+color3+" WIN"+reset+"\n")
            running = False
            input("\n > ")

        # si égalité

        def draw():
            global running
            if "0" in ligne1.ligne :
                return
            else :
                print("\n"+color3+" DRAW"+reset+"\n")
                running = False
                input("\n > ")

# instansiation des lignes

ligne6 = Ligne()
ligne5 = Ligne()
ligne4 = Ligne()
ligne3 = Ligne()
ligne2 = Ligne()
ligne1 = Ligne()

# initialisation des variables

running = True
player1 = "1"
player2 = "2"
game_mode = "1"
ia1 = "1"
ia2 = "2"

# Entrer dans la game loop

Menu.display_menu()

# game loop

while running :

    # local

    if game_mode == "1" and running :
        User.user_move(player1)
        if not running :
            Menu.display_menu()
    # vs ia

    elif game_mode == "2" and running :
        Win_condition.draw()
        User.user_move(player1)
        if not running :
            Menu.display_menu()
        else :
            Win_condition.draw()
            time.sleep(uniform(0.5, 1.5))
            Ia.ia_move("2")
            if not running :
                Menu.display_menu()

    # ia vs ia

    elif game_mode == "3" and running :
        Win_condition.draw()
        time.sleep(uniform(0.5, 1.5))
        Ia.ia_move(ia1)
        ia1, ia2 = ia2, ia1
        if not running :
            Menu.display_menu()
