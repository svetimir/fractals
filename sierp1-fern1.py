#   ANIMATED FRACTAL DRAWING FUNCTIONS
#   AUTHOR: fluxoid, ifi@yandex.ru
#   VERSION: 0.0.0.1
#   LATEST REVISION: 01.07.2017

import turtle
import time
import random
import math

t=turtle.Pen()
t.speed('fastest')

def draw_point(x,y,color):
    x=math.ceil(x)
    y=math.ceil(y)
    t.penup()
    t.goto(x,y)
    t.color(color)
    t.pendown()
    t.down()
    t.circle(1)
    t.up()
    t.penup()
    return 0

#   SIERPINSKI TRIANGLE
#   Треугольник Серпинского
#   main
def draw_sierp():
    r=0
    x=0
    y=0
    steps=1e3
    factor=120
    for i in range(0,int(steps)):           
        r=random.randint(0,30)
        if r>20:
            x=0.5*x
            y=0.5*y
            draw_point(x,y,'red')
        elif r<=20:
            if r<=10:
                x=0.5*x+factor
                y=0.5*y+factor
                draw_point(x,y,'blue')
            elif r>10:
                x=0.5*x+factor
                y=0.5*y
                draw_point(x,y,'green')
    return 0


#   Папоротник Барнсли
#   BARNSLEY FERN
def draw_fern():
    r=0
    x=1.0
    y=0
    tmp=x
    steps=1e4
    scale=27
    for i in range(0,int(steps)):
        r=random.randint(0,100)
        tmp=x
        if r<=85:
            x=0.85*x+0.04*y
            y=-0.04*tmp+0.85*y+1.6
        elif r<=92:
            x=0.2*x-0.26*y
            y=0.23*tmp+0.22*y+1.6
        elif r<=99:
            x=-0.15*x+0.28*y
            y=0.26*tmp+0.24*y+0.44
        else:
            x=0.0
            y=0.16*y
        draw_point(scale*x,scale*y,'blue')
    return 0

draw_fern()
