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

carte_valori={
                "1"     :   1,
                "2"     :   2,
                "3"     :   3,
                "4"     :   4,
                "5"     :   5,
                "6"     :   6,
                "7"     :   7,
                "J"      :   8,
                "Q"    :    9,
                "K"     :    10
}

manoPlayerOne,  manoPlayerTwo   =   ["","",""]  ,  ["","",""]

tavolo=[]

mazzettoPlayerOne, mazzettoPlayerTwo=[],[]

player=1


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
            cartaDaControllare=tavolo[j]
            val_cartaDaControllare=carte_valori[cartaDaControllare[0]]
            val_cartaGiocatore=carte_valori[carta[0]]
            if val_cartaGiocatore==val_cartaDaControllare:
                if player==1:
                    print(f"il giocatore {player} ha preso {cartaDaControllare} con {carta}")
                    mazzettoPlayerOne.append(carta)
                    mazzettoPlayerOne.append(cartaDaControllare)
                    tavolo.remove(cartaDaControllare)
                    turnSwap(player,carta)
                else:
                    print(f"il giocatore {player} ha preso {cartaDaControllare} con {carta}")
                    mazzettoPlayerTwo.append(carta)
                    mazzettoPlayerTwo.append(cartaDaControllare)
                    tavolo.remove(cartaDaControllare)
                    turnSwap(player,carta)
#------------------------
    for i in range (len(tavolo)):
        for j in range(len(tavolo)):
            cartaDaControllare=tavolo[j]
            val_cartaDaControllare=carte_valori[cartaDaControllare[0]]
            val_cartaGiocatore=carte_valori[carta[0]]
            for t in range(len(tavolo)):
                cartaDaControllare2=tavolo[t]
                val_cartaDaControllare2=carte_valori[cartaDaControllare2[0]]
            if val_cartaGiocatore==val_cartaDaControllare+val_cartaDaControllare2:
                    if player==1:
                        print(f"il giocatore {player} ha preso {cartaDaControllare} e {cartaDaControllare2} con {carta}")
                        mazzettoPlayerOne.append(carta)
                        mazzettoPlayerOne.append(cartaDaControllare)
                        mazzettoPlayerOne.append(cartaDaControllare2)                           
                        tavolo.remove(cartaDaControllare)
                        tavolo.remove(cartaDaControllare2)
                        turnSwap(player,carta)
                    else:
                        print(f"il giocatore {player} ha preso {cartaDaControllare} e {cartaDaControllare2} con {carta}")
                        mazzettoPlayerTwo.append(carta)
                        mazzettoPlayerTwo.append(cartaDaControllare)
                        mazzettoPlayerTwo.append(cartaDaControllare2)                           
                        tavolo.remove(cartaDaControllare)
                        tavolo.remove(cartaDaControllare2)
                        turnSwap(player,carta)
#-----------------------    
    #aggiunig anche la somma a 3 carte
    
    turnSwap(player,carta)


def turnSwap(player, carta):
    if len(tavolo)==0:
        print(f"il giocatore {player} ha fatto scopa con {carta}")
    #aggiungi un sistema di conteggio delle scope
    if player==1:
        player=2
    else:
        player=1
    drop(player)
    
     
def drop(player):
   # tableView()
    inp=0
    if player==1:
        print(manoPlayerOne)
    else:
        print(manoPlayerTwo)
    while not 1<=inp<=len(manoPlayerTwo):
        inp=int(input(f"Giocatore {player} che carta vuoi giocare?"))
        if player==1:
            carta=manoPlayerOne[inp-1]
            del manoPlayerOne[inp-1]
            checkPickUp(player,carta)
        else:
            carta=manoPlayerTwo[inp-1]
            del manoPlayerTwo[inp-1]
            checkPickUp(player,carta)


shuffle()
start()
drop(player)


'''' aggiungi la "cattura finale" delle catte per l'ultima mano'''

'''aggiungi il sistema di conteggi punti ed il salvataggio degli stessi in un file '''

'''aggiungi l'interfaccia da terminale con i vari clear e l'indentazione da partita'''

''''aggiungi il rimescolamento delle carte '''

''''aggiungi la visualizzazione del tavolo'''

'''aggiungi "asso pigloa tutto" '''