import os
import random
import sys
import time
mazzo=[
                "1♥", "1♦", "1♣", "1♠",
                "2♥", "2♦", "2♣", "2♠",
                "3♥", "3♦", "3♣", "3♠",
                "4♥", "4♦", "4♣", "4♠",
                "5♥", "5♦", "5♣", "5♠",
                "6♥", "6♦", "6♣", "6♠",
                "7♥", "7♦", "7♣", "7♠",
                "J♥", "J♦", "J♣", "J♠",
                "Q♥", "Q♦", "Q♣", "Q♠",
                "K♥", "K♦", "K♣", "K♠"
            ]

mazzo_reset=[
                "1♥", "1♦", "1♣", "1♠",
                "2♥", "2♦", "2♣", "2♠",
                "3♥", "3♦", "3♣", "3♠",
                "4♥", "4♦", "4♣", "4♠",
                "5♥", "5♦", "5♣", "5♠",
                "6♥", "6♦", "6♣", "6♠",
                "7♥", "7♦", "7♣", "7♠",
                "J♥", "J♦", "J♣", "J♠",
                "Q♥", "Q♦", "Q♣", "Q♠",
                "K♥", "K♦", "K♣", "K♠"
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

tavolo, manoPlayerOne,  manoPlayerTwo , mazzettoPlayerOne, mazzettoPlayerTwo   = []  ,  []  ,  []  ,  []  ,  []

player=1

scopePlayerOne,scopePlayerTwo=0,0

lastPickup=0

ultimamano=False

nomeGiocatore1,nomeGiocatore2="",""

finePartita=0

def loading():
    for i in range(6):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n")
        print("Caricamento")
        print("° "*(i+1))
        time.sleep(0.5)
    
    time.sleep(1)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("\n\n")
    print("  ______   ______   ______  _______   ______  \n /      \ /      \ /      \|       \ /      \ \n|  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\  ▓▓▓▓▓▓\ \n| ▓▓___\▓▓ ▓▓   \▓▓ ▓▓  | ▓▓ ▓▓__/ ▓▓ ▓▓__| ▓▓\n \▓▓    \| ▓▓     | ▓▓  | ▓▓ ▓▓    ▓▓ ▓▓    ▓▓\n _\▓▓▓▓▓▓\ ▓▓   __| ▓▓  | ▓▓ ▓▓▓▓▓▓▓| ▓▓▓▓▓▓▓▓\n|  \__| ▓▓ ▓▓__/  \ ▓▓__/ ▓▓ ▓▓     | ▓▓  | ▓▓\n \▓▓    ▓▓\▓▓    ▓▓\▓▓    ▓▓ ▓▓     | ▓▓  | ▓▓\n  \▓▓▓▓▓▓  \▓▓▓▓▓▓  \▓▓▓▓▓▓ \▓▓      \▓▓   \▓▓")
    print("-------------------")
    print("╔═══╗    ╔═══╗╔═══╗\n║╔═╗║    ║╔═╗║║╔═╗║\n║║ ╚╝╔╗╔╗║╚══╗║║ ║║\n║║ ╔╗║║║║╚══╗║║║ ║║\n║╚═╝║║╚╝║║╚═╝║║╚═╝║\n╚═══╝╚══╝╚═══╝╚═══╝")
    print("-------------------")
    time.sleep(2.4)

    os.system('cls' if os.name == 'nt' else 'clear')

def reset():
    os.system('cls' if os.name == 'nt' else 'clear')
    mazzo=mazzo_reset
    tavolo, manoPlayerOne,  manoPlayerTwo , mazzettoPlayerOne, mazzettoPlayerTwo   = []  ,  []  ,  []  ,  []  ,  []
    scopePlayerOne,scopePlayerTwo=0,0
    lastPickup=0
    ultimamano=False
    print(f"Eseguo il reset: \nmazzo={mazzo};\ntavolo={tavolo}; \nmanoPlayerOne={manoPlayerOne};\nmanoPlayerTwo={manoPlayerTwo}\nmazzettoPlayerOne={mazzettoPlayerOne};\nmazzettoPlayerTwo={mazzettoPlayerTwo};\nscopePlayerOne={scopePlayerOne};\nscopePlayerTwo={scopePlayerTwo};\nlastPickup={lastPickup};\nultimamano={ultimamano}")
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

def askBeforeStart(nomeGiocatore1,nomeGiocatore2,finePartita):
    while nomeGiocatore1=="":
        nomeGiocatore1=input("Giocatore1, come ti chiami?\n")
    while nomeGiocatore2=="":
        nomeGiocatore2=input("Giocatore2, come ti chiami?\n")
    while finePartita==0:
        finePartita=int(input("A quanti punti volete che la partita finisca? (solitamente si gioca a 11 o 21 punti)\n"))
    print(f"Ottimo, benvenuti {nomeGiocatore1} e {nomeGiocatore2}, che vinca il migliore")   

def tableView():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"carte nel mazzo: {len(mazzo)}")
    print("******"*len(tavolo),end="\n")
    print()
    print(" ---- "*len(tavolo))
    for ele in tavolo:
        print("|",end=" ")
        print(ele,end=" |")      
    print()
    print(" ---- "*len(tavolo))
    print()
    print("******"*len(tavolo))
    print()
    print("la tua mano:")

