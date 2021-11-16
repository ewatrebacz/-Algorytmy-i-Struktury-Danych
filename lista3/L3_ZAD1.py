def binom(a, b):
    """Count binom without multiplication."""
    if a < b:
        return 0
    elif a == b or b == 0:
        return 1
    else:
        return binom(a - 1, b - 1) + binom(a - 1, b)

def exp_by_squ(a,b):
    """Count b to the power of a making less multiplications.

@param a:(int) number

@param b:(int) power

@return:(tuple) b to the power of a and number of made multiplications"""
    b_0 = b
    b_1 = b
    pow = 1
    mult = 0
    while pow <= a:
        b_1 *= b_1
        pow *= 2
        mult += 1
    b_1 *= b_0 ** (a - pow)
    mult += a - pow/2 -1
    return b_1, mult

def probability(n, k, p):
    """Count the probability of achieving k or fewer successes

@param n:(int) number of tries

@param k:(int) maximum number of successes

@param p:(float) the probability of success in a single attempt

@return:(tuple) the probability and number of made multiplications"""
    part1_0 = p / (1 - p)
    part1 = p / (1 - p)
    count_mul = 3
    part2 = (1 - p)
    part2 = exp_by_squ(n, part2)[0]
    count_mul += exp_by_squ(n, part2)[1]
    prob = 1 + binom(n, 1) * part1
    for i in range(2, k + 1):
        part1 *= part1_0
        prob += part1 * binom(n, i)
        count_mul += 2
    prob *= part2
    count_mul += 1
    return (prob, count_mul)

