def ordinary_polynomial_value_calc(coeff, arg):
    """Compute the value of the polynomial in the traditional way

@param coeff:(list) a list of the coefficients of the polynomial from degree zero upwards

@param arg: the point where we want to calculate the value of the polynomial

@return: result, the number of multiplications and the number of additions that have been made to obtain this result"""
    value = 0
    count_mult = 0
    count_add = 0
    for i in range(0,len(coeff)):
        value += arg**i * coeff[i]
        print(value)
        count_mult += i 
        count_add += 1
    return value, count_mult, count_add

def smart_polynomial_value_calc(coeff, arg):
    """Compute the value of the polynomial in a way that minimizes the number of multiplication performed

@param coeff:(list) a list of the coefficients of the polynomial from degree zero upwards

@param arg: the point where we want to calculate the value of the polynomial

@return: result, the number of multiplications and the number of additions that have been made to obtain this result"""
    coeff.reverse()
    value = arg * coeff[0]
    count_mult = 1
    count_add = 0
    for i in range(1,len(coeff)-1):
        value = (value + coeff[i]) * arg
        count_mult += 1
        count_add += 1
    value += coeff[-1]
    count_add += 1
    return value, count_mult, count_add