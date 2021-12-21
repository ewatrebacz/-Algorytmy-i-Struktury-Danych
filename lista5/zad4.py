from turtle import *


def koch(step, approx):
    '''Move turtle to draw the Koch's curve
    @param step: size of step
    @param approx: level of approximation'''
    if approx == 0:

        forward(step)
        return

    step /= 3

    koch(step, approx - 1)
    left(60)
    koch(step, approx - 1)
    right(120)
    koch(step, approx - 1)
    left(60)
    koch(step, approx - 1)


def snow_flake(step, approx):
    '''Move turtle to draw the Koch's curve
    @param step: size of step
    @param approx: level of approximation'''

    speed(0)
    penup()
    backward(step/2)
    pendown()
    for i in range(3):
        koch(step, approx)
        right(120)
    mainloop()

   
snow_flake(300, 4)