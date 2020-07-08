
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
        self.colonne = []
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
            Board.display_board(token_width, None, None, 0.1)
        elif game_mode == "4" :
            game_start()

        elif game_mode == "5"  :
            running = False

        else :
            Menu.menu()

class Board():

    def initialize_board():

        # reinitialise chaque ligne

        for ligne in Ligne.list_inst_ligne:
            ligne.colonne = ["0"]*token_width

    def display_board(colonne, player, lign=None, startime=0.025, color=""):

        # permet d'indiquer ou et qui à jouer le dernier coup

        if player == "2":
            color = color5
        elif player == "1":
            color = color1

        # affichage numéro + triangle

        print("\n"*10)

        numero_colonne = "    "+"|".join([f"{color4 + str(i+1) + reset}" for i in range(token_width)])
        Board.display_triangle_nbr(numero_colonne, startime, color, colonne)

        # affichage des lignes

        Board.display_lign(p1symb, p2symb, color, color1, color2, color4, reset, startime, lign)

    def display_lign(p1symb, p2symb, color, color1, color2, color4, reset, startime, lign):

        x = len(Ligne.list_inst_ligne)

        for element in reversed(Ligne.list_inst_ligne):
            ligne = element.colonne.copy()
            while p1symb in ligne :
                    ligne[ligne.index(p1symb)] = color1+p1symb+reset
            while p2symb in ligne :
                ligne[ligne.index(p2symb)] = color2+p2symb+reset

            tableau = "|".join(ligne)
            time.sleep(startime)

            # affiche les numéro sur le coté pour le mode morpion

            if gravity == False :
                if x == lign :
                    print(color4+str(x)+reset+color+" ▸ "+reset+tableau)
                else :
                    print(color4+str(x)+reset+" ▸ "+tableau)

            else :
                print("    "+tableau)
            x -= 1

    def display_triangle_nbr(numero_colonne, startime, color, colonne):
        triangle_list = []
        for colonnes in range(token_width):
            triangle_list.append("▾")
        triangle_list[colonne-1] = color+triangle_list[colonne-1]+reset
        triangle = "    "+" ".join(triangle_list)

        time.sleep(startime)
        print(numero_colonne)
        time.sleep(startime)
        print(triangle)

