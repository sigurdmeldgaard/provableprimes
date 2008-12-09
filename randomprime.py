from __future__ import division
import math
import random as randomimport
from primes import primes

r_max = 10
c_int = 1.2
p0 = 10000000


def primetest(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def random(a, b):
    return randomimport.randint(a, b)


def sqrt(a):
    return long(math.sqrt(a))


def generate_size_list(sl):
    #TODO
    return r


def g_opt(p):
    return 1000000


def trialdivision(a, b):
    for p in primes:
        if p>b:
            break
        if a % p == 0:
            return False
    return True


def square_and_multiply(x, exponent, n):
    """Exponentiation by the well-known square-and-multiply algorithm.
    """
    result = 1
    while exponent > 0:
        if exponent % 2:
            result = (result * x) % n
        x = (x * x) % n
        exponent = exponent // 2
    return result


def gcd(a, b):
    if a<b:
        b, a = (a, b)
    while(b != 0):
        a, b = (b, a % b)
    return a


def checklemma1(n, a, l, r):
    if square_and_multiply(a, n - 1, n)!= 1:
        return False
    for j in l:
        if gcd(a ** ((n - 1)//j - 1))!= 0:
            return False
    return True


def random_prime(p1, p2):
    pfl = []
    if p2 <= p0:
        while True:
            n = random(p1, p2)
            if primetest(n):
                break

        return n
    else:
        sl, r = generate_size_list()
        p = sqrt((p1 - 1) * (p2 - 1)) // 2
        f = 1
        g = g_opt(p)
        for i in range(1, r+1):
            q = p ** sl[i]
            pfl[i] = random_prime(q/c_int, q*c_int)
            f = f*pfl[i]
        i1 = (p1-1) // (2*f)
        i2 = (p2-1) // (2*f)
        while True:
            n = 2*random(i1, i2)
            a = random(2, p)
            if(trialdivision(n, g) and
               checklemma1(n, a, pfl, r)):
                break
        return n

