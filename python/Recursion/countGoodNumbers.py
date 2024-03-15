import math
n = 1
primes = {}


def isPrime(n):
    if primes.get(n):
        return primes.get(n)
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    primes[n] = True
    return True


ans = 0


def sol(num, ans):
    if int(math.log10(num)) + 1 > n:
        return ans
    strnum = str(num)
    t = True
    for i in range(len(strnum)):
        if i % 2 == 0 and int(strnum[i]) % 2 == 0:
            continue
        elif i % 2 == 1 and isPrime(int(strnum[i])):
            continue
        else:
            t = False
            break
    if t:
        ans += 1
    return sol(num+1,ans)

startingNumber = '0'*2
print(startingNumber)
# print(sol(startingNumber,0))