class Ia():

    # fonction principale

    def ia_move(ia):

        global player1, player2

        player1, player2 = player2, player1

        # verifie si l'ia peut empecher l'adversaire de gagner ou de gagner elle meme ou autre

        for win_loose in [p2symb,p1symb] :

            #horizontale

            for lign in range(token_height):
                for col in range((token_width+1)-token_win):
                    temp = Ligne.list_inst_ligne[lign].colonne[col:col+token_win]
                    if lign > 1 and gravity == True :
                        if Ia.horizontal_top(temp, lign, col+1, win_loose, ia) or Ia.horizontal_middle(temp, lign, col+1, win_loose, ia) :
                            return
                    if lign == 1 and gravity == True :
                        if Ia.horizontal_middle(temp, lign, col+1, win_loose, ia) :
                            return
                    elif lign == 0 or gravity == False:
                        if Ia.horizontal_bot(temp, lign+1, col+1, win_loose, ia) :
                            return

            # verticale

            for lign in range((token_height+1)-token_win) :
                for col in range(token_width) :
                    temp = [Ligne.list_inst_ligne[lign+x].colonne[col] for x in range(token_win)]
                    if Ia.vertical(temp, lign+1, col+1, win_loose, ia) :
                        return

            # diag droite

            for col in range((token_width+1)-token_win) :
                for lign in range((token_height+1)-token_win):
                    temp = [Ligne.list_inst_ligne[lign+x].colonne[col+1*x] for x in range(token_win)]
                    if Ia.diag_right(temp, lign+1, col+1, win_loose, ia) :
                        return

            # gauche haut

            for col in range(token_win-1, token_width) :
                for lign in range((token_height+1)-token_win):
                    temp = [Ligne.list_inst_ligne[lign+x].colonne[col-1*x] for x in range(token_win)]
                    if Ia.diag_left(temp, lign+1, col+1, win_loose, ia) :
                        return

        # permet de faire en sorte que les jeton sois plus concentrés si un jeton est seul

        for win_loose in [p2symb, p1symb] :
            for lign in range(token_height):
                for col in range(token_width-2):
                    temp = Ligne.list_inst_ligne[lign].colonne[col:col+3]

                    if Ia.nexto(temp, lign+1, col+1, win_loose, ia) :
                        return

        # sinon jouer aléatoirement

        col = randint(1,token_width)
        lign = randint(1,token_height)
        if gravity == False :
            while Ligne.list_inst_ligne[lign-1].colonne[col-1] in [p1symb, p2symb] :
                col = randint(1,token_width)
                lign = randint(1,token_height)
            else :
                Token.place_token(col, ia, lign)
                return print("\ndebug : random no grav")
        else :
            while Ligne.list_inst_ligne[-1].colonne[col-1] in [p1symb, p2symb] :
                col = randint(1,token_width)
            else :
                Token.place_token(col, ia)
                return print("\ndebug : random grav")

    def horizontal_bot(temp, lign, col, win_loose, ia):

        if temp == [win_loose]*(token_win-1)+[emptysymb] :
            Token.place_token(col+(token_win-1), ia, lign)
            print("\ndebug : horizontale devant bas")
            return True
        elif temp == [emptysymb]+[win_loose]*(token_win-1) :
            Token.place_token(col, ia, lign)
            print("\ndebug : horizontale derrière bas")
            return True
        elif temp == [win_loose]*(token_win-2)+["0"]+[win_loose]:
            Token.place_token(col+(token_win-2), ia, lign)
            print("\ndebug : horizontale milieu + bas")
            return True
        elif temp == [win_loose]+[emptysymb]+[win_loose]*(token_win-2) :
            Token.place_token(col+1, ia, lign)
            print("\ndebug : horizontale milieu - bas")
            return True
        else :
            return False

    def horizontal_middle(temp, lign, col, win_loose, ia):

        if temp == [win_loose]*(token_win-1)+[emptysymb] and not Ligne.list_inst_ligne[lign-1].colonne[col-1+(token_win-1)] == emptysymb :
            Token.place_token(col+(token_win-1), ia)
            print("\ndebug : horizontale devant middle")
            return True
        elif temp == [emptysymb]+[win_loose]*(token_win-1) and not Ligne.list_inst_ligne[lign-1].colonne[col-1] == emptysymb :
            Token.place_token(col, ia)
            print("\ndebug : horizontale derrière middle")
            return True
        elif temp == [win_loose]*(token_win-2)+[emptysymb]+[win_loose] and not Ligne.list_inst_ligne[lign-1].colonne[col+(token_win-2)] == emptysymb :
            Token.place_token(col+(token_win-2), ia)
            print("\ndebug : horizontale milieu + middle")
            return True
        elif temp == [win_loose]+[emptysymb]+[win_loose]*(token_win-2) and not Ligne.list_inst_ligne[lign-1].colonne[col+1] == emptysymb :
            Token.place_token(col+1, ia)
            print("\ndebug : horizontale milieu - middle")
            return True
        else :
            return False

    def horizontal_top(temp, lign, col, win_loose, ia):

        if temp == [win_loose]*(token_win-1)+[emptysymb] and Ligne.list_inst_ligne[lign-2].colonne[col-1+token_win-1] == emptysymb  :
            Token.place_token(col+(token_win-1), ia)
            print("\ndebug : horizontale devant haut")
            return True
        elif temp == [emptysymb]+[win_loose]*(token_win-1) and Ligne.list_inst_ligne[lign-2].colonne[col-1] == emptysymb :
            Token.place_token(col, ia)
            print("\ndebug : horizontale derrière haut")
            return True
        elif temp == [win_loose]*(token_win-2)+[emptysymb]+[win_loose] and Ligne.list_inst_ligne[lign-2].colonne[col-1+token_win-2] == emptysymb  :
            Token.place_token(col+(token_win-2), ia)
            print("\ndebug : horizontale milieu + haut")
            return True
        elif temp == [win_loose]+[emptysymb]+[win_loose]*(token_win-2) and Ligne.list_inst_ligne[lign-2].colonne[col-1+1] == emptysymb  :
            Token.place_token(col+1, ia)
            print("\ndebug : horizontale milieu - haut")
            return True
        else :
            return False

    def vertical(temp, lign, col, win_loose, ia):

        if temp == [win_loose]*(token_win-1)+[emptysymb] :
            Token.place_token(col, ia, lign+(token_win-1))
            print("\ndebug : vertical +")
            return True
        elif temp == [emptysymb]+[win_loose]*(token_win-1) :
            Token.place_token(col, ia, lign)
            print("\ndebug : vertical -")
            return True
        elif temp == [win_loose]*(token_win-2)+[emptysymb]+[win_loose] :
            Token.place_token(col, ia, lign+(token_win-2))
            print("\ndebug : vertical middle +")
            return True
        elif temp == [win_loose]+[emptysymb]+[win_loose]*(token_win-2) :
            Token.place_token(col, ia, lign+1)
            print("\ndebug : vertical middle -")
            return True
        else :
            return False

    def diag_right(temp, lign, col, win_loose, ia):

        if temp == [win_loose]*(token_win-1)+[emptysymb] :
            if Ligne.list_inst_ligne[lign].colonne[col-1+(token_win-1)] == emptysymb :
                Token.place_token(col+(token_win-1), ia, lign+(token_win-1))
                print("\ndebug : droite haut")
                return True
            elif not Ligne.list_inst_ligne[lign+1].colonne[col-1+(token_win-1)] == emptysymb :
                Token.place_token(col+(token_win-1), ia, lign+(token_win-1))
                print("\ndebug : droite haut block/finish")
                return True
        elif temp == [win_loose]*(token_win-2)+[emptysymb]+[win_loose] :
            if Ligne.list_inst_ligne[lign-1].colonne[col-1+(token_win-2)] == emptysymb :
                Token.place_token(col+(token_win-2), ia, lign+(token_win-2))
                print("\ndebug : droite middle +")
                return True
            elif not Ligne.list_inst_ligne[lign].colonne[col-1+(token_win-2)] == emptysymb :
                Token.place_token(col+(token_win-2), ia, lign+(token_win-2))
                print("\ndebug : droite middle + block/finish")
                return True

            # droite bas

        elif temp == [emptysymb]+[win_loose]*(token_win-1) :
            Token.place_token(col, ia, lign)
            print("\ndebug : droite bas")
            return True
        elif temp == [win_loose]+[emptysymb]+[win_loose]*(token_win-2) :
            Token.place_token(col+1, ia, lign+1)
            print("\ndebug : droite middle -")
            return True
        else :
            return False

    def diag_left(temp, lign, col, win_loose, ia):

        if temp == [win_loose]*(token_win-1)+[emptysymb] :
            if Ligne.list_inst_ligne[lign].colonne[col-1-(token_win-1)] == emptysymb :
                Token.place_token(col-(token_win-1), ia, lign+(token_win-1))
                print("\ndebug : gauche haut")
                return True
            elif not Ligne.list_inst_ligne[lign+1].colonne[col-1-(token_win-1)] == emptysymb :
                Token.place_token(col-(token_win-1), ia, lign+(token_win-1))
                print("\ndebug : gauche haut block/finish")
                return True
        elif temp == [win_loose]*(token_win-2)+[emptysymb]+[win_loose] :
            if Ligne.list_inst_ligne[lign-1].colonne[col-1-(token_win-2)] == emptysymb :
                Token.place_token(col-(token_win-2), ia, lign+(token_win-2))
                print("\ndebug : gauche middle +")
                return True
            elif not Ligne.list_inst_ligne[lign].colonne[col-1-(token_win-2)] == emptysymb :
                Token.place_token(col-(token_win-2), ia, lign+(token_win-2))
                print("\ndebug : gauche middle + block/finish")
                return True

            # gauche bas

        elif temp == [emptysymb]+[win_loose]*(token_win-1) :
            Token.place_token(col, ia, lign)
            print("\ndebug : gauche bas")
            return True
        elif temp == [win_loose]+[emptysymb]+[win_loose]*(token_win-2) :
            Token.place_token(col-1, ia, lign+1)
            print("\ndebug : gauche middle -")
            return True
        else :
            return False

    def nexto(temp, lign, col, win_loose, ia):

        if temp == [emptysymb]+[win_loose]+[emptysymb] :
            rightleft = randint(0,1)
            if rightleft :
                Token.place_token(col+2, ia, lign)
                print("\ndebug : nexto right")
                return True
            else :
                Token.place_token(col, ia, lign)
                print("\ndebug : nexto left")
                return True
        else :
            return False


