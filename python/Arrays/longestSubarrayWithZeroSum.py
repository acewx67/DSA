n = 5
arr = [0, 1 ,2,-1,-1]
max_len = 1
ans = 0
sum = arr[0]
for i in range(1,len(arr)):
    sum += arr[i]
    if max_len > 0 and sum != 0:
        max_len = 0
    else:
        max_len += 1
    if max_len > ans:
        ans = max_len
if ans == 0 and arr[0] == 0:
    ans = 1
print(ans)
