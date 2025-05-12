# TODO
import math
def isPrime(n):
    j = int(math.sqrt(n))
    if n == 1:
        return False
    elif n != 1:
        for i in range(2,j):
            if n % i != 0:
                print("sosuu")
                return True
                break
            else:
                print("not sosuu")
                return False
isPrime(61)
isPrime(10)