class User():

    def user_main(joueur):

        global running, game_mode, player1, player2
        if running == True :

            col = input("\ncolumn > ")

            if User.user_ia_move(joueur, col) :
                pass
            elif col.isdigit() :

                col = int(col)

                if col > token_width :
                    col = token_width
                elif col < 1 :
                    col = 1

                User.user_move_grav(joueur, col, p1symb, p2symb)

            elif col == "back":
                running = False
            else :
                User.user_main(joueur)

    def user_main_no_grav(joueur) :

        global running, game_mode, player1, player2

        if running == True :

            col = input("\ncolumn > ")
            lign = input("\nlign > ")

            if User.user_ia_move(joueur, col, lign) :
                pass
            elif lign.isdigit() and col.isdigit() :

                col = int(col)
                lign = int(lign)

                # regulation des inputs

                if col > token_width :
                    col = token_width
                if col < 1 :
                    col = 1

                if lign > token_height :
                    lign = token_height
                if lign < 1 :
                    lign = 1

                User.user_move_no_grav(lign, col, p1symb, p2symb, joueur)

            elif col == "back" or lign == "back":
                running = False
            else :
                User.user_main_no_grav(joueur)

    def user_ia_move(joueur, col, lign=""):

        if col == "ia" or lign == "ia" :
            Ia.ia_move(joueur)
            return True
        else :
            return False

    def user_move_grav(joueur, col, p1symb, p2symb):

        global player1, player2

        if Ligne.list_inst_ligne[-1].colonne[col-1] in [p1symb, p2symb] :
            User.user_main(joueur)
        else :
            player1, player2 = player2, player1
            Token.place_token(col, joueur)

    def user_move_no_grav(lign, col, p1symb, p2symb, joueur):

        global player1, player2

        if Ligne.list_inst_ligne[lign-1].colonne[col-1] in [p1symb, p2symb] :
            User.user_main_no_grav(joueur)

        else :
            player1, player2 = player2, player1
            Token.place_token(col, joueur, lign)





