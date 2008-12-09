import random
import sys


def square_and_multiply(x, exponent, n):
    result = 1
    while exponent > 0:
        if exponent & 1:
            result = (result * x) % n
        x = (x * x) % n
        exponent = exponent >> 1
    return result


def millerrabin(n, t, a=None):
    k=0
    m = n - 1
    while(m%2 == 0):
        k+=1
        m = m // 2
    for i in range(t):
        test = False
        if a==None:
            a = random.randint(1, n-1)
        b = pow(a, m, n)
        if b == 1:
            test = True
        for i in range(0, k):
            if b == n-1:
                test = True
            b = b*b % n
        if not test:
            return False
    return True


smallprimes = [
    3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
    53, 59, 61, 67,
    71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
    149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
    227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
    307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383,
    389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
    467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
    571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647,
    653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743,
    751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
    853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
    947, 953, 967, 971, 977, 983, 991, 997]


def find_prime(k):
    while True:
        n = random.getrandbits(k-1)
        n = n<<1 | 1
        test = True
        for p in smallprimes:
            if n % p == 0:
                test = False
        if test:
            test = millerrabin(n, 1)
        # probability of compositeness: < 1/2**(60)
        if test:
            return n


find_prime(int(sys.argv[1]))
#import cProfile
#cProfile.run('find_prime(1500)')
