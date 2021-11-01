import math, time

#Zadanie 2

#Version 1
def pitagoras(sides_sum):
    if type(sides_sum) == int and sides_sum > 0:
        for a in range(1, sides_sum):
            for b in range(1, sides_sum):
                for c in range(1, sides_sum):
                    if a**2 + b**2 == c**2 and a + b + c == sides_sum:
                        return (True, (a, b, c))
        return False
    else:
        raise ValueError('Incorrect argument! Choose a positive integer.')

#Version 2
def pitagoras2(sides_sum):
    if type(sides_sum) == int and sides_sum > 0:
        for a in range(1, sides_sum):
            for b in range(1, sides_sum):
                c = math.sqrt(a**2 + b**2)
                if int(c) == c  and a + b + c == sides_sum:
                    return (True, (a, b, int(c)))
        return False
    else:
        raise ValueError('Incorrect argument! Choose a positive integer.')

#Version 3
def pitagoras3(sides_sum):
    if type(sides_sum) == int and sides_sum > 0:
        for a in range(1, sides_sum):
            for b in range(1, a):
                c = math.sqrt(a**2 + b**2)
                if int(c) == c  and a + b + c == sides_sum:
                    return (True, (a, b, int(c)))
        return False
    else:
        raise ValueError('Incorrect argument! Choose a positive integer.')

#Version 4
def pitagoras4(sides_sum):
    if type(sides_sum) == int and sides_sum > 0:
        for a in range(1, int(sides_sum / 3)):
            for b in range(a + 1, int(sides_sum / 2)):
                c = sides_sum - a - b
                if c**2 == a**2 + b**2:
                    return (True, (a, b, c))
        return False
    else:
        raise ValueError('Incorrect argument! Choose a positive integer.')

#Version 5
def pitagoras5(sides_sum):
    if type(sides_sum) == int and sides_sum > 0:
        for a in range(1, int(sides_sum / 3)):
            b = (sides_sum**2 - 2*a*sides_sum)/(2*sides_sum - 2*a)
            c = sides_sum - a - b
            if b == int(b) and c**2 == a**2 + b**2:
                return (True, (a, b, c))
        return False
    else:
        raise ValueError('Incorrect argument! Choose a positive integer.')

#Zadanie 3

def pitagoras5(sides_sum):
    operations = 0
    if type(sides_sum) == int and sides_sum > 0:
        for a in range(1, int(sides_sum / 3)):
            b = (sides_sum**2 - 2*a*sides_sum)/(2*sides_sum - 2*a)
            c = sides_sum - a - b
            operations += 17
            if b == int(b) and c**2 == a**2 + b**2:
                return (True, (a, int(b), int(c)), operations)
        return False
    else:
        raise ValueError('Incorrect argument! Choose a positive integer.')

def pitagoras4(sides_sum):
    operations = 0
    if type(sides_sum) == int and sides_sum > 0:
        for a in range(1, int(sides_sum / 3)):
            for b in range(a + 1, int(sides_sum / 2)):
                c = sides_sum - a - b
                operations += 7
                if c**2 == a**2 + b**2:
                    return (True, (a, b, c), operations)
        return False
    else:
        raise ValueError('Incorrect argument! Choose a positive integer.')

def pitagoras3(sides_sum):
    operations = 0
    if type(sides_sum) == int and sides_sum > 0:
        for a in range(1, sides_sum):
            for b in range(1, a):
                c = math.sqrt(a**2 + b**2)
                operations += 9
                if int(c) == c  and a + b + c == sides_sum:
                    return (True, (a, b, int(c)), operations)
        return False
    else:
        raise ValueError('Incorrect argument! Choose a positive integer.')

def pitagoras2(sides_sum):
    operations = 0
    if type(sides_sum) == int and sides_sum > 0:
        for a in range(1, sides_sum):
            for b in range(sides_sum):
                c = math.sqrt(a**2 + b**2)
                operations += 9
                if int(c) == c  and a + b + c == sides_sum:
                    return (True, (a, b, int(c)), operations)
        return False
    else:
        raise ValueError('Incorrect argument! Choose a positive integer.')

def pitagoras(sides_sum):
    operations  = 0
    if type(sides_sum) == int and sides_sum > 0:
        for a in range(1, sides_sum):
            for b in range(1, sides_sum):
                for c in range(1, sides_sum):
                    operations += 9
                    if a**2 + b**2 == c**2 and a + b + c == sides_sum:
                        return (True, (a, b, c), operations)
        return False
    else:
        raise ValueError('Incorrect argument! Choose a positive integer.')

time1_1 = time.time()
p1 = pitagoras(1000)
time1_2 = time.time()

time2_1 = time.time()
p2 = pitagoras2(1000)
time2_2 = time.time()

time3_1 = time.time()
p3 = pitagoras3(1000)
time3_2 = time.time()

time4_1 = time.time()
p4 = pitagoras4(1000)
time4_2 = time.time()

time5_1 = time.time()
p5 = pitagoras5(1000)
time5_2 = time.time()

print(p5, f'time: {time5_2 - time5_1}')
print(p4, f'time: {time4_2 - time4_1}')
print(p3, f'time: {time3_2 - time3_1}')
print(p2, f'time: {time2_2 - time2_1}')
print(p1, f'time: {time1_2 - time1_1}')