def shuffle():
    random.shuffle(mazzo)

def start():
    shuffle()
    distro()
    for _ in range(4):
        tavolo.append(mazzo[0])
        del mazzo[0]
    drop(player)

def distro():
    for i in range (3):
        manoPlayerOne.append(mazzo[0])
        del mazzo[0]
        manoPlayerTwo.append(mazzo[0])
        del mazzo[0]

def checkPickUp(player,carta):
    if len(tavolo)>=1:
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
                    lastPickup=1
                    turnSwap(player,carta,ultimamano,scopePlayerOne,scopePlayerTwo)
                else:
                    print(f"il giocatore {player} ha preso {cartaDaControllare} con {carta}")
                    mazzettoPlayerTwo.append(carta)
                    mazzettoPlayerTwo.append(cartaDaControllare)
                    tavolo.remove(cartaDaControllare)
                    lastPickup=2
                    turnSwap(player,carta,ultimamano,scopePlayerOne,scopePlayerTwo)
#------------------------
    if len(tavolo)>=2:
        for j in range(len(tavolo)-1):
            cartaDaControllare=tavolo[j]
            val_cartaDaControllare=carte_valori[cartaDaControllare[0]]
            val_cartaGiocatore=carte_valori[carta[0]]
            for t in range(j+1, len(tavolo)):
                cartaDaControllare2=tavolo[t]
                val_cartaDaControllare2=carte_valori[cartaDaControllare2[0]]
            if val_cartaGiocatore==(val_cartaDaControllare+val_cartaDaControllare2):
                    if player==1:
                        print(f"il giocatore {player} ha preso {cartaDaControllare} e {cartaDaControllare2} con {carta}")
                        mazzettoPlayerOne.append(carta)
                        mazzettoPlayerOne.append(cartaDaControllare)
                        mazzettoPlayerOne.append(cartaDaControllare2)                           
                        tavolo.remove(cartaDaControllare)
                        tavolo.remove(cartaDaControllare2)
                        lastPickup=1
                        turnSwap(player,carta,ultimamano,scopePlayerOne,scopePlayerTwo)
                    else:
                        print(f"il giocatore {player} ha preso {cartaDaControllare} e {cartaDaControllare2} con {carta}")
                        mazzettoPlayerTwo.append(carta)
                        mazzettoPlayerTwo.append(cartaDaControllare)
                        mazzettoPlayerTwo.append(cartaDaControllare2)                           
                        tavolo.remove(cartaDaControllare)
                        tavolo.remove(cartaDaControllare2)
                        lastPickup=2
                        turnSwap(player,carta,ultimamano,scopePlayerOne,scopePlayerTwo)
