import sys
x = 2.10
n = 3
a = sys.maxsize
print(a)
def pow(x,n):
    if n == 1:
        return x
    if n%2 == 1:
        x_pow_odd = pow( x , (n-1) // 2 )
        return x*x_pow_odd*x_pow_odd
    else:
        x_pow_even = pow(x,n//2)
        return x_pow_even*x_pow_even
if n < 0:

    print(1/pow(x,-n))
else:
    print(pow(x,n))