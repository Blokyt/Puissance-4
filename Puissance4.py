
from colored import *

color1 = fg('cyan')
color2 = fg('red')
color3 = fg('green')
reset = attr('reset')

class Ligne():

    list_inst_ligne = []

    def __init__(self, name):
        self.name = name
        self.ligne = ["0","0","0","0","0","0","0"]
        self.list_inst_ligne.append(self)

    def display_board():
        x = 1
        for inst in Ligne.list_inst_ligne:
            ligne = Ligne.list_inst_ligne[len(Ligne.list_inst_ligne)-x].ligne.copy()
            while "1" in ligne :
                ligne[ligne.index("1")] = color1+"1"+reset
            while "2" in ligne :
                ligne[ligne.index("2")] = color2+"2"+reset
            affichage = "|".join(ligne)
            print(affichage)
            x += 1

    def action():
        global turn
        global running
        print("\n")
        Ligne.display_board()
        choix = input("\n > ")
        if choix == "1" :
            Ligne.choose_ligne(1)
        elif choix == "2":
            Ligne.choose_ligne(2)
        elif choix == "3":
            Ligne.choose_ligne(3)
        elif choix == "4":
            Ligne.choose_ligne(4)
        elif choix == "5":
            Ligne.choose_ligne(5)
        elif choix == "6":
            Ligne.choose_ligne(6)
        elif choix == "7":
            Ligne.choose_ligne(7)
        elif choix == "stop":
            running = False
            pass


        Ligne.verification_win()

    def choose_ligne(colonne):
        global turn
        if turn == "1" :
            turn = "2"
        else :
            turn = "1"
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

    def verification_win():

        for ligne in Ligne.list_inst_ligne :
            for i in range(len(ligne.ligne)-3):
                if ligne.ligne[i] in ["1","2"] and ligne.ligne[i] == ligne.ligne[i+1] == ligne.ligne[i+2] == ligne.ligne[i+3]:
                    for itération in range(4) :
                        ligne.ligne[i] = color3+ligne.ligne[i]+reset
                        i +=1
                    Ligne.win()
                    break

        for ligne in range(len(ligne1.ligne)-3) :
            for i in range(len(ligne1.ligne)-4):
                if Ligne.list_inst_ligne[i].ligne[ligne] in ["1","2"] and Ligne.list_inst_ligne[i].ligne[ligne] == Ligne.list_inst_ligne[i+1].ligne[ligne] == Ligne.list_inst_ligne[i+2].ligne[ligne] == Ligne.list_inst_ligne[i+3].ligne[ligne]:
                    for itération in range(4) :
                        Ligne.list_inst_ligne[i].ligne[ligne] = color3+Ligne.list_inst_ligne[i].ligne[ligne]+reset
                        i +=1
                    Ligne.win()
                    break

        for ligne in range(len(ligne1.ligne)-3) :
            for i in range(len(ligne1.ligne)-4):
                if Ligne.list_inst_ligne[i].ligne[ligne] in ["1","2"] and Ligne.list_inst_ligne[i].ligne[ligne] == Ligne.list_inst_ligne[i+1].ligne[ligne+1] == Ligne.list_inst_ligne[i+2].ligne[ligne+2] == Ligne.list_inst_ligne[i+3].ligne[ligne+3] :
                    for itération in range(4) :
                        Ligne.list_inst_ligne[i].ligne[ligne] = color3+Ligne.list_inst_ligne[i].ligne[ligne]+reset
                        i +=1
                        ligne += 1
                    Ligne.win()
                    break


        for ligne in range(3, len(ligne1.ligne)) :
            for i in range(len(ligne1.ligne)-4):
                if Ligne.list_inst_ligne[i].ligne[ligne] in ["1","2"] and Ligne.list_inst_ligne[i].ligne[ligne] == Ligne.list_inst_ligne[i+1].ligne[ligne-1] == Ligne.list_inst_ligne[i+2].ligne[ligne-2] == Ligne.list_inst_ligne[i+3].ligne[ligne-3]:
                    for itération in range(4) :
                        Ligne.list_inst_ligne[i].ligne[ligne] = color3+Ligne.list_inst_ligne[i].ligne[ligne]+reset
                        i +=1
                        ligne -= 1
                    Ligne.win()
                    break

    def win():
        global running
        Ligne.display_board()
        print("\n"+color3+"WIN"+reset+"\n")
        running = False

ligne6 = Ligne(6)
ligne5 = Ligne(5)
ligne4 = Ligne(4)
ligne3 = Ligne(3)
ligne2 = Ligne(2)
ligne1 = Ligne(1)

running = True

turn = "2"

while running :
    Ligne.action()
