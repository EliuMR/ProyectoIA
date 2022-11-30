# -*- coding: utf-8 -*-
"""
INAOE
Autor: Eliú Moreno Ramírez
Fecha: Noviembre 2022
Proyecto: Inteligencia Artificial
Consiste en la implementación de una variación gatoxgato el cual toma el algoritmo alpha beta para poder jugar humano-maquina
"""
#Librerías
import math
import time
#Creamos el tablero en forma de una matriz de 9x3x3
posiciones = [['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','','']]
#Variables iniciales
if True:
    infinity = math.inf
    puntajeGanador = infinity #Estableces con que puntaje se gana el juego
    scoreCelda = 20 #Tablero local ganado
    scoreFila = 3 #Aquellos que tienen dos marcas en una fila y sólo falta una marca para ganar en una raya
    scorePuntoSimple = 1 #Marca por cada marca hecha
    pesos = [1,1,1,1,1,1,1,1,1] #Pesos de cada tablero local, podría darse más peso a algunos tableros locales
    humano = 'o'
    cpu = 'x'  
def ChecarTablero(posicion): #Guarda las posiciones del tablero global
    tableroGlobal = ['','','','','','','','','']
    ganador = ''
    for i in range(len(posicion)):
        tableroLocal = posicion[i]
        #Comprobando si en cada "tableroLocal" y establece lo valores en el tablero global si gana
        if (tableroLocal[0] == "x" and tableroLocal[1] == "x" and tableroLocal[2] == "x") or (tableroLocal[3] == "x" and tableroLocal[4] == "x" and tableroLocal[5] == "x") or (tableroLocal[6] == "x" and tableroLocal[7] == "x" and tableroLocal[8] == "x") or (tableroLocal[0] == "x" and tableroLocal[3] == "x" and tableroLocal[6] == "x") or (tableroLocal[1] == "x" and tableroLocal[4] == "x" and tableroLocal[7] == "x") or (tableroLocal[2] == "x" and tableroLocal[5] == "x" and tableroLocal[8] == "x") or (tableroLocal[0] == "x" and tableroLocal[4] == "x" and tableroLocal[8] == "x") or (tableroLocal[2] == "x" and tableroLocal[4] == "x" and tableroLocal[6] == "x"):
            tableroGlobal[i] = "x"
        elif (tableroLocal[0] == "o" and tableroLocal[1] == "o" and tableroLocal[2] == "o") or (tableroLocal[3] == "o" and tableroLocal[4] == "o" and tableroLocal[5] == "o") or (tableroLocal[6] == "o" and tableroLocal[7] == "o" and tableroLocal[8] == "o") or (tableroLocal[0] == "o" and tableroLocal[3] == "o" and tableroLocal[6] == "o") or (tableroLocal[1] == "o" and tableroLocal[4] == "o" and tableroLocal[7] == "o") or (tableroLocal[2] == "o" and tableroLocal[5] == "o" and tableroLocal[8] == "o") or (tableroLocal[0] == "o" and tableroLocal[4] == "o" and tableroLocal[8] == "o") or (tableroLocal[2] == "o" and tableroLocal[4] == "o" and tableroLocal[6] == "o"):
            tableroGlobal[i] = "o"
        else:
            empate = True
            for celda in tableroLocal:
                if celda == '':
                    empate = False
                    break
            if empate:
                tableroGlobal[i] = 't'
    return tableroGlobal
