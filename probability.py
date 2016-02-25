from __future__ import division
import operator
from itertools import izip, cycle
from sympy import mpmath
from sympy.functions.combinatorial.numbers import nC


"""
In a dye with n-sides, the probability of getting 1 through n in any order
for exactly n trials can be calculated by principle of inclusion-exclusion.

total outcomes = 6**n

# of outcomes excluding 1 = 5**n
# of outcomes excluding 2 = 5**n
# of outcomes excluding n = n*(5**n)

# of outcomes excluding 1 and 2 = 4**n
# of outcomes excluding 1 and 3 = 4**n
# of outcomes excluding {(1,2), (1,3) ... } all 2 pair combination
                           = nC(n,2)*((n-2)**n)
# of outcomes excluding {(1,2,3), (1,3,4) ... } all 3 pair combination
                           = nC(n,3)*((n-3)**n)

# of outcomes that has all n numbers is in n trials
        = 1
          - {outcomes excluding pairs (a,b)}
          + {outcomes excluding three numbers (a,b,c)}
          - {outcomes excluding four numbers (a,b,c,d)}

          + (-1)**n excluding n numbers (1,...,n)
        where (a,b,c,d) belongs to {1,...,n}

Complexity = O(n**n)
"""


def probability(n):
    """ Calculates the probability of an n-sided die to have all numbers
        in the list from 1 through n in a trial of n throws
        Input n : n-sided die
        Output prob : probability
    """

    if not isinstance(n, int):
        raise ValueError('Input not of integer instance')

    if n <= 0:
        raise ValueError('Input not a positive integer')

    exclusions_list = [(nC(n, r) * ((n-r)**n)) for r in range(n)]
    nr = reduce(operator.add,
                [x*y for x, y in izip(exclusions_list, cycle([1, -1]))])
    dr = n**n
    prob = mpmath.mpf(nr)/mpmath.mpf(dr)
    return prob

if __name__ == "__main__":
    for i in xrange(1, 7, 1):
        print "P({}) => {prob}".format(i, prob=probability(i))

    import matplotlib.pyplot as plt
    x_axis = []
    y_axis = []
    for i in xrange(100, 3000, 100):
        x_axis.append(i)
        y_axis.append(mpmath.timing(probability, i))

    plt.plot(x_axis, y_axis)
    plt.xlabel("n-sided die")
    plt.ylabel("time in seconds for p(n)")
    plt.title("Time complexity of P(n)")
    plt.show()
