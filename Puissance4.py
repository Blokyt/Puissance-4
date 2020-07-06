
# module

from random import *

import time

from colored import *

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
        global game_mode, running, turnpass, player1, player2
        game_mode = input("\n > ")
        if game_mode == "1" or game_mode == "2" or game_mode == "3" :
            running = True
            player1 = p1symb
            player2 = p2symb
            Board.initialize_board()
            Board.display_board(token_width, None, 0.1)
        elif game_mode == "4"  :
            running = False
        else :
            Menu.menu()

class Board():

    # reinitialise chaque ligne

    def initialize_board():
        for ligne in Ligne.list_inst_ligne:
            ligne.ligne = ["0"]*token_width

    def display_board(colonne, player, startime=0.025, color=""):

        # permet d'indiquer ou et qui à jouer le dernier coup

        if player == "2":
            color = color5
        elif player == "1":
            color = color1

        # affichage des lignes

        print("\n"*10)
        numéro_colonne = " "+"|".join([f"{color4 + str(i+1) + reset}" for i in range(token_width)])


        triangle_list = []
        for colonnes in range(token_width):
            triangle_list.append("▾")
        triangle_list[colonne-1] = color+triangle_list[colonne-1]+reset
        triangle = " "+" ".join(triangle_list)

        x = 1
        time.sleep(startime)
        print(numéro_colonne)
        time.sleep(startime)
        print(triangle)

        for element in Ligne.list_inst_ligne:
            ligne = Ligne.list_inst_ligne[len(Ligne.list_inst_ligne)-x].ligne.copy()
            while p1symb in ligne :
                    ligne[ligne.index(p1symb)] = color1+p1symb+reset
            while p2symb in ligne :
                ligne[ligne.index(p2symb)] = color2+p2symb+reset

            tableau = "|".join(ligne)
            time.sleep(startime)
            print(" "+tableau)
            x += 1

        triangle_list = []
        for colonnes in range(token_width):
            triangle_list.append("▴")
        triangle_list[colonne-1] = color+triangle_list[colonne-1]+reset
        triangle = " "+" ".join(triangle_list)

        time.sleep(startime)
        print(triangle)
        time.sleep(startime)
        print(numéro_colonne)