class Token():

    def place_token(colonne, player, ligne=None):

        if gravity == False :
            Ligne.list_inst_ligne[ligne-1].colonne[colonne-1] = player
        else :
            for ligne in Ligne.list_inst_ligne :
                if ligne.colonne[colonne-1] in [p1symb, p2symb] :
                    pass
                else :
                    ligne.colonne[colonne-1] = player
                    break
        Win_condition.is_win(colonne, player)
        if running == True :
            Board.display_board(colonne, player, ligne)

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
                    temp = [Ligne.list_inst_ligne[i+x].colonne[ligne+calc*x] for x in range(token_win)]
                    if temp == [win_loose]*token_win :
                        Win_condition.light_diag(calc, i, ligne)
                        Win_condition.win(player, colonne)
                        break

        # horizontale

        def horrizontal(player, colonne):

            for win_loose in [p1symb, p2symb] :
                for ligne in Ligne.list_inst_ligne :
                    for i in range((token_width+1)-token_win):
                        if ligne.colonne[i:i+token_win] == [win_loose]*token_win :

                            # light horizontal

                            for itération in range(token_win) :
                                ligne.colonne[i] = color3+ligne.colonne[i]+reset
                                i +=1
                            Win_condition.win(player, colonne)
                            break

        # mettre en surbrillance les "diags"

        def light_diag(lign_op, i, ligne):
            for token in range(token_win) :
                Ligne.list_inst_ligne[i].colonne[ligne] = color3+Ligne.list_inst_ligne[i].colonne[ligne]+reset
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
                    if emptysymb in ligne.colonne :
                        return
                else :
                    Board.display_board(colonne, player)
                    print("\n"+color3+" DRAW"+reset+"\n")
                    running = False
                    input("\n > ")
            else :
                if emptysymb in Ligne.list_inst_ligne[-1].colonne :
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
    twidth = input("\nEntrez la "+color1+"COLONNES"+reset+" du tableau > ")
    theight = input("\nEntrez la "+color1+"LIGNES"+reset+" du tableau > ")
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

    print("\ndebug : next player"+player1)

    # local

    if game_mode == "1" and running :
        if gravity == True :
            User.user_main(player1)
        else :
            User.user_main_no_grav(player1)
        if not running :
            Menu.display_menu()

    # vs ia

    elif game_mode == "2" and running :
        if gravity == True :
            User.user_main(p1symb)
        else :
            User.user_main_no_grav(p1symb)
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
