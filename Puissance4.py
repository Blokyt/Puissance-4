
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
        print("\n"+color1+" 1"+reset+" : Local\n"+color1+" 2"+reset+" : Contre l'IA\n"+color1+" 3"+reset+" : IA VS IA\n"+color1+" 4"+reset+" : Regles\n\n"+color1+" 5"+reset+" : Exit")
        Menu.menu()

    # choix du mode

    def menu():
        global game_mode, running, turnpass, player1, player2, gravity, token_win, token_width, token_height, p1symb, p2symb
        game_mode = input("\n > ")
        if game_mode == "1" or game_mode == "2" or game_mode == "3" :
            running = True
            player1 = p1symb
            player2 = p2symb
            Board.initialize_board()
            Board.display_board(token_width, None, 0.1)
        elif game_mode == "4" :
            game_start()

        elif game_mode == "5"  :
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
        numéro_colonne = "    "+"|".join([f"{color4 + str(i+1) + reset}" for i in range(token_width)])


        triangle_list = []
        for colonnes in range(token_width):
            triangle_list.append("▾")
        triangle_list[colonne-1] = color+triangle_list[colonne-1]+reset
        triangle = "    "+" ".join(triangle_list)

        x = 1
        nb_coté = len(Ligne.list_inst_ligne)
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
            if gravity == False :
                print(color4+str(nb_coté)+reset+" ▸ "+tableau+" ◂ "+color4+str(nb_coté)+reset)
            else :
                print("    "+tableau)
            nb_coté -= 1
            x += 1

        triangle_list = []
        for colonnes in range(token_width):
            triangle_list.append("▴")
        triangle_list[colonne-1] = color+triangle_list[colonne-1]+reset
        triangle = "    "+" ".join(triangle_list)

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
                    if hauteur > 1 and gravity == True :
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

                    if hauteur == 1 and gravity == True :
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

                    elif hauteur == 0 or gravity == False :
                        if temp == [win_loose]*(token_win-1)+[emptysymb] :
                            Token.place_token(i+token_win, ia, hauteur+1)
                            return print("\ndebug : horizontale devant bas")

                        if temp == [emptysymb]+[win_loose]*(token_win-1) :
                            Token.place_token(i+1, ia, hauteur+1)
                            return print("\ndebug : horizontale derrière bas")

                        if temp == [win_loose]*(token_win-2)+["0"]+[win_loose]:
                            Token.place_token(i+(token_win-1), ia, hauteur+1)
                            return print("\ndebug : horizontale milieu + bas")

                        if temp == [win_loose]+[emptysymb]+[win_loose]*(token_win-2) :
                            Token.place_token(i+2, ia, hauteur+1)
                            return print("\ndebug : horizontale milieu - bas")

                # verticale

            for ligne in range(token_width) :
                for i in range((token_height+1)-token_win) :
                    temp = [Ligne.list_inst_ligne[i+x].ligne[ligne] for x in range(token_win)]

                    if temp == [win_loose]*(token_win-1)+[emptysymb] :
                        Token.place_token(ligne+1, ia, i+token_win)
                        return print("\ndebug : vertical +")

                    elif temp == [emptysymb]+[win_loose]*(token_win-1) :
                        Token.place_token(ligne+1, ia, i+1)
                        return print("\ndebug : vertical -")

                    elif temp == [win_loose]*(token_win-2)+[emptysymb]+[win_loose] :
                        Token.place_token(ligne+1, ia, i+(token_win-1))
                        return print("\ndebug : vertical middle +")

                    elif temp == [win_loose]+[emptysymb]+[win_loose]*(token_win-2) :
                        Token.place_token(ligne+1, ia, i+2)
                        return print("\ndebug : vertical middle -")

                #diagonales

                # droite haut

            for ligne in range((token_width+1)-token_win) :
                for i in range((token_height+1)-token_win):
                    temp = [Ligne.list_inst_ligne[i+x].ligne[ligne+1*x] for x in range(token_win)]
                    if temp == [win_loose]*(token_win-1)+[emptysymb] and Ligne.list_inst_ligne[i+1].ligne[ligne+(token_win-1)] == emptysymb or temp == [win_loose]*(token_win-1)+[emptysymb] and not Ligne.list_inst_ligne[i+2].ligne[ligne+(token_win-1)] == emptysymb :
                        Token.place_token(ligne+token_win, ia, i+token_win)
                        return print("\ndebug : droite haut")

                    if temp == [win_loose]*(token_win-2)+[emptysymb]+[win_loose] and Ligne.list_inst_ligne[i].ligne[ligne+(token_win-2)] == emptysymb or temp == [win_loose]*(token_win-2)+[emptysymb]+[win_loose] and not Ligne.list_inst_ligne[i+1].ligne[ligne+(token_win-2)] == emptysymb :
                        Token.place_token(ligne+(token_win-1), ia, i+(token_win-1))
                        return print("\ndebug : droite middle +")
                        # droite bas

                    if temp == [emptysymb]+[win_loose]*(token_win-1) :
                        Token.place_token(ligne+1, ia, i+1)
                        return print("\ndebug : droite bas")

                    if temp == [win_loose]+[emptysymb]+[win_loose]*(token_win-2) :
                        Token.place_token(ligne+2, ia, i+2)
                        return print("\ndebug : droite middle -")

                # gauche haut

            for ligne in range(token_win-1, token_width) :
                for i in range((token_height+1)-token_win):
                    temp = [Ligne.list_inst_ligne[i+x].ligne[ligne-1*x] for x in range(token_win)]
                    if temp == [win_loose]*(token_win-1)+[emptysymb] and Ligne.list_inst_ligne[i+1].ligne[ligne-(token_win-1)] == emptysymb or temp == [win_loose]*(token_win-1)+[emptysymb] and not Ligne.list_inst_ligne[i+2].ligne[ligne-(token_win-1)] == emptysymb :
                        Token.place_token(ligne-(token_win-2), ia, i+token_win)
                        print(win_loose)
                        return print("\ndebug : gauche haut")

                    if temp == [win_loose]*(token_win-2)+[emptysymb]+[win_loose] and Ligne.list_inst_ligne[i].ligne[ligne-(token_win-2)] == emptysymb or temp == [win_loose]*(token_win-2)+[emptysymb]+[win_loose] and not Ligne.list_inst_ligne[i+1].ligne[ligne-(token_win-2)] == emptysymb :
                        Token.place_token(ligne-(token_win-3), ia, i+(token_win-1))
                        return print("\ndebug : gauche middle +")

                        # gauche bas

                    if temp == [emptysymb]+[win_loose]*(token_win-1) :
                        Token.place_token(ligne+1, ia, i+1)
                        return print("\ndebug : gauche bas")

                    if temp == [win_loose]+[emptysymb]+[win_loose]*(token_win-2) :
                        Token.place_token(ligne, ia, i+2)
                        return print("\ndebug : gauche middle -")

            # si on ne peut pas bloquer une win ou win jouer "aléatoirement"

        for win_loose in [p2symb, p1symb] :
            for hauteur in range(token_height):
                for i in range(token_width-2):
                    temp = Ligne.list_inst_ligne[hauteur-1].ligne[i:i+3]
                    if temp == [emptysymb]+[win_loose]+[emptysymb] :
                        rightleft = randint(0,1)
                        if rightleft :
                            Token.place_token(i+3, ia, hauteur)
                            return print("\ndebug : nexto right")
                        else :
                            Token.place_token(i+1, ia, hauteur)
                            return print("\ndebug : nexto left")

        col = randint(1,token_width)
        lign = randint(1,token_width)

        if gravity == False :

            while Ligne.list_inst_ligne[lign-1].ligne[col-1] in [p1symb, p2symb] :
                col = randint(1,token_width)
                lign = randint(1,token_height)
            else :
                Token.place_token(col, ia, lign)
                return print("\ndebug : random")

        else :

            while Ligne.list_inst_ligne[-1].ligne[col-1] in [p1symb, p2symb] :
                col = randint(1,token_width)
            else :
                Token.place_token(col, ia)
                return print("\ndebug : random")