#Comprobando si hay un ganador
def ChecarGanador(tableroGlobal):
    if (tableroGlobal[0] == "x" and tableroGlobal[1] == "x" and tableroGlobal[2] == "x") or (tableroGlobal[3] == "x" and tableroGlobal[4] == "x" and tableroGlobal[5] == "x") or (tableroGlobal[6] == "x" and tableroGlobal[7] == "x" and tableroGlobal[8] == "x") or (tableroGlobal[0] == "x" and tableroGlobal[3] == "x" and tableroGlobal[6] == "x") or (tableroGlobal[1] == "x" and tableroGlobal[4] == "x" and tableroGlobal[7] == "x") or (tableroGlobal[2] == "x" and tableroGlobal[5] == "x" and tableroGlobal[8] == "x") or (tableroGlobal[0] == "x" and tableroGlobal[4] == "x" and tableroGlobal[8] == "x") or (tableroGlobal[2] == "x" and tableroGlobal[4] == "x" and tableroGlobal[6] == "x"):
        return 'x'
    elif (tableroGlobal[0] == "o" and tableroGlobal[1] == "o" and tableroGlobal[2] == "o") or (tableroGlobal[3] == "o" and tableroGlobal[4] == "o" and tableroGlobal[5] == "o") or (tableroGlobal[6] == "o" and tableroGlobal[7] == "o" and tableroGlobal[8] == "o") or (tableroGlobal[0] == "o" and tableroGlobal[3] == "o" and tableroGlobal[6] == "o") or (tableroGlobal[1] == "o" and tableroGlobal[4] == "o" and tableroGlobal[7] == "o") or (tableroGlobal[2] == "o" and tableroGlobal[5] == "o" and tableroGlobal[8] == "o") or (tableroGlobal[0] == "o" and tableroGlobal[4] == "o" and tableroGlobal[8] == "o") or (tableroGlobal[2] == "o" and tableroGlobal[4] == "o" and tableroGlobal[6] == "o"):
        return 'o'
    else:
        return ''
#Para checar si es fin del juego
def GameOver(posiciones):
    suma=0
    tableroGlobal=ChecarTablero(posiciones)
    for i in range (9):
        if tableroGlobal[i]=='x' or tableroGlobal[i]=='o':
            suma=suma+1
    if (tableroGlobal[0] == "x" and tableroGlobal[1] == "x" and tableroGlobal[2] == "x") or (tableroGlobal[3] == "x" and tableroGlobal[4] == "x" and tableroGlobal[5] == "x") or (tableroGlobal[6] == "x" and tableroGlobal[7] == "x" and tableroGlobal[8] == "x") or (tableroGlobal[0] == "x" and tableroGlobal[3] == "x" and tableroGlobal[6] == "x") or (tableroGlobal[1] == "x" and tableroGlobal[4] == "x" and tableroGlobal[7] == "x") or (tableroGlobal[2] == "x" and tableroGlobal[5] == "x" and tableroGlobal[8] == "x") or (tableroGlobal[0] == "x" and tableroGlobal[4] == "x" and tableroGlobal[8] == "x") or (tableroGlobal[2] == "x" and tableroGlobal[4] == "x" and tableroGlobal[6] == "x"):
        return False
    elif (tableroGlobal[0] == "o" and tableroGlobal[1] == "o" and tableroGlobal[2] == "o") or (tableroGlobal[3] == "o" and tableroGlobal[4] == "o" and tableroGlobal[5] == "o") or (tableroGlobal[6] == "o" and tableroGlobal[7] == "o" and tableroGlobal[8] == "o") or (tableroGlobal[0] == "o" and tableroGlobal[3] == "o" and tableroGlobal[6] == "o") or (tableroGlobal[1] == "o" and tableroGlobal[4] == "o" and tableroGlobal[7] == "o") or (tableroGlobal[2] == "o" and tableroGlobal[5] == "o" and tableroGlobal[8] == "o") or (tableroGlobal[0] == "o" and tableroGlobal[4] == "o" and tableroGlobal[8] == "o") or (tableroGlobal[2] == "o" and tableroGlobal[4] == "o" and tableroGlobal[6] == "o"):
        return False
    elif suma==9:
        return False
    else:
        return True