#-----------------------    
    if len(tavolo)>=3:
        for j in range(len(tavolo)-2):
            cartaDaControllare=tavolo[j]
            val_cartaDaControllare=carte_valori[cartaDaControllare[0]]
            val_cartaGiocatore=carte_valori[carta[0]]
            for t in range(j+1, len(tavolo)-1):
                cartaDaControllare2=tavolo[t]
                val_cartaDaControllare2=carte_valori[cartaDaControllare2[0]]
                for i in range (t+1, len(tavolo)):
                    cartaDaControllare3=tavolo[i]
                    val_cartaDaControllare3=carte_valori[cartaDaControllare3[0]]
                if val_cartaGiocatore==(val_cartaDaControllare+val_cartaDaControllare2+val_cartaDaControllare3):
                        if player==1:
                            print(f"il giocatore {player} ha preso {cartaDaControllare} e {cartaDaControllare2} e {cartaDaControllare3} con {carta}")
                            mazzettoPlayerOne.append(carta)
                            mazzettoPlayerOne.append(cartaDaControllare)
                            mazzettoPlayerOne.append(cartaDaControllare2)    
                            mazzettoPlayerOne.append(cartaDaControllare3)                         
                            tavolo.remove(cartaDaControllare)
                            tavolo.remove(cartaDaControllare2)
                            tavolo.remove(cartaDaControllare3)
                            lastPickup=1
                            turnSwap(player,carta,ultimamano,scopePlayerOne,scopePlayerTwo)
                        else:
                            print(f"il giocatore {player} ha preso {cartaDaControllare} e {cartaDaControllare2} e {cartaDaControllare3} con {carta}")
                            mazzettoPlayerTwo.append(carta)
                            mazzettoPlayerTwo.append(cartaDaControllare)
                            mazzettoPlayerTwo.append(cartaDaControllare2)                           
                            mazzettoPlayerTwo.append(cartaDaControllare3)                           
                            tavolo.remove(cartaDaControllare)
                            tavolo.remove(cartaDaControllare2)
                            tavolo.remove(cartaDaControllare3)
                            lastPickup=2
                            turnSwap(player,carta,ultimamano,scopePlayerOne,scopePlayerTwo)
#-----------------------   
    if len(tavolo)>=4:
        for j in range(len(tavolo)-3):
            cartaDaControllare=tavolo[j]
            val_cartaDaControllare=carte_valori[cartaDaControllare[0]]
            val_cartaGiocatore=carte_valori[carta[0]]
            for t in range(j+1, len(tavolo)-2):
                cartaDaControllare2=tavolo[t]
                val_cartaDaControllare2=carte_valori[cartaDaControllare2[0]]
                for i in range (t+1, len(tavolo)-1):
                    cartaDaControllare3=tavolo[i]
                    val_cartaDaControllare3=carte_valori[cartaDaControllare3[0]]
                    for w in range(i+1, len(tavolo)):
                        cartaDaControllare4=tavolo[w]
                        val_cartaDaControllare4=carte_valori[cartaDaControllare4[0]]
                        if val_cartaGiocatore==(val_cartaDaControllare+val_cartaDaControllare2+val_cartaDaControllare3+val_cartaDaControllare4):
                                if player==1:
                                    print(f"il giocatore {player} ha preso {cartaDaControllare} e {cartaDaControllare2} e {cartaDaControllare3} e {cartaDaControllare4} con {carta}")
                                    mazzettoPlayerOne.append(carta)
                                    mazzettoPlayerOne.append(cartaDaControllare)
                                    mazzettoPlayerOne.append(cartaDaControllare2)    
                                    mazzettoPlayerOne.append(cartaDaControllare3)                         
                                    mazzettoPlayerOne.append(cartaDaControllare4)                         
                                    tavolo.remove(cartaDaControllare)
                                    tavolo.remove(cartaDaControllare2)
                                    tavolo.remove(cartaDaControllare3)
                                    tavolo.remove(cartaDaControllare4)
                                    lastPickup=1
                                    turnSwap(player,carta,ultimamano,scopePlayerOne,scopePlayerTwo)
                                else:
                                    print(f"il giocatore {player} ha preso {cartaDaControllare} e {cartaDaControllare2} e {cartaDaControllare3} e {cartaDaControllare4} con {carta}")
                                    mazzettoPlayerTwo.append(carta)
                                    mazzettoPlayerTwo.append(cartaDaControllare)
                                    mazzettoPlayerTwo.append(cartaDaControllare2)                           
                                    mazzettoPlayerTwo.append(cartaDaControllare3)                           
                                    mazzettoPlayerTwo.append(cartaDaControllare4)                           
                                    tavolo.remove(cartaDaControllare)
                                    tavolo.remove(cartaDaControllare2)
                                    tavolo.remove(cartaDaControllare3)
                                    tavolo.remove(cartaDaControllare4)
                                    lastPickup=2
                                    turnSwap(player,carta,ultimamano,scopePlayerOne,scopePlayerTwo)
    tavolo.append(carta)
    turnSwap(player,carta,ultimamano,scopePlayerOne,scopePlayerTwo)

