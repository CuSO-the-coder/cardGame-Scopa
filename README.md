# cardGame-scopa
Il gioco di carte "scopa" scritto in python

## Come funziona
Vi verrà chiesto il nome dei giocatori e a quanti punti far finire la partita, in seguito il gioco seguirà le regole standard che potete trovare a piè pagina.

### Il gioco
Vi verrà mostrata la seguente interfaccia:

carte nel mazzo: 30
************************

 ----  ----  ----  ----
| 2f || Jq || Kc || 5f |
 ----  ----  ----  ----

************************

poco più sotto vi sarà  la vostra mano, potrete quindi scegliere che carta giocare tra le 3 di cui disporrete.
Basterà digitare 1, 2 o 3 per giocare la carta.
Le catture seguiranno le regole qui sotto:

# Regole
Le regole della Scopa sono in apparenza molto semplici, e si basano sulla dinamica dei giochi di carte italiani. Ciascun giocatore seduto al tavolo o coppia, riceve 3 carte dal mazziere, che successivamente ripone quattro carte scoperte a terra e il restante mazzo di carte ancora inutilizzato vicino a se. 

Il giocatore primo di mano dovrà lanciare a terra una delle carte in proprio possesso. Calando una carta dello stesso valore di una presente a terra, quel giocatore prenderà entrambe le carte, riponendole di fronte a se nell'area dedicata alle carte conquistate. E' anche possibile calare una carta e prendere da terra due o più carte il cui valore sommato uguaglia il valore della carta lanciata. 

Quando a terra non rimane alcuna carta, a seguito di una presa, si dice che si è fatto "scopa". La scopa non può essere eseguita durante l'ultima mano dell'ultimo giocatore e quindi prima dell'esaurimento delle carte della smazzata in corso. Al termine del lancio delle tre carte dei giocatori, il mazziere distribuisce nuovamente tre carte a testa, senza però riporre nuovamente le quattro carte a terra, cosa che avviene sono nella prima mano di gioco.

Il punteggio

Alla fine della mano, ossia quando non rimangono più carte in mano ai giocatori, viene assegnato il punteggio secondo i seguenti schemi:

Ogni scopa totalizzata vale 1 punto

Settebello: il giocatore che ha conquistato la carta del 7 di denari riceve 1 punto in più, per se o per la coppia

Maggioranza delle carte: il giocatore o la coppia che ha conquistato 20 o più carte guadagna 1 punto. In caso la smazzata finisca in parità non vengono assegnati punti per le carte.

Denari: il giocatore o coppia che ha conquistato 5 o più carte del seme di denari guadagna un punto. Anche in questo caso, qualora vi fosse parità non si procede all'assegnazione di punti.

Primiera: il giocatore o la coppia che realizza la primiera guadagna un punto


La primiera è costituita dai punti conferiti della carta più alta che si ha per ogni seme. Il punteggio di ciascuna carta è dato come di seguito: 
 

il 7 vale 21 punti
il 6 vale 18 punti
l'Asso vale 16 punti
il 5 vale 15 punti
il 4 vale 14 punti
il 3 vale 13 punti
il 2 vale 12 punti
le figure valgono 10 punti

Per poter accedere alla primiera, oltre a totalizzare il punteggio di primiera più alto, è necessario possedere almeno una carta per ciascun seme di gioco, altrimenti la primiera sarà aggiudicata all'avversario, e in caso di parità di punteggio, la primiera non viene assegnata.

Obiettivo del gioco

Nel gioco della Scopa si deve raggiungere il punteggio prestabilito prima del proprio avversario. Normalmente questo punteggio è fissato ad 11 ma in alcuni tipi di torneo viene aumentato o diminuito secondo le esigenze. Al termine di ciascun round di gioco, si sommerà il punteggio dei partecipanti, con quello acquisito nei precedenti round. Qualora entrambi i giocatori o coppie raggiungessero o superassero gli 11 punti nello stesso round di gioco, vincerà il giocatore o la coppia che avrà totalizzato il punteggio più alto. In caso di punteggio in parità (esempio 12 a 12), si continuerà a giocare fino a che non sarà rotta la parità, e decretato così il vincitore.