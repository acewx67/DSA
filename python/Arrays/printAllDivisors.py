from math import sqrt
def sum_divi(n):
    if n <= 1:
        return 1
    sum = 0
    for i in range(1,int(sqrt(n)+1)):

        if n%i == 0:
            if i == n // i:
                sum += i
                return sum
            sum += n//i
            sum += i
    return sum
def sol(n):
    sum = 0
    for i in range(1,n+1):
        sum += sum_divi(i)
    return sum
print(sol(5))

