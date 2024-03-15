arr = [1, 2, 2, 3]
x = 2
def sol():
    s = 0
    e = len(arr) - 1
    ans = len(arr)
    if arr[ans-1] < x:
        return ans
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] >= x:
            ans = mid
            e = mid-1
        else:
            s = mid + 1
    return ans
print(sol())