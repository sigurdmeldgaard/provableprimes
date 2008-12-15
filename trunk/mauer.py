import random
import math
import small_primes
from millerrabin import millerrabin
import gmpy
import sys


#constants that are set manually to optimize the running time.
#These needs to be configured depending on your OS and CPU/RAM etc. 
p0 = 10000000000
c_opt = 0.2
margin = 20


#Your standard greatest common divisor
def gcd(a, b):
    if b > a:
        (b, a) = (a, b)
    while b!=0:
        (a, b) = (b, a % b)
    return a


#Simple test that checks if the number n mod i is 0.
#if this is the case, n can never be a prime. 
def prime_test(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


#Uses the list of small primes to conduct the same
#test as in prime_test
def trial_division(a, b):
    for i in small_primes.primes:
        if i>b:
            break
        if a % i == 0:
            return False
    return True


#Optimized version of square and multiply. 
#The original version can be found in millerrabin.py
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


#Optimized version of the millerrabin test.
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


#The actual algorithm. - explained in detail in the report.
def fastprime(k):
    if k <= margin:
		#small k - take the fast route
        while True:
            n = random.getrandbits(k-1)
            n = n<<1 | 1
            if prime_test(n):
                return n
    else:
		#k too big, go the long way
        g = c_opt * k * k
        if k > 2*margin:
            while True:
                relative_size = 2 ** (random.random() - 1)
                if k * relative_size < k - margin:
                    break
        else:
            relative_size = 0.5
        q = fastprime(int(relative_size * k)+1)
        success = False
        i = int((2**(k-1)) / (2*q))
        while not success:
            r = random.randint(i+1, 2*i)
			#using gmpy to improve performance - better representation of big integers.
			#Once you used gmpy, everywhere you use the variable, the result of that 
			#expression will also use gmpy representations.
            n = gmpy.mpz(2*r*q+1)
			#here we sort out the most wrong numbers
            if  trial_division(n, g) and millerrabin_2(n):
                #SIGURD - can the millerrabin(n,5) be removed? - check not nessesary imo.
				millerrabin(n, 5)
                a = gmpy.mpz(random.randint(2, n-2))
                if pow(a, n-1, n) == 1:
                    if gcd(pow(a, 2*r, n)-1, n) == 1:
                        success = True
        return n


def main():
    a = fastprime(int(sys.argv[1]))
    print a

#remove main() and de-comment cProfile and you will get a time-table over the program
#execution, and where it spend the most time calculating.
#import cProfile
#cProfile.run('main()')
main()
