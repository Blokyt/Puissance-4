
from colored import *

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

        numéro_colonne = "\n"+color4+"1"+reset+"|"+color4+"2"+reset+"|"+color4+"3"+reset+"|"+color4+"4"+reset+"|"+color4+"5"+reset+"|"+color4+"6"+reset+"|"+color4+"7"+reset+"\n"

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

    def action():
        global turn
        global running
        print("\n")
        Ligne.display_board()
        choix = input("\n > ")
        if choix.isdigit() :
            Ligne.choose_ligne_token(int(choix))
        elif choix == "stop":
            running = False
            pass
        else :
            Ligne.action()


        Ligne.verification_win()

# deposer jeton

    def choose_ligne_token(colonne):

        global turn

        if colonne > 7 :
            colonne = 7
        elif colonne < 1 :
            colonne = 1

        for ligne in Ligne.list_inst_ligne :
            if Ligne.list_inst_ligne[len(Ligne.list_inst_ligne)-1].ligne[colonne-1] == "1" :
                print("debug")
                break
            elif ligne.ligne[colonne-1] == "1" or ligne.ligne[colonne-1] == "2" :
                pass
            else :
                ligne.ligne[colonne-1] = turn
                print(turn)
                break

# verification win

    def verification_win():

        Ligne.horrizontal_win()

        for ligne in range(len(ligne1.ligne)-3) :
            Ligne.win_diag_vert(0, ligne)

        for ligne in range(len(ligne1.ligne)-3) :
            Ligne.win_diag_vert(1, ligne)

        for ligne in range(3, len(ligne1.ligne)) :
            Ligne.win_diag_vert(-1, ligne)

# diagonales et verticale

    def win_diag_vert(calc, ligne):
        for i in range(len(ligne1.ligne)-4):
            if Ligne.list_inst_ligne[i].ligne[ligne] in ["1","2"] and Ligne.list_inst_ligne[i].ligne[ligne] == Ligne.list_inst_ligne[i+1].ligne[ligne+calc] == Ligne.list_inst_ligne[i+2].ligne[ligne+calc*2] == Ligne.list_inst_ligne[i+3].ligne[ligne+calc*3]:
                Ligne.surbrillance_win(calc, i, ligne)
                Ligne.win()
                break

# horizontale

    def horrizontal_win():

        for ligne in Ligne.list_inst_ligne :
            for i in range(len(ligne.ligne)-3):
                if ligne.ligne[i] in ["1","2"] and ligne.ligne[i] == ligne.ligne[i+1] == ligne.ligne[i+2] == ligne.ligne[i+3]:
                    for itération in range(4) :
                        ligne.ligne[i] = color3+ligne.ligne[i]+reset
                        i +=1
                    Ligne.win()
                    break

# mettre en surbrillance la ligne de 4

    def surbrillance_win(lign_op, i, ligne):
        for itération in range(4) :
            Ligne.list_inst_ligne[i].ligne[ligne] = color3+Ligne.list_inst_ligne[i].ligne[ligne]+reset
            i +=1
            ligne += lign_op

# si victoire

    def win():
        global running
        Ligne.display_board()
        print("\n"+color3+"WIN"+reset+"\n")
        running = False

# instansiation des lignes

ligne6 = Ligne(6)
ligne5 = Ligne(5)
ligne4 = Ligne(4)
ligne3 = Ligne(3)
ligne2 = Ligne(2)
ligne1 = Ligne(1)

running = True

turn = ""

# game loop

while running :

    if turn == "1":
        turn = "2"
    else :
        turn = "1"

    Ligne.action()