#Verifica si cuando se llena el tablero local gano 'x' o 'x' o e un empate
def Ganador(posiciones):
    suma=0
    tableroGlobal=ChecarTablero(posiciones)
    for i in range (9):
        if tableroGlobal[i]=='x' or tableroGlobal[i]=='o':
            suma=suma+1
    if (tableroGlobal[0] == "x" and tableroGlobal[1] == "x" and tableroGlobal[2] == "x") or (tableroGlobal[3] == "x" and tableroGlobal[4] == "x" and tableroGlobal[5] == "x") or (tableroGlobal[6] == "x" and tableroGlobal[7] == "x" and tableroGlobal[8] == "x") or (tableroGlobal[0] == "x" and tableroGlobal[3] == "x" and tableroGlobal[6] == "x") or (tableroGlobal[1] == "x" and tableroGlobal[4] == "x" and tableroGlobal[7] == "x") or (tableroGlobal[2] == "x" and tableroGlobal[5] == "x" and tableroGlobal[8] == "x") or (tableroGlobal[0] == "x" and tableroGlobal[4] == "x" and tableroGlobal[8] == "x") or (tableroGlobal[2] == "x" and tableroGlobal[4] == "x" and tableroGlobal[6] == "x"):
        print ('Ganó la computadora')
    elif (tableroGlobal[0] == "o" and tableroGlobal[1] == "o" and tableroGlobal[2] == "o") or (tableroGlobal[3] == "o" and tableroGlobal[4] == "o" and tableroGlobal[5] == "o") or (tableroGlobal[6] == "o" and tableroGlobal[7] == "o" and tableroGlobal[8] == "o") or (tableroGlobal[0] == "o" and tableroGlobal[3] == "o" and tableroGlobal[6] == "o") or (tableroGlobal[1] == "o" and tableroGlobal[4] == "o" and tableroGlobal[7] == "o") or (tableroGlobal[2] == "o" and tableroGlobal[5] == "o" and tableroGlobal[8] == "o") or (tableroGlobal[0] == "o" and tableroGlobal[4] == "o" and tableroGlobal[8] == "o") or (tableroGlobal[2] == "o" and tableroGlobal[4] == "o" and tableroGlobal[6] == "o"):
        print ('Ganaste')
    elif suma==9:
        return print ('Es un empate')
#Función de evaluación
def CalcularScore(posiciones, tableroGlobal):
    score = 0
    for i in range(len(posiciones)):
        tableroLocal = posiciones[i]
        tableroLocalScore = 0 #Score inicial
        #verifica de quien es el turno para asignar el puntaje
        if tableroGlobal[i] == 'x':
            tableroLocalScore += scoreCelda
            score += tableroLocalScore * pesos[i]
            continue
        elif tableroGlobal[i] == 'o':
            tableroLocalScore -= scoreCelda
            score += tableroLocalScore * pesos[i]
            continue

        for celda in tableroLocal:
            if celda == 'x':
                tableroLocalScore += scorePuntoSimple
            elif celda == 'o':
                tableroLocalScore -= scorePuntoSimple

