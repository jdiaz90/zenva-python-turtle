from turtle import *

def paint_shape(sides):

    for x in range(sides):
        forward(50)
        angle = 360 / sides
        right(angle)

paint_shape(8)

done()