from turtle import * 

def hilbert(aprox, direction, step):
    '''Make one sequence of movements
    @param aprox: level of approximation
    @param direction: angle by which the turtle should turn
    @param step: size of step'''

    if aprox == int(aprox) and aprox > 0:

        right(direction)
        hilbert(aprox - 1, -direction, step)
        forward(step)
        left(direction)
        hilbert(aprox - 1, direction, step)
        forward(step)
        hilbert(aprox - 1, direction, step)
        left(direction)
        forward(step)
        hilbert(aprox - 1, -direction, step)
        right(direction)
    
    else:
        return

def draw_hilbert(approx):
    '''Draw a hilbert curve using the turtle module
    @param apprpx: level of approximation'''

    size = 100
    penup()
    goto(-size / 2, size / 2)
    pendown()
    hilbert(approx, 90, size/(2**approx-1))
    done()

draw_hilbert(4)