class User():

    def user_move(joueur):
        global running, game_mode, player1, player2
        lign = ""
        if running == True :
            print("\ndebug : next player "+joueur)
            if gravity == False :

                col = input("\ncolumn > ")
                lign = input("\nlign > ")

                if lign == "ia" or col == "ia" :
                    if game_mode == "1":
                        player1, player2 = player2, player1
                    Ia.ia_move(joueur)


                elif lign.isdigit() and col.isdigit() :

                    colonne = int(col)

                    if colonne > token_width :
                        colonne = token_width
                    elif colonne < 1 :
                        colonne = 1

                    ligne = int(lign)

                    if ligne > token_height :
                        ligne = token_height
                    elif ligne < 1 :
                        ligne = 1

                    if Ligne.list_inst_ligne[ligne-1].ligne[colonne-1] in [p1symb, p2symb] :
                        User.user_move(joueur)
                    else :
                        if game_mode == "1":
                            player1, player2 = player2, player1
                        Token.place_token(colonne, joueur, ligne)

                elif col == "back" or lign == "back":
                    running = False

                else :
                    User.user_move(joueur)

            else :
                col = input("\ncolumn > ")

                if col == "ia" :
                    Ia.ia_move(joueur)
                    if game_mode == "1":
                        player1, player2 = player2, player1

                elif col.isdigit() :

                    colonne = int(col)

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

                elif col == "back":
                    running = False

                else :
                    User.user_move(joueur)

