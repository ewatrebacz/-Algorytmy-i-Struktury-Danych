"""
This module contains class Fraction, function returning the greatest common divisor and function turning integers and floats into fractions.
Basic operations (+, -. * and /) can be performed on fractions also with ints and floats (exapmle 2 * Fraction(1,2)).
Fractions can be compared.
Fractions are stored in their most abbreviated form.
If mixed = True fractions as printed as a mixed number (example Fraction(5,2) ==> 2,(1/2))
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

def trans_to_frac(number, den): 
    """Turns integers and floats into fractions

    @param numer:(int or float) number to change, goes to the nominator

    @param den:(int) should always be 1, otherwise the result won't be equal to the number

    @return:(Fraction) fraction"""
    if len(str(number)) <= 10**6 and len(str(den)) <= 10**6:
        if number == int(number):
            return Fraction_ext(int(number), int(den))
        else:
            return trans_to_frac(10 * number, 10 * den)
    else:
        raise ValueError('Arguments are too long!')

class Fraction_ext:

    mixed = False

    def __init__(self, num, den):
        if type(num) != int or type(den) != int:
            frac = trans_to_frac(num, den)
            self.num = frac.num
            self.den = frac.den
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
        if type(sec_frac) != Fraction_ext:
            sec_frac = trans_to_frac(sec_frac, 1)
        return Fraction_ext(self.num * sec_frac.den + sec_frac.num * self.den, self.den * sec_frac.den)

    def __radd__(self, sec_frac):
        if type(sec_frac) != Fraction_ext:
            sec_frac = trans_to_frac(sec_frac, 1)
        return Fraction_ext(self.num * sec_frac.den + sec_frac.num * self.den, self.den * sec_frac.den)

    def __sub__(self, sec_frac):
        if type(sec_frac) != Fraction_ext:
            sec_frac = trans_to_frac(sec_frac, 1)
        return Fraction_ext(self.num * sec_frac.den - sec_frac.num * self.den, self.den * sec_frac.den)

    def __rsub__(self, sec_frac):
        if type(sec_frac) != Fraction_ext:
            sec_frac = trans_to_frac(sec_frac, 1)
        return Fraction_ext(self.num * sec_frac.den - sec_frac.num * self.den, self.den * sec_frac.den)
    
    def __mul__(self, sec_frac):
        if type(sec_frac) != Fraction_ext:
            sec_frac = trans_to_frac(sec_frac, 1)
        return Fraction_ext(self.num * sec_frac.num, self.den * sec_frac.den)
    
    def __rmul__(self, sec_frac):
        if type(sec_frac) != Fraction_ext:
            sec_frac = trans_to_frac(sec_frac, 1)
        return Fraction_ext(self.num * sec_frac.num, self.den * sec_frac.den)

    def __truediv__(self, sec_frac):
        if type(sec_frac) != Fraction_ext:
            sec_frac = trans_to_frac(sec_frac, 1)
        return Fraction_ext(self.num * sec_frac.den, self.den * sec_frac.num)
    
    def __rtruediv__(self, sec_frac):
        if type(sec_frac) != Fraction_ext:
            sec_frac = trans_to_frac(sec_frac, 1)
        return Fraction_ext(self.den * sec_frac.num, self.num * sec_frac.den)

    def __str__(self):
        if Fraction_ext.mixed == True:
            num = abs(self.num)
            den = abs(self.den)
            if num > den:
                if self.num < 0:
                    return f'-{num // den},({num % den}/{den})'
                else:
                    return f'{num // den},({num % den}/{den})'
            else:
                return f'{int(self.num)}/{int(self.den)}'
        else:
                return f'{int(self.num)}/{int(self.den)}'

    def __lt__(self, sec_frac):
        if type(sec_frac) != Fraction_ext:
            sec_frac = trans_to_frac(sec_frac, 1)
        if self.num * sec_frac.den < sec_frac.num * self.den:
            return True
        else:
            return False

    def __le__(self, sec_frac):
        if type(sec_frac) != Fraction_ext:
            sec_frac = trans_to_frac(sec_frac, 1)
        if self.num * sec_frac.den <= sec_frac.num * self.den:
            return True
        else:
            return False

    def __eq__(self, sec_frac):
        if type(sec_frac) != Fraction_ext:
            sec_frac = trans_to_frac(sec_frac, 1)
        if self.num * sec_frac.den == sec_frac.num * self.den:
            return True
        else:
            return False
    
    def __ne__(self, sec_frac):
        if type(sec_frac) != Fraction_ext:
            sec_frac = trans_to_frac(sec_frac, 1)
        if self.num * sec_frac.den != sec_frac.num * self.den:
            return True
        else:
            return False

    def __gt__(self, sec_frac):
        if type(sec_frac) != Fraction_ext:
            sec_frac = trans_to_frac(sec_frac, 1)
        if self.num * sec_frac.den > sec_frac.num * self.den:
            return True
        else:
            return False

    def __ge__(self, sec_frac):
        if type(sec_frac) != Fraction_ext:
            sec_frac = trans_to_frac(sec_frac, 1)
        if self.num * sec_frac.den >= sec_frac.num * self.den:
            return True
        else:
            return False

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den