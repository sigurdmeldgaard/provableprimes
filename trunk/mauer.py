import random
import math
import small_primes
import gmpy
import sys


# Constants that are set manually to optimize the running time.
# These needs to be configured depending on your OS and CPU/RAM etc.
p0 = 10000000000
c_opt = 0.2
margin = 20

# Your standard greatest common divisor
def gcd(a, b):
    if b > a:
        (b, a) = (a, b)
    while b!=0:
        (a, b) = (b, a % b)
    return a


# Simple test that checks if the number n mod i is 0.
# if this is the case, n can never be a prime. 
def prime_test(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


# Uses the list of small primes to conduct the same
# test as in prime_test
def trial_division(a, b):
    for i in small_primes.primes:
        if i>b:
            break
        if a % i == 0:
            return False
    return True



# Specialized version of the millerrabin test for base 2.
def millerrabin_2(n):
    k=0
    m = n - 1
    while(m & 1 == 0):
        k+=1
        m = m >> 1
    b = pow(2, m, n)
    if b == 1:
        return True
    for i in range(0, k):
        if b == n-1:
            return True
        b = b*b % n
    return False


# The actual algorithm. - explained in more detail in the report.
def fastprime(k):
    if k <= margin:
		# Small k - generate the prime by trial division.
        while True:
            n = random.getrandbits(k-1)
            n = n<<1 | 1
            if prime_test(n):
                return n
    else:
		# k big, generate the prime recursively.
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
			# using gmpy to improve performance - better representation of big integers.
			# Once you used gmpy, everywhere you use the variable, the result of that 
			# expression will also use gmpy representations.
            n = gmpy.mpz(2*r*q+1)
			# Here we sort out the most wrong numbers
            if  trial_division(n, g) and millerrabin_2(n):
                a = gmpy.mpz(random.randint(2, n-2))
                if pow(a, n-1, n) == 1:
                    if gcd(pow(a, 2*r, n)-1, n) == 1:
                        success = True
        return n


def main():
    a = fastprime(int(sys.argv[1]))
    print a

# Remove main() and de-comment cProfile and you will get a time-table over the program
# execution, and where it spend the most time calculating.

# import cProfile
# cProfile.run('main()')

main()