def lastChance(tavolo):
    if lastPickup==1:
        for ele in tavolo:
            mazzettoPlayerOne.append(ele)
        print(f"essendo l'ultima mano, il giocatore 1 prende {tavolo}")
        tavolo=[]
    else:
        for ele in tavolo:
            mazzettoPlayerTwo.append(ele)
        print(f"essendo l'ultima mano, il giocatore 2 prende {tavolo}")
        tavolo=[]
    scoreCheck()
    
def turnSwap(player, carta, ultimamano,scopePlayerOne,scopePlayerTwo):
    if len(mazzo)==0 and len(manoPlayerOne)==0:
        ultimamano=True
    if len(tavolo)==0 and ultimamano==False:
        print(f"il giocatore {player} ha fatto scopa con {carta}")
        if player==1:
            scopePlayerOne+=1
        else:
            scopePlayerTwo+=1
    if player==1:
        player=2
    else:
        player=1
    if len(manoPlayerTwo)==0 and len(mazzo)>=6:
        distro()
    if len(manoPlayerTwo)==0 and ultimamano==True:
        lastChance(tavolo)
    #time.sleep(1.3)
    drop(player)
     
def drop(player):
    tableView()
    inp=0
    if player==1:
        print(manoPlayerOne,end="\n\n")
    else:
        print(manoPlayerTwo,end="\n\n")
    while not 1<=inp<=len(manoPlayerTwo) and inp!=" ":
        inp=int(input(f"Giocatore {player} che carta vuoi giocare?"))
    if player==1:
        carta=manoPlayerOne[inp-1]
        del manoPlayerOne[inp-1]
        checkPickUp(player,carta)
    else:
        carta=manoPlayerTwo[inp-1]
        del manoPlayerTwo[inp-1]
        checkPickUp(player,carta)

def carte():
    if len(mazzettoPlayerOne) >20:
        return(1)
    elif len(mazzettoPlayerOne)==20:
        return("patta")
    else:
        return(2)

def ori():
    ori=0
    for ele in mazzettoPlayerOne:
        if ele[1]=="♦":
            ori+=1
    if ori>5:
        return(1)
    elif ori==5:
        return("patta")
    else:
        return(2)

def settebello():
    if "7♦" in mazzettoPlayerOne:
        return(1)
    else:
        return(2)

def primiera():
    q, p, c, f=False , False, False, False 
    puntiPrimiera1=0
    puntiPrimiera2=0 
    for ele in mazzettoPlayerOne:
        if ele[0]=="7":
            if ele[1]=="♦" and q==False:
                q=True
                puntiPrimiera1+=21
            if ele[1]=="♠" and p==False:
                p=True
                puntiPrimiera1+=21
            if ele[1]=="♥" and c==False:
                c=True
                puntiPrimiera1+=21
            if ele[1]=="♣" and f==False:
                c=True
                puntiPrimiera1+=21
    if puntiPrimiera1<70:
        for ele in mazzettoPlayerOne:
            if ele[0]=="6":
                if ele[1]=="♦" and q==False:
                    q=True
                    puntiPrimiera1+=18
                if ele[1]=="♠" and p==False:
                    p=True
                    puntiPrimiera1+=18
                if ele[1]=="♥" and c==False:
                    c=True
                    puntiPrimiera1+=18
                if ele[1]=="♣" and f==False:
                    c=True
                    puntiPrimiera1+=18
    if puntiPrimiera1<70:
        for ele in mazzettoPlayerOne:
            if ele[0]=="1":
                if ele[1]=="♦" and q==False:
                    q=True
                    puntiPrimiera1+=16
                if ele[1]=="♠" and p==False:
                    p=True
                    puntiPrimiera1+=16
                if ele[1]=="♥" and c==False:
                    c=True
                    puntiPrimiera1+=16
                if ele[1]=="♣" and f==False:
                    c=True
                    puntiPrimiera1+=16
    
    q, p, c, f=False , False, False, False 
    for ele in mazzettoPlayerTwo:
        if ele[0]=="7":
            if ele[1]=="♦" and q==False:
                q=True
                puntiPrimiera2+=21
            if ele[1]=="♠" and p==False:
                p=True
                puntiPrimiera2+=21
            if ele[1]=="♥" and c==False:
                c=True
                puntiPrimiera2+=21
            if ele[1]=="♣" and f==False:
                c=True
                puntiPrimiera2+=21
    if puntiPrimiera2<70:
        for ele in mazzettoPlayerTwo:
            if ele[0]=="6":
                if ele[1]=="♦" and q==False:
                    q=True
                    puntiPrimiera2+=18
                if ele[1]=="♠" and p==False:
                    p=True
                    puntiPrimiera2+=18
                if ele[1]=="♥" and c==False:
                    c=True
                    puntiPrimiera2+=18
                if ele[1]=="♣" and f==False:
                    c=True
                    puntiPrimiera2+=18
    if puntiPrimiera2<70:
        for ele in mazzettoPlayerOne:
            if ele[0]=="1":
                if ele[1]=="♦" and q==False:
                    q=True
                    puntiPrimiera2+=16
                if ele[1]=="♠" and p==False:
                    p=True
                    puntiPrimiera2+=16
                if ele[1]=="♥" and c==False:
                    c=True
                    puntiPrimiera2+=16
                if ele[1]=="♣" and f==False:
                    c=True
                    puntiPrimiera2+=16
    
    if puntiPrimiera1>puntiPrimiera2:
        return(1)
    elif puntiPrimiera1<puntiPrimiera2:
        return(2)
    else:
        return("patta")            

