"""
This module contains class Fraction and function returning the greatest common divisor.
Basic operations (+, -. * and /) can be performed on fractions.
Fractions can be compared.
Fractions are stored in their most abbreviated form.
"""
import math as m

def gcd(first, second):
    """Returns the greatest common divisor of two numbers"""
    if abs(first) < abs(second):
        first, second = second, first
    rest = first - int(first / second) * second
    if rest == 0:
        return abs(second)
    else:
        first, second = second, rest
        return gcd(first, second)

class Fraction:

    def __init__(self, num, den):
        if type(num) != int or type(den) != int:
            raise ValueError('Use only integers!')
        if den == 0:
            raise ZeroDivisionError("Denominator can't be zero!")
        if den < 0:
            self.num = -1 * num
            self.den = -1 * den
        else:
            self.num = num
            self.den = den
        if self.num != 0:
            dev = gcd(self.num,self.den)
            if dev != 1:
                self.num /= dev
                self.den /= dev

    def __add__(self, sec_frac):
        return Fraction(self.num * sec_frac.den + sec_frac.num * self.den, self.den * sec_frac.den)

    def __sub__(self, sec_frac):
        return Fraction(self.num * sec_frac.den - sec_frac.num * self.den, self.den * sec_frac.den)
    
    def __mul__(self, sec_frac):
        return Fraction(self.num * sec_frac.num, self.den * sec_frac.den)

    def __dev__(self, sec_frac):
        return Fraction(self.num * sec_frac.den, self.den * sec_frac.num)

    def __str__(self):
        return f'{int(self.num)}/{int(self.den)}'

    def __lt__(self, sec_frac):
        if self.num * sec_frac.den < sec_frac.num * self.den:
            return True
        else:
            return False

    def __le__(self, sec_frac):
        if self.num * sec_frac.den <= sec_frac.num * self.den:
            return True
        else:
            return False

    def __eq__(self, sec_frac):
            if self.num * sec_frac.den == sec_frac.num * self.den:
                return True
            else:
                return False
    
    def __ne__(self, sec_frac):
        if self.num * sec_frac.den != sec_frac.num * self.den:
            return True
        else:
            return False

    def __gt__(self, sec_frac):
        if self.num * sec_frac.den > sec_frac.num * self.den:
            return True
        else:
            return False

    def __ge__(self, sec_frac):
        if self.num * sec_frac.den >= sec_frac.num * self.den:
            return True
        else:
            return False

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den