class Token():

    def place_token(colonne, player, ligne=None):

        if gravity == False :
            Ligne.list_inst_ligne[ligne-1].ligne[colonne-1] = player
        else :
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

            Win_condition.horrizontal(player, colonne)

            for ligne in range(token_width) :
                Win_condition.diag(0, ligne, player, colonne)

            for ligne in range((token_width+1)-token_win) :
                Win_condition.diag(1, ligne, player, colonne)

            for ligne in range(token_win-1, token_width) :
                Win_condition.diag(-1, ligne, player, colonne)

            Win_condition.draw(player, colonne)

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
            if gravity == False :
                for ligne in Ligne.list_inst_ligne :
                    if emptysymb in ligne.ligne :
                        return
                else :
                    Board.display_board(colonne, player)
                    print("\n"+color3+" DRAW"+reset+"\n")
                    running = False
                    input("\n > ")
            else :
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

gravity = True
running = True
fst_ia = p1symb
player1 = p1symb
player2 = p2symb
game_mode = ""
ia1 = p1symb
ia2 = p2symb

token_win = None
token_width = None
token_height = None

# definir constante game_var

def game_start():

    global running, token_win, token_width, token_height, gravity
    running = True
    twin = input("\nEntrez le "+color1+"NOMBRE DE JETON"+reset+" à aligner pour gagner > ")
    twidth = input("\nEntrez la "+color1+"LARGEUR"+reset+" du tableau > ")
    theight = input("\nEntrez la "+color1+"HAUTEUR"+reset+" du tableau > ")
    isgravity = input("\nActiver la "+color1+"GRAVITÉ"+reset+" ? (yes/no) > ")
    if isgravity == "yes" :
        gravity = True
    elif isgravity == "no" :
        gravity = False
    if twin.isdigit() and twidth.isdigit() and theight.isdigit() :
        token_win = int(twin)
        token_width = int(twidth)
        token_height = int(theight)
        if token_win > token_width and token_win > token_height :
            running = False
            print("\n"+color2+"Erreur Systeme !"+reset)
    else :
        running = False
        print("\n"+color2+"Erreur Systeme !"+reset)

# Entrer dans la game loop

    if running == True :

        # instansiation des lignes
        Ligne.list_inst_ligne = []
        for ligne in range(token_height):
            ligne = Ligne()

        Menu.display_menu()

game_start()

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
