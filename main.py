#INICIALIZACIÓN DE VARIABLES
#CASILLAS
C1=0
C2=0
C3=0
C4=0
C5=0
C6=0
C7=0
C8=0
C9=0

#RONDA
ronda=0


    #SUBRUTINA TABLERO, DIBUJA EL TABLERO
def Tablero (C1,C2,C3,C4,C5,C6,C7,C8,C9):
    print("---------")
    print(C1,C2,C3)
    print(C4,C5,C6)
    print(C7,C8,C9)
    print("---------")

    #SUBRUTINA VICTORIA, REVISA SI HAY GANADOR Y FINALIZA EL JUEGO
def Victoria (ronda,C1,C2,C3,C4,C5,C6,C7,C8,C9):        #RECIBE POSICIONES COMO PARÁMETROS
            #Y RONDA

    if ((C1==C2 and C2==C3 and C3==1) or     #CONDICIONES DE VICTORIA
        (C4==C5 and C5==C6 and C6==1) or
        (C7==C8 and C8==C9 and C9==1) or
        (C1==C5 and C5==C9 and C9==1) or
        (C1==C5 and C5==C9 and C9==1) or
        (C1==C4 and C4==C7 and C7==1) or
        (C2==C5 and C5==C8 and C8==1) or
        (C2==C5 and C5==C8 and C8==1) or
        (C3==C6 and C6==C9 and C9==1)):      #SI LA CONDICIÓN SE CUMPLE CON EL UNO

            print ("Victoria para el Jugador 1")        #OUTPUT
            print("En ronda", ronda)        #OUTPUT

            Tablero(C1, C2, C3, C4, C5, C6, C7, C8, C9)  # SITUACIÓN DE VICTORIA
            return 1  # DEVUELVE RESULTADO

    if ((C1 == C2 and C2 == C3 and C3 == 2) or  # CONDICIONES DE VICTORIA
        (C4 == C5 and C5 == C6 and C6 == 2) or
        (C7 == C8 and C8 == C9 and C9 == 2) or
        (C1 == C5 and C5 == C9 and C9 == 2) or
        (C1 == C5 and C5 == C9 and C9 == 2) or
        (C1 == C4 and C4 == C7 and C7 == 2) or
        (C2 == C5 and C5 == C8 and C8 == 2) or
        (C2 == C5 and C5 == C8 and C8 == 2) or
        (C3 == C6 and C6 == C9 and C9 == 2)):       #SI LA CONDICIÓN SE CUMPLE CON EL 2

            print ("Victoria para el jugador 2")        #OUTPUT
            print("En ronda", ronda)        #OUTPUT

            Tablero(C1, C2, C3, C4, C5, C6, C7, C8, C9)  # SITUACIÓN DE VICTORIA
            return 1     #DEVUELVE RESULTADO


    if (not ((C1 == C2 and C2 == C3 and (C3 == 1 or C3 == 2)) or  # CONDICIONES DE NO VICTORIA
        (C4 == C5 and C5 == C6 and (C6 == 1 or C6 == 2)) or
        (C7 == C8 and C8 == C9 and (C9 == 1 or C9 == 2)) or
        (C1 == C5 and C5 == C9 and (C9 == 1 or C9 == 2)) or
        (C1 == C5 and C5 == C9 and (C9 == 1 or C9 == 2)) or
        (C1 == C4 and C4 == C7 and (C7 == 1 or C7 == 2)) or
        (C2 == C5 and C5 == C8 and (C8 == 1 or C8 == 2)) or
        (C2 == C5 and C5 == C8 and (C8 == 1 or C8 == 2)) or
        (C3 == C6 and C6 == C9 and (C9 == 1 or C9 == 2)))):
            return 0        #DEVUELVE RESULTADO



    #SUBRUTINA PLAY, CONTIENE EL JUEGO PRINCIPAL
def play (ronda,C1,C2,C3,C4,C5,C6,C7,C8,C9):        #RECIBE PARÁMETROS

    ronda=0     #INCIALIZA RONDA

    while (Victoria(ronda,C1,C2,C3,C4,C5,C6,C7,C8,C9) == 0):        #REPETIR RONDAS MIENTRAS NO HAYA GANADOR
        valid = 0       #INICIALIZAR VALID, VALIDA LA JUGADA

        Tablero(C1, C2, C3, C4, C5, C6, C7, C8, C9)     #SUBRUTINA TABLERO

        while (valid==0):       #MIENTRAS JUGADA NO SEA VÁLIDA
            play = int(input("Introduzca la casilla en la que quiere jugar: "))         #SOLICITA VALOR
            if ((play==1 and C1!=0) or      #CONDICIONES DE JUGADA NO VÁLIDA (CASILLA OCUPADA)
                (play==2 and C2!=0) or
                (play==3 and C3!=0) or
                (play==4 and C4!=0) or
                (play==5 and C5!=0) or
                (play==6 and C6!=0) or
                (play==7 and C7!=0) or
                (play==8 and C8!=0) or
                (play==9 and C9!=0) or
                play<1 or play>9):      #CASILLA NO EXISTENTE

                print ("La jugada no es válida, vuelva a jugar.")       #OUTPUT

            else:       #SI NO
                print ("Se jugará la casilla:",play)        #OUTPUT
                valid=1     #VALIDACIÓN

        if (play == 1):     #SI JUGADA ES CASILLA 1
            if (ronda%2==0):        #SI RONDA ES PAR (JUEGA EL 1)
                C1=1        #COLOCAR 1 EN CASILLA
            else:                   #SI NO ES PAR (JUEGA EL 2)
                C1=2        #COLOCAR 2 EN CASILLA

        #DE AQUÍ EN ADELANTE ES EL MISMO RAZONAMIENTO, UNO PARA CADA CASILLA.

        if (play == 2):
            if (ronda%2==0):
                C2=1
            else:
                C2=2

        if (play == 3):
            if (ronda%2==0):
                C3 = 1
            else:
                C3 = 2

        if (play == 4):
            if (ronda%2==0):
                C4 = 1
            else:
                C4 = 2

        if (play == 5):
            if (ronda%2==0):
                C5 = 1
            else:
                C5 = 2

        if (play == 6):
            if (ronda%2==0):
                C6 = 1
            else:
                C6 = 2

        if (play == 7):
            if (ronda%2==0):
                C7 = 1
            else:
                C7 = 2

        if (play == 8):
            if (ronda%2==0):
                C8 = 1
            else:
                C8 = 2

        if (play == 9):
            if (ronda%2==0):
                C9 = 1
            else:
                C9 = 2

        ronda = ronda + 1       #ACTUALIZA RONDA

play(ronda,C1,C2,C3,C4,C5,C6,C7,C8,C9)      #LLAMA SUBRUTINA PLAY (INICIO DE JUEGO)
