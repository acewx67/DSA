b = [1,2,3,3]
a = [2,2,4]
ans = [0]
i,j = 0,0
if a[0] < b[0]:
    ans[0] = a[0]
    i += 1
else:
    ans[0] = b[0]
    j += 1
k = 1
while i<len(a) and j<len(b):
    if a[i] < b[j]:
        if a[i] == ans[k-1]:
            i += 1
            continue
        ans.append(a[i])
        i += 1
        k += 1
    else:
        if b[j] == ans[k-1]:
            j += 1
            continue
        ans.append(b[j])
        j += 1
        k += 1
while i < len(a):
    if a[i] == ans[k-1]:
        i += 1
        continue
    ans.append(a[i])
    i += 1
    k += 1
while j < len(b):
    if b[j] == ans[k-1]:
        j += 1
        continue
    ans.append(b[j])
    j += 1
    k += 1
print(ans)