#Marcar todos los posibles 'dos en una fila con uno vacío' y da la puntuación correspondiente
        if (tableroLocal[0] == '' and tableroLocal[1] == 'x' and tableroLocal[2] == 'x') or (tableroLocal[0] == '' and tableroLocal[3] == 'x' and tableroLocal[6] == 'x') or (tableroLocal[0] == '' and tableroLocal[4] == 'x' and tableroLocal[8] == 'x'):
            tableroLocalScore += scoreFila
        if (tableroLocal[1] == '' and tableroLocal[0] == 'x' and tableroLocal[2] == 'x') or (tableroLocal[1] == '' and tableroLocal[4] == 'x' and tableroLocal[7] == 'x'):
            tableroLocalScore += scoreFila
        if (tableroLocal[2] == '' and tableroLocal[0] == 'x' and tableroLocal[1] == 'x') or (tableroLocal[2] == '' and tableroLocal[5] == 'x' and tableroLocal[8] == 'x') or (tableroLocal[2] == '' and tableroLocal[4] == 'x' and tableroLocal[6] == 'x'):
            tableroLocalScore += scoreFila
        if (tableroLocal[3] == '' and tableroLocal[4] == 'x' and tableroLocal[5] == 'x') or (tableroLocal[3] == '' and tableroLocal[0] == 'x' and tableroLocal[6] == 'x'):
            tableroLocalScore += scoreFila
        if (tableroLocal[4] == '' and tableroLocal[1] == 'x' and tableroLocal[7] == 'x') or (tableroLocal[4] == '' and tableroLocal[3] == 'x' and tableroLocal[5] == 'x') or (tableroLocal[4] == '' and tableroLocal[0] == 'x' and tableroLocal[8] == 'x') or (tableroLocal[4] == '' and tableroLocal[2] == 'x' and tableroLocal[6] == 'x'):
            tableroLocalScore += scoreFila
        if (tableroLocal[5] == '' and tableroLocal[3] == 'x' and tableroLocal[4] == 'x') or (tableroLocal[5] == '' and tableroLocal[2] == 'x' and tableroLocal[8] == 'x'):
            tableroLocalScore += scoreFila
        if (tableroLocal[6] == '' and tableroLocal[0] == 'x' and tableroLocal[3] == 'x') or (tableroLocal[6] == '' and tableroLocal[7] == 'x' and tableroLocal[8] == 'x') or (tableroLocal[6] == '' and tableroLocal[2] == 'x' and tableroLocal[4] == 'x'):
            tableroLocalScore += scoreFila
        if (tableroLocal[7] == '' and tableroLocal[1] == 'x' and tableroLocal[4] == 'x') or (tableroLocal[7] == '' and tableroLocal[6] == 'x' and tableroLocal[8] == 'x'):
            tableroLocalScore += scoreFila
        if (tableroLocal[8] == '' and tableroLocal[2] == 'x' and tableroLocal[5] == 'x') or (tableroLocal[8] == '' and tableroLocal[6] == 'x' and tableroLocal[7] == 'x') or (tableroLocal[8] == '' and tableroLocal[0] == 'x' and tableroLocal[4] == 'x'):
            tableroLocalScore += scoreFila

        if (tableroLocal[0] == '' and tableroLocal[1] == 'o' and tableroLocal[2] == 'o') or (tableroLocal[0] == '' and tableroLocal[3] == 'o' and tableroLocal[6] == 'o') or (tableroLocal[0] == '' and tableroLocal[4] == 'o' and tableroLocal[8] == 'o'):
            tableroLocalScore -= scoreFila
        if (tableroLocal[1] == '' and tableroLocal[0] == 'o' and tableroLocal[2] == 'o') or (tableroLocal[1] == '' and tableroLocal[4] == 'o' and tableroLocal[7] == 'o'):
            tableroLocalScore -= scoreFila
        if (tableroLocal[2] == '' and tableroLocal[0] == 'o' and tableroLocal[1] == 'o') or (tableroLocal[2] == '' and tableroLocal[5] == 'o' and tableroLocal[8] == 'o') or (tableroLocal[2] == '' and tableroLocal[4] == 'o' and tableroLocal[6] == 'o'):
            tableroLocalScore -= scoreFila
        if (tableroLocal[3] == '' and tableroLocal[4] == 'o' and tableroLocal[5] == 'o') or (tableroLocal[3] == '' and tableroLocal[0] == 'o' and tableroLocal[6] == 'o'):
            tableroLocalScore -= scoreFila
        if (tableroLocal[4] == '' and tableroLocal[1] == 'o' and tableroLocal[7] == 'o') or (tableroLocal[4] == '' and tableroLocal[3] == 'o' and tableroLocal[5] == 'o') or (tableroLocal[4] == '' and tableroLocal[0] == 'o' and tableroLocal[8] == 'o') or (tableroLocal[4] == '' and tableroLocal[2] == 'o' and tableroLocal[6] == 'o'):
            tableroLocalScore -= scoreFila
        if (tableroLocal[5] == '' and tableroLocal[3] == 'o' and tableroLocal[4] == 'o') or (tableroLocal[5] == '' and tableroLocal[2] == 'o' and tableroLocal[8] == 'o'):
            tableroLocalScore -= scoreFila
        if (tableroLocal[6] == '' and tableroLocal[0] == 'o' and tableroLocal[3] == 'o') or (tableroLocal[6] == '' and tableroLocal[7] == 'o' and tableroLocal[8] == 'o') or (tableroLocal[6] == '' and tableroLocal[2] == 'o' and tableroLocal[4] == 'o'):
            tableroLocalScore -= scoreFila
        if (tableroLocal[7] == '' and tableroLocal[1] == 'o' and tableroLocal[4] == 'o') or (tableroLocal[7] == '' and tableroLocal[6] == 'o' and tableroLocal[8] == 'o'):
            tableroLocalScore -= scoreFila
        if (tableroLocal[8] == '' and tableroLocal[2] == 'o' and tableroLocal[5] == 'o') or (tableroLocal[8] == '' and tableroLocal[6] == 'o' and tableroLocal[7] == 'o') or (tableroLocal[8] == '' and tableroLocal[0] == 'o' and tableroLocal[4] == 'o'):
            tableroLocalScore -= scoreFila

        score += tableroLocalScore * pesos[i]
    return score

