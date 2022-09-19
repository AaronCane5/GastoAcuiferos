"""
cd OneDrive\Escritorio\Complejidad
env\Scripts\activate
py app.py
"""
from turtle import *


CONSUMPTION_PER_HOUSEHOLD = 1
CONSUMPTION_PER_FACTORY = 10

setup(900, 900, 0, 0)
speed(100)
title("Distribucion de agua")
    
def map():
    '''
        Funcion que el campo
        Entrada: 
            liters -> int
        Salida:
            Null
    '''
    colors = ["red", "green", "blue","yellow"]
    for color in range(len(colors)):
        pendown()
        goto(0,0)
        pencolor(colors[color])
        forward(500)
        left(90)
        penup()
    penup()
    
def draw_lake(liters, color):
    '''
        Funcion que dibuja el lago 
        Entrada: 
            liters -> int
        Salida:
            Null
    '''
    penup()
    print('Capacidad total del sistema acuifero: {}'.format(liters))
    right(90)
    goto(-liters/2,0)
    begin_fill()
    fillcolor(color)
    pencolor("brown")
    pendown()
    circle(liters/2)
    end_fill()
    penup()
    
def draw_house(total_houses):
    '''
        Funcion que dibuja las casas distribuidas en el plano de 900*900
        Entrada:
            total_houses -> int: Cantidad de casas a dibujar
        Salida:
            Null
    '''
    position = -400
    left(90)
    print('Total de Casas: {}'.format(total_houses))
    for house in range(total_houses):
        pencolor("DarkGoldenrod1")
        goto(position,250)
        pendown()
        #piso derecho
        begin_fill()
        fillcolor("DarkGoldenrod1")
        forward(50)
        #pared derecha
        left(90)
        forward(30)
        #techo derecho
        left(70)
        forward(52)
        #techo izquierdo
        left(40)
        forward(52)
        #pared izquierda
        left(70)
        forward(30)
        #piso izquierdo
        left(90)
        forward(50)
        end_fill()
        penup()
        position = position+200

def draw_factory(total_factory):
    '''
        Funcion que dibuja el fabricas 
        Entrada: 
            total_factory-> int: Cantidad de fabricas a dibujar
        Salida:
            Null
    '''
    print('Total de Fabricas: {}'.format(total_factory))
    penup()
    position = -400
    goto(position,-250)
    pencolor("cornsilk4")
    for factory in range(total_factory):
        goto(position,-250)
        pendown()
        begin_fill()
        fillcolor("cornsilk4")
        #piso derecho
        forward(50)
        #pared derecha
        left(90)  
        forward(30)
        #techo derecho
        left(90)
        forward(25)
        #1 pico
        right(45)
        forward(25)
        left(135)
        forward(18)
        for i in range(2):
            right(135)
            forward(25)
            left(135)
            forward(18)
        #pared izq
        right(135)
        forward(25)
        left(135)
        forward(47)
        #piso izq
        left(90)
        forward(50)
        end_fill()
        penup()
        position = position+200

def waste_calculation(total_houses,total_factory, liters)->int:
    '''
        Funcion que calcula el consmo total del del agua y determina el tiempo en que se acaba
        Entrada: 
            total_factory-> int: Cantidad de fabricas
            total_houses-> int: Cantidad de fabricas
            liters-> int: Cantidad de agua
        Salida:
            Null
    '''
    total_consumption_per_household = total_houses*CONSUMPTION_PER_HOUSEHOLD
    total_consumption_per_factory = total_factory*CONSUMPTION_PER_FACTORY
    total_consumption = total_consumption_per_household +total_consumption_per_factory
    print('Total de consumo: {}'.format(total_consumption))
    remaining_liters = liters
    time =0
    print('Anio **** Litros sobrantes **** ')
    while(remaining_liters>0):
        
        output = '{}    ****    {}'.format(time,remaining_liters)
        print(output)
        time = time+1
        remaining_liters = remaining_liters -total_consumption
    return time

def draw_flow(time):
    '''
        Funcion que grafica el tiempo en el cual se acaba el agua
        Entrada: 
            time-> int: Tiempo en el cual se acaba el agua
        Salida:
            Null
    '''
    print('Anios en los que se acaba el agua: {}'.format(time))
    goto(0,0)
    pencolor("blue")
    pendown()
    position =-450
    initial_point = (0,0)
    for house in range(total_houses):
        for year in range(time):
            penup()
            goto(initial_point)
            pendown()
            goto(position+(year*20), 250)
        position = position+200
    
    position =-450
    for house in range(total_factory):
        for year in range(time):
            penup()
            goto(initial_point)
            pendown()
            goto(position+(year*20), -200)  
        position = position+200
    draw_lake(liters,"white")
    
    

if __name__ == "__main__":
    print("Starting")
    liters = 200
    total_houses = 1 #max value: 5
    total_factory = 5 #max value: 5
    time = waste_calculation(total_houses,total_factory, liters)
   
    map()
    draw_lake(liters,"Blue")
    draw_house(total_houses)
    draw_factory(total_factory)
    draw_flow(time)
    texto = ' Capacidad total del sistema acuifero: {} \n Total de Casas: {} \n Total de Fabricas: {} \n Anios en los que se acaba el agua: {} \n'.format(liters,total_houses,total_factory,time)

    penup()
    goto(300,0)
    pendown()
    write(texto)
    done()