import random
import math
import small_primes
#from millerrabin import square_and_multiply
from millerrabin import millerrabin
import gmpy
import sys

p0 = 10000000000
c_opt = 0.2
margin = 20


def gcd(a, b):
    if b > a:
        (b, a) = (a, b)
    while b!=0:
        (a, b) = (b, a % b)
    return a


def prime_test(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def trial_division(a, b):
    for i in small_primes.primes:
        if i>b:
            break
        if a % i == 0:
            return False
    return True


def square_and_multiply_2(exponent, n):
    result = 1
    x = 1
    i = 1
    while exponent > 0:
        if exponent & 1:
            result = (result * x) % n
        x = x * x % n
        exponent = exponent >> 1
    return result


def millerrabin_2(n):
    k=0
    m = n - 1
    while(m & 1 == 0):
        k+=1
        m = m >> 1
    b = square_and_multiply_2(m, n)
    if b == 1:
        return True
    for i in range(0, k):
        if b == n-1:
            return True
        b = b*b % n
    return False


def fastprime(k):
    if k <= margin:
        while True:
            n = random.getrandbits(k-1)
            n = n<<1 | 1
            if prime_test(n):
                return n
    else:
        g = c_opt * k * k
        if k > 2*margin:
            while True:
                relative_size = 2 ** (random.random() - 1)
                if k * relative_size < k - margin:
                    break
        else:
            relative_size = 0.5
        q = fastprime(int(relative_size * k)+1)
        #print "Generating prime with %d bits" % (int(relative_size * k)+1)
        #print "Had %s bits" % math.log(q, 2)
        #print "rel %s" % (math.log(q, 2) / (int(relative_size * k)+1))
        success = False
        i = int((2**(k-1)) / (2*q))
        while not success:
            r = random.randint(i+1, 2*i)
            n = gmpy.mpz(2*r*q+1)
            if  trial_division(n, g) and millerrabin_2(n):
                millerrabin(n, 5)
                a = gmpy.mpz(random.randint(2, n-2))
                if pow(a, n-1, n) == 1:
                    #print "sq"
                    if gcd(pow(a, 2*r, n)-1, n) == 1:
                        success = True
        return n


def main():
    #print sys.argv
    a = fastprime(int(sys.argv[1]))
    #print a, millerrabin(a, 10)


def test():
    square_and_multiply_2(4, 101)
#    gmpy.mpz(5)
#import cProfile
#cProfile.run('main()')
main()
#test()