#Funcion minimax
def minimax(posiciones, seleccion, profundidad, alpha, beta, maximizandoJugador):
    tablero = ChecarTablero(posiciones)#checa el estado del tablero
    ganador = ChecarGanador (tablero)
    # Verificamos si hay ganador en la profundidad y regresar el score
    if ganador == 'x':
        score = infinity 
        return score
    elif ganador == 'o':
        score = -infinity
        return score
    elif profundidad == 0:
        score = CalcularScore(posiciones, tablero)
        return score
    #Generando arbol para el jugador max
    if maximizandoJugador:
        maxEval = -infinity #Valor inicial a maximizar
##----------------------------------Creando los hijos----------------------------
        hijo_indice = []
        if tablero[seleccion] == '': #Checamos si esa posicion es vacia a la que se manda el tablero local
            hijo_indice.append(seleccion)#Guardamos esa posicion
        else:#cuando la posición a la que se manda del tablero local esta llena
            for i in range(len(tablero)):
                if tablero[i] == '':
                    hijo_indice.append(i)#guardamos las posiciones disponibles
        Break = False#Variable tipo bandera para terminar el minimax
        for indice in hijo_indice:
            for i in range(len(posiciones[indice])):
                if posiciones[indice][i] == '': #Verificamos que no esté ocupado
                    posiciones[indice][i] = cpu #como es turno de max guardamos su turno que es el de la computadora
                    seleccion = i#guardamos esa posicion
## ------------------------------------------Fin-----------------------------------
                    Eval = minimax(posiciones, seleccion, profundidad - 1, alpha, beta, False)#llamamos a la misma función pero para el jugador min
                    posiciones[indice][i] = ''
                    maxEval = max(maxEval, Eval)
                    alpha = max(alpha, Eval) #Guardamos nuevo valor para alpha
                    if beta <= alpha:#si se cumplen las codiciones para la poda se hace y termina la buqueda alli
                        Break = True
                        break
            if Break: 
                break
        return maxEval #retornamos el valor maximo
    #Generando arbol para el jugador min, todo es muy similar que para max
    else:
        minEval = infinity#Valor inicial a minimizar
##-----------------------------------Creando los hijos----------------------------
        hijo_indice = []
        if tablero[seleccion] == '':
            hijo_indice.append(seleccion)
        else:
            for i in range(len(tablero)):
                if tablero[i] == '':
                    hijo_indice.append(i)
        Break = False
        for indice in hijo_indice:
            for i in range(len(posiciones[indice])):
                if posiciones[indice][i] == '':
                    posiciones[indice][i] = humano
                    seleccion = i
