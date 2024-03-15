a = [1,2,3,2]
b = 2
ans= 0
xor = 0
hm = {0:1}
for i in range(len(a)):
    xor ^= a[i]
    if type(hm.get(xor^b)) == int:
        ans += hm.get(xor^b)
    if type(hm.get(xor)) == int :
        hm[xor] += 1
    else:
        hm[xor] = 1
print(ans)