class Ia():

    def ia_move(ia):
        # verifie si l'ia peut empecher l'adversaire de gagner ou de gagner elle meme ou autre
        for win_loose in [p2symb,p1symb] :
            #horizontale devant
            for hauteur in range(token_height):
                for i in range((token_width+1)-token_win):
                    temp = Ligne.list_inst_ligne[hauteur].ligne[i:i+token_win]
                    if hauteur > 1 :
                        if temp == [win_loose]*(token_win-1)+[emptysymb] and Ligne.list_inst_ligne[hauteur-2].ligne[i+token_win-1] == emptysymb or temp == [win_loose]*(token_win-1)+[emptysymb] and not Ligne.list_inst_ligne[hauteur-1].ligne[i+token_win-1] == emptysymb :
                            Token.place_token(i+token_win, ia)
                            return print("\ndebug : horizontale devant haut")

                        if temp == [emptysymb]+[win_loose]*(token_win-1) and Ligne.list_inst_ligne[hauteur-2].ligne[i] == emptysymb or temp == [emptysymb]+[win_loose]*(token_win-1) and not Ligne.list_inst_ligne[hauteur-1].ligne[i] == emptysymb:
                            Token.place_token(i+1, ia)
                            return print("\ndebug : horizontale derrière haut")

                        if temp == [win_loose]*(token_win-2)+[emptysymb]+[win_loose] and Ligne.list_inst_ligne[hauteur-2].ligne[i+token_win-2] == emptysymb or temp == [win_loose]*(token_win-2)+[emptysymb]+[win_loose] and not Ligne.list_inst_ligne[hauteur-1].ligne[i+token_win-2] == emptysymb :
                            Token.place_token(i+(token_win-1), ia)
                            return print("\ndebug : horizontale milieu + haut")

                        if temp == [win_loose]+[emptysymb]+[win_loose]*(token_win-2) and Ligne.list_inst_ligne[hauteur-2].ligne[i+1] == emptysymb or temp == [win_loose]+[emptysymb]+[win_loose]*(token_win-2) and not Ligne.list_inst_ligne[hauteur-1].ligne[i+1] == emptysymb :
                            Token.place_token(i+2, ia)
                            return print("\ndebug : horizontale milieu - haut")

                    if hauteur == 1 :
                        if temp == [win_loose]*(token_win-1)+[emptysymb] and not Ligne.list_inst_ligne[hauteur-1].ligne[i+(token_win-1)] == emptysymb :
                            Token.place_token(i+token_win, ia)
                            return print("\ndebug : horizontale devant middle")

                        if temp == [emptysymb]+[win_loose]*(token_win-2) and not Ligne.list_inst_ligne[hauteur-1].ligne[i] == emptysymb :
                            Token.place_token(i+1, ia)
                            return print("\ndebug : horizontale derrière middle")

                        if temp == [win_loose]*(token_win-2)+[emptysymb]+[win_loose] and not Ligne.list_inst_ligne[hauteur-1].ligne[i+(token_win-2)] == emptysymb :
                            Token.place_token(i+(token_win-1), ia)
                            return print("\ndebug : horizontale milieu + middle")

                        if temp == [win_loose]+[emptysymb]+[win_loose]*(token_win-2) and not Ligne.list_inst_ligne[hauteur-1].ligne[i+1] == emptysymb :
                            Token.place_token(i+2, ia)
                            return print("\ndebug : horizontale milieu - middle")

                    elif hauteur == 0 :
                        if temp == [win_loose]*(token_win-1)+[emptysymb] :
                            Token.place_token(i+token_win, ia)
                            return print("\ndebug : horizontale devant bas")

                        if temp == [emptysymb]+[win_loose]*(token_win-1) :
                            Token.place_token(i+1, ia)
                            return print("\ndebug : horizontale derrière bas")

                        if temp == [win_loose]*(token_win-2)+["0"]+[win_loose]:
                            Token.place_token(i+(token_win-1), ia)
                            return print("\ndebug : horizontale milieu + bas")

                        if temp == [win_loose]+[emptysymb]+[win_loose]*(token_win-2) :
                            Token.place_token(i+2, ia)
                            return print("\ndebug : horizontale milieu - bas")

                # verticale

            for ligne in range(token_width) :
                for i in range((token_height+1)-token_win) :
                    temp = [Ligne.list_inst_ligne[i+x].ligne[ligne] for x in range(token_win)]
                    if temp == [win_loose]*(token_win-1)+[emptysymb] :
                        Token.place_token(ligne+1, ia)
                        return print("\ndebug : vertical")

                #diagonales

                # droite haut

            for ligne in range((token_width+1)-token_win) :
                for i in range((token_height+1)-token_win):
                    temp = [Ligne.list_inst_ligne[i+x].ligne[ligne+1*x] for x in range(token_win)]
                    if temp == [win_loose]*(token_win-1)+[emptysymb] and Ligne.list_inst_ligne[i+1].ligne[ligne+(token_win-1)] == emptysymb or temp == [win_loose]*(token_win-1)+[emptysymb] and not Ligne.list_inst_ligne[i+2].ligne[ligne+(token_win-1)] == emptysymb :
                        Token.place_token(ligne+token_win, ia)
                        return print("\ndebug : droite haut")

                    if temp == [win_loose]*(token_win-2)+[emptysymb]+[win_loose] and Ligne.list_inst_ligne[i].ligne[ligne+(token_win-2)] == emptysymb or temp == [win_loose]*(token_win-2)+[emptysymb]+[win_loose] and not Ligne.list_inst_ligne[i+1].ligne[ligne+(token_win-2)] == emptysymb :
                        Token.place_token(ligne+(token_win-1), ia)
                        return print("\ndebug : droite middle +")
                        # droite bas

                    if temp == [emptysymb]+[win_loose]*(token_win-1) :
                        Token.place_token(ligne+1, ia)
                        return print("\ndebug : droite bas")

                    if temp == [win_loose]+[emptysymb]+[win_loose]*(token_win-2) :
                        Token.place_token(ligne+2, ia)
                        return print("\ndebug : droite middle -")

                # gauche haut

            for ligne in range(token_win-1, token_width) :
                for i in range((token_height+1)-token_win):
                    temp = [Ligne.list_inst_ligne[i+x].ligne[ligne-1*x] for x in range(token_win)]
                    if temp == [win_loose]*(token_win-1)+[emptysymb] and Ligne.list_inst_ligne[i+1].ligne[ligne-(token_win-1)] == emptysymb or temp == [win_loose]*(token_win-1)+[emptysymb] and not Ligne.list_inst_ligne[i+2].ligne[ligne-(token_win-1)] == emptysymb :
                        Token.place_token(ligne-(token_win-2), ia)
                        print(win_loose)
                        return print("\ndebug : gauche haut")

                    if temp == [win_loose]*2+[emptysymb]+[win_loose] and Ligne.list_inst_ligne[i].ligne[ligne-(token_win-2)] == emptysymb or temp == [win_loose]*(token_win-2)+[emptysymb]+[win_loose] and not Ligne.list_inst_ligne[i+1].ligne[ligne-(token_win-2)] == emptysymb :
                        Token.place_token(ligne-(token_win-3), ia)
                        return print("\ndebug : gauche middle +")

                        # gauche bas

                    if temp == [emptysymb]+[win_loose]*(token_win-1) :
                        Token.place_token(ligne+1, ia)
                        return print("\ndebug : gauche bas")

                    if temp == [win_loose]+[emptysymb]+[win_loose]*(token_win-2) :
                        Token.place_token(ligne, ia)
                        return print("\ndebug : gauche middle -")

            # si on ne peut pas bloquer une win ou win jouer "aléatoirement"

        for win_loose in [p2symb, p1symb] :
            for hauteur in range(token_height):
                for i in range(token_width-2):
                    temp = Ligne.list_inst_ligne[hauteur-1].ligne[i:i+3]
                    if temp == [emptysymb]+[win_loose]+[emptysymb] :
                        if i+2 < 4 :
                            Token.place_token(i+3, ia)
                            return print("\ndebug : nexto right")
                        elif i+2 > 4 :
                            Token.place_token(i+1, ia)
                            return print("\ndebug : nexto left")

        choix = randint(1,token_width)

        while Ligne.list_inst_ligne[-1].ligne[choix-1] in [p1symb, p2symb] :
            choix = randint(1,token_width)
        else :
            Token.place_token(choix, ia)
            return print("\ndebug : random")