## ------------------------------------------Fin-----------------------------------
                    Eval = minimax(posiciones, seleccion, profundidad - 1, alpha, beta, True)
                    posiciones[indice][i] = ''
                    minEval = min(minEval, Eval)
                    beta = min(beta, Eval) #Guardamos nuevo valor para beta
                    if beta <= alpha:#si se cumplen las codiciones para la poda se hace y termina la buqueda alli
                        Break = True
                        break
            if Break:
                break
        return minEval #regresamos el valor minimo
    
#En esta parte es para dibujar el tablero
def Dibujar(indiceSeleccionado):
    lineaAncho = 5
    cube = 5
    cuboColoreado = 10
    board_offset = 20
    display_offset = 15

    longitudTablero = [int(window_size[0]/3) - board_offset*2, int(window_size[1]/3) - board_offset*2]
    longitudDisplay = [int(window_size[0]/3) - display_offset*2, int(window_size[1]/3) - display_offset*2]
    #(50,50,50)
    win.fill((0,0,0))

    pygame.draw.line(win, (255,255,255),  (int(window_size[0]/3), 0),(int(window_size[0]/3), window_size[1]), lineaAncho)
    pygame.draw.line(win, (255,255,255),  (int(window_size[0]*2/3), 0),(int(window_size[0]*2/3), window_size[1]), lineaAncho)
    pygame.draw.line(win, (255,255,255),  (0, int(window_size[1]/3)),(window_size[0],int(window_size[1]/3)), lineaAncho)
    pygame.draw.line(win, (255,255,255),  (0, int(window_size[1]*2/3)),(window_size[0],int(window_size[1]*2/3)), lineaAncho)

    actualX = display_offset
    actualY = display_offset
    indice = 0

    tableroGlobal = ChecarTablero(posiciones)

    for i in range(3):
        for j in range(3):
            
            if indice in indiceSeleccionado:
                pygame.draw.rect(win, (0, 255, 0), ((actualX, actualY), longitudDisplay))
            if tableroGlobal[indice] == 'x':
                pygame.draw.rect(win, (40,40,255), ((actualX, actualY), longitudDisplay))
            if tableroGlobal[indice] == 'o':
                pygame.draw.rect(win, (255,40,40), ((actualX, actualY), longitudDisplay))
                
            indice += 1
            actualX += int(window_size[0]/3)
        actualY += int(window_size[1]/3)
        actualX = display_offset


    actualX = board_offset
    actualY = board_offset

    indiceTableroLleno = 0
    indiceTableroLocal = 0

    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    pygame.draw.rect(win, (255,255,255), ((actualX + longitudTablero[0] / 3 * l + cube, actualY + longitudTablero[1] / 3 * k + cube), (longitudTablero[0] / 3 - cube*2, longitudTablero[1] / 3 - cube*2)))
                    if posiciones[indiceTableroLleno][indiceTableroLocal] == 'x': 
                        #pygame.draw.rect(win, (40,40,255), ((actualX + longitudTablero[0] / 3 * l + cuboColoreado, actualY + longitudTablero[1] / 3 * k + cuboColoreado), (longitudTablero[0] / 3 - cuboColoreado*2, longitudTablero[1] / 3 - cuboColoreado*2)))
                        d=(board_offset-2)*2#Para mover a esquinas las dos rectas que harán la x
                        pygame.draw.line(win, (40,40,255), (actualX + longitudTablero[0] / 3 * l + cuboColoreado, actualY + longitudTablero[1] / 3 * k + cuboColoreado),((actualX + longitudTablero[0] / 3 * l + cuboColoreado)+d, (actualY + longitudTablero[1] / 3 * k + cuboColoreado)+d),6)
                        pygame.draw.line(win, (40,40,255), ((actualX + longitudTablero[0] / 3 * l + cuboColoreado), (actualY + longitudTablero[1] / 3 * k + cuboColoreado)+d),((actualX + longitudTablero[0] / 3 * l + cuboColoreado)+d, (actualY + longitudTablero[1] / 3 * k + cuboColoreado)),6)
                    if posiciones[indiceTableroLleno][indiceTableroLocal] == 'o':
                        #pygame.draw.rect(win, (255,40,40), ((actualX + longitudTablero[0] / 3 * l + cuboColoreado, actualY + longitudTablero[1] / 3 * k + cuboColoreado), (longitudTablero[0] / 3 - cuboColoreado*2, longitudTablero[1] / 3 - cuboColoreado*2)))
                        d=board_offset-2#Para dar el centro y el radio del circulo
                        pygame.draw.circle(win, (255,40,40), (((actualX + longitudTablero[0] / 3 * l + cuboColoreado)+d, (actualY + longitudTablero[1] / 3 * k + cuboColoreado)+d)),d+2,5)
                        
                    indiceTableroLocal += 1
            indiceTableroLleno += 1
            indiceTableroLocal = 0
            actualX += int(window_size[0]/3)
        actualY += int(window_size[1]/3)
        actualX = board_offset
        pygame.display.update()