def scoreCheck():
    os.system('cls' if os.name == 'nt' else 'clear')
    f=open("cache.txt", "r")
    l=f.readlines()
    if len(l)==4:
        puntiTotPlayerOne=int(l[1])
        puntiTotPlayerTwo=int(l[3])
    else:
        puntiTotPlayerOne=0
        puntiTotPlayerTwo=0
    
    puntoCarte=carte()
    puntoOri=ori()
    puntoSettebello=settebello()
    puntoPrimiera=primiera()

    punteggi=[puntoCarte, puntoOri, puntoSettebello, puntoSettebello]
    
    for ele in punteggi:
        if ele==1:
            puntiTotPlayerOne+=1
        elif ele==2:
            puntiTotPlayerTwo+=1

    puntiTotPlayerOne+=scopePlayerOne
    puntiTotPlayerTwo+=scopePlayerTwo


    print(f"Ecco i risultati della partita:")
    print(f"Carte\t{puntoCarte}")
    print(f"Ori\t{puntoOri}")
    print(f"Settebello\t{puntoSettebello}")
    print(f"Primiera\t{puntoPrimiera}")
    print(f"Scope giocatore1\t{scopePlayerOne}")
    print(f"Scope giocatore2\t{scopePlayerTwo}")
    f.close()
    f=open("cache.txt","w")
    f.write("Punti giocatore1:\n")
    f.write(str(puntiTotPlayerOne)+"\n")
    
    f.write("Punti giocatore2:\n")
    f.write(str(puntiTotPlayerTwo)+"\n")

    f.close()
    f=open("cache.txt", "r")
    l=f.readlines()
    puntiPartitaP1=l[1]
    puntiPartitaP2=l[3]
    if puntiPartitaP1 or puntiPartitaP2>=finePartita:
        os.system('cls' if os.name == 'nt' else 'clear')
        if puntiPartitaP1>puntiPartitaP2:
            print(f"Complimenti {nomeGiocatore1}, hai vinto contro {nomeGiocatore2} con un totale di {puntiPartitaP1} a {puntiPartitaP2}!")
            sys.exit()
    else:
        print(f"Il vostro punteggio è di {puntiPartitaP1} a {puntiPartitaP2} per {nomeGiocatore1}")
        risp=""
        while risp !="sì"or risp!="no" or risp!="si":
            risp=input("Volete continuare a giocare?\n")
            risp=risp.lower()
        if risp=="sì" or risp=="si":
            print("Ottimo!")
            replay()
        elif risp=="no":
            print("Va bene, allora dite addio ai vostri progressi :) ")
            destroy()
    
def destroy():
    f=open("cache.txt", "w")
    f.close()

def replay():
    reset()
    start()

def main():
    loading()
    askBeforeStart(nomeGiocatore1,nomeGiocatore2,finePartita)
    start()

if __name__ == "__main__":
    main()