class User():

    def user_move(joueur):
        global running, game_mode, player1, player2
        if running == True :
            choix = input("\n > ")
            print("\ndebug : "+joueur)
            if choix == "ia" :
                Ia.ia_move(joueur)
                if game_mode == "1":
                    player1, player2 = player2, player1
            elif choix.isdigit():
                colonne = int(choix)
                if colonne > token_width :
                    colonne = token_width
                elif colonne < 1 :
                    colonne = 1
                if Ligne.list_inst_ligne[-1].ligne[colonne-1] in [p1symb, p2symb] :
                    User.user_move(joueur)
                else :
                    if game_mode == "1":
                        player1, player2 = player2, player1
                    Token.place_token(colonne, joueur)

            elif choix == "back":
                running = False

            else :
                User.user_move(joueur)

class Token():

    def place_token(colonne, player):

        for ligne in Ligne.list_inst_ligne :
            if ligne.ligne[colonne-1] in [p1symb, p2symb] :
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

            Win_condition.draw(player, colonne)

            Win_condition.horrizontal(player, colonne)

            for ligne in range(token_width) :
                Win_condition.diag(0, ligne, player, colonne)

            for ligne in range((token_width+1)-token_win) :
                Win_condition.diag(1, ligne, player, colonne)

            for ligne in range(token_win-1, token_width) :
                Win_condition.diag(-1, ligne, player, colonne)

        # diagonale

        def diag(calc, ligne, player, colonne):

            for win_loose in [p1symb, p2symb] :
                for i in range((token_height+1)-token_win):
                    temp = [Ligne.list_inst_ligne[i+x].ligne[ligne+calc*x] for x in range(token_win)]
                    if temp == [win_loose]*token_win :
                        Win_condition.light_diag(calc, i, ligne)
                        Win_condition.win(player, colonne)
                        break

        # horizontale

        def horrizontal(player, colonne):

            for win_loose in [p1symb, p2symb] :
                for ligne in Ligne.list_inst_ligne :
                    for i in range((token_width+1)-token_win):
                        if ligne.ligne[i:i+token_win] == [win_loose]*token_win :

                            # light horizontal

                            for itération in range(token_win) :
                                ligne.ligne[i] = color3+ligne.ligne[i]+reset
                                i +=1

                            Win_condition.win(player, colonne)

                            break

        # mettre en surbrillance la diag de 4

        def light_diag(lign_op, i, ligne):
            for token in range(token_win) :
                Ligne.list_inst_ligne[i].ligne[ligne] = color3+Ligne.list_inst_ligne[i].ligne[ligne]+reset
                i +=1
                ligne += lign_op

        # si victoire

        def win(player, colonne):
            Board.display_board(colonne, player)
            global running
            if player == p1symb:
                print("\n"+color1+"BLUE"+reset+color3+" WIN"+reset+"\n")
            else :
                print("\n"+color2+"RED"+reset+color3+" WIN"+reset+"\n")
            running = False
            input("\n > ")

        # si égalité


        def draw(player, colonne):
            global running
            if emptysymb in Ligne.list_inst_ligne[-1].ligne :
                return
            else :
                Board.display_board(colonne, player)
                print("\n"+color3+" DRAW"+reset+"\n")
                running = False
                input("\n > ")

# initialisation des variables

emptysymb = "0"
p1symb = "1"
p2symb = "2"

running = True
fst_ia = p1symb
player1 = p1symb
player2 = p2symb
game_mode = ""
ia1 = p1symb
ia2 = p2symb

# constante game_var

token_win = 4
token_width = 7
token_height = 6

# instansiation des lignes

for ligne in range(token_height):
    ligne = Ligne()

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
        User.user_move(p1symb)
        if not running :
            Menu.display_menu()
        else :
            time.sleep(uniform(0.5, 1.5))
            Ia.ia_move(p2symb)
            if not running :
                Menu.display_menu()

    # ia vs ia

    elif game_mode == "3" and running :
        time.sleep(uniform(0.5, 1.5))
        Ia.ia_move(ia1)
        ia1, ia2 = ia2, ia1
        if not running :
            if fst_ia == p1symb :
                fst_ia = p2symb
                ia1 = p2symb
                ia2 = p1symb
            else :
                fst_ia = p1symb
                ia1 = p1symb
                ia2 = p2symb
            Menu.display_menu()
