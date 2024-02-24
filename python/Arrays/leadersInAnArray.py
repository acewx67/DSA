a = [1, 2, 3, 2]
n = 4
ans = [a[len(a)-1]]
ind = 0
def sol():
    a = [ 1,2,2,1]
    n = 4
    ans = [ a[ len( a ) - 1 ] ]
    ind = 0
    for i in range(len(a)-2,-1,-1):
        if a[i] > ans[ind]:
            ans.append(a[i])
            ind += 1
    return ans
print(sol())