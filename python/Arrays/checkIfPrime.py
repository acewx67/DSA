from math import sqrt
n = 7
def isPrime(n):
    if n % 2 == 0:
        return False
    for i in range(3,int(sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True
print(isPrime(7))