##partita di scopa in python
import random

mazzo=[
                "1c", "1q", "1f", "1p",
                "2c", "2q", "2f", "2p",
                "3c", "3q", "3f", "3p",
                "4c", "4q", "4f", "4p",
                "5c", "5q", "5f", "5p",
                "6c", "6q", "6f", "6p",
                "7c", "7q", "7f", "7p",
                "Jc", "Jq", "Jf", "Jp",
                "Qc", "Qq", "Qf", "Qp",
                "Kc", "Kq", "Kf", "Kp"
            ]
mazzo_reset=[
                "1c", "1q", "1f", "1p",
                "2c", "2q", "2f", "2p",
                "3c", "3q", "3f", "3p",
                "4c", "4q", "4f", "4p",
                "5c", "5q", "5f", "5p",
                "6c", "6q", "6f", "6p",
                "7c", "7q", "7f", "7p",
                "Jc", "Jq", "Jf", "Jp",
                "Qc", "Qq", "Qf", "Qp",
                "Kc", "Kq", "Kf", "Kp"
            ]

manoPlayerOne,  manoPlayerTwo   =   ["","",""]  ,  ["","",""]

tavolo=[]

mazzettoPlayerOne, mazzettoPlayerTwo=[],[]




def shuffle():
    random.shuffle(mazzo)

def start():
    distro()
    for i in range(4):
        tavolo.append(mazzo[0])
        del mazzo[0]


def distro():
    for i in range (3):
        manoPlayerOne[i]=mazzo[0]
        del mazzo[0]
        manoPlayerTwo[i]=mazzo[0]
        del mazzo[0]


def checkPickUp(player,carta):
    for i in range (len(tavolo)):
        for j in range(len(tavolo)):
            cont2=tavolo[j]
            if carta[0]==cont2[0]:
                if player==1:
                    print(f"il giocatore {player} ha preso {cont2} con {carta}")
                    mazzettoPlayerOne.append(carta)
                    mazzettoPlayerOne.append(cont2)
                    tavolo.remove(carta)
                    tavolo.remove(cont2)
                    break
                else:
                    print(f"il giocatore {player} ha preso {cont2} con {carta}")
                    mazzettoPlayerTwo.append(carta)
                    mazzettoPlayerTwo.append(cont2)
                    tavolo.remove(carta)
                    tavolo.remove(cont2)
                    break
    '''Aggiungi il sistema delle somme: salva in una variabile il valore dell aprima carta, poi cerca se ci son oatre carte che danno lo stesso valore sommate. Per ovviare a regina jack e re, metti un if che da al valore della carta 8,9,10'''


'''' aggiungi la "cattura finale" delle catte per l'ultima mano'''

'''aggiungi il sistema di conteggi punti ed il salvataggio degli stessi in un file '''

'''aggiungi l'interfaccia da terminale con i vari clear e l'indentazione da partita'''
    



def drop(player):
    inp=0
    while not 1<=inp<=len(manoPlayerTwo):
        inp=int(input(f"Giocatore{player} che carta vuoi giocare?"))
        if player==1:
            carta=manoPlayerOne[inp]
            del manoPlayerOne[inp-1]
            tavolo.append(carta)
            checkPickUp(player,carta)
        else:
            carta=manoPlayerTwo[inp]
            del manoPlayerTwo[inp-1]
            tavolo.append(carta)
            checkPickUp(player,carta)


shuffle()
start()