import pygame
#Inicializamoes el tablero
pygame.init()
window_size = [620,620]
win = pygame.display.set_mode(window_size)
pygame.display.set_caption("Gato x Gato")
#Para guardar doonde se encuentran los clicks de mouse y poder guardarlo en el registro del tablero
click = False
seleccion = 0
clickIndice = [0,1,2,3,4,5,6,7,8]
Dibujar(clickIndice) #dibuja la marca del jugador correspondiente
while GameOver(posiciones)==True: #Se puede jugar mientras no se detecte el fin del juego
##--------Seguir jugando y guardar las posiciones-------
    inicio = time.time()
    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
    if click:
        click = False
        mouseX, mouseY = pygame.mouse.get_pos()
        tableroLocalX = int(mouseX / (window_size[0]/9))
        tableroLocalY = int(mouseY / (window_size[1]/9))
        tableroLocalX = tableroLocalX % 3
        tableroLocalY = tableroLocalY % 3
        tableroLocalIndice = tableroLocalY*3 + tableroLocalX
        tableroLlenoX = int(mouseX / (window_size[0]/3))
        tableroLlenoY = int(mouseY / (window_size[1]/3))        
        indiceTableroLleno = tableroLlenoY*3 + tableroLlenoX           
        if posiciones[indiceTableroLleno][tableroLocalIndice] == '' and indiceTableroLleno in clickIndice:
            posiciones[indiceTableroLleno][tableroLocalIndice] = humano
            seleccion = tableroLocalIndice
##----------------Activando minimax-------------------
            tablero = ChecarTablero(posiciones)
            maxEval = -infinity
            indiceHijos = []
            if tablero[seleccion] == '':
                indiceHijos.append(seleccion)
            else:
                for i in range(len(tablero)):
                    if tablero[i] == '':
                        indiceHijos.append(i)
            Dibujar(indiceHijos)
            Break = False
            for indice in indiceHijos:
                for i in range(len(posiciones[indice])):
                    if posiciones[indice][i] == '':
                        posiciones[indice][i] = cpu
                        seleccion = i
                            
                        Eval = minimax(posiciones, seleccion, 6, -infinity, infinity, False)
                        posiciones[indice][i] = ''
                        if Eval > maxEval:
                            maxEval = Eval
                            mejorMovimiento = [indice, i]
                                
            seleccion = mejorMovimiento[1]
            posiciones[mejorMovimiento[0]][mejorMovimiento[1]] = cpu               
        tablero = ChecarTablero(posiciones)
        clickIndice = []            
        if tablero[seleccion] == '':
            clickIndice.append(seleccion)
        else:
            for i in range(len(tablero)):
                if tablero[i] == '':
                    clickIndice.append(i)
        Dibujar(clickIndice)
        fin = time.time()
Ganador(posiciones)
print('Fin del Juego')
