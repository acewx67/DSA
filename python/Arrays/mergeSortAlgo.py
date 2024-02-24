arr = [4,1,5,2,3,8]

def mergesort(arr):
    if len(arr) == 1:
        return arr
    m = len(arr)//2
    left = mergesort(arr[:m])
    right = mergesort(arr[m:])
    return merge(right,left)

def merge(arr1,arr2):
    p1 = 0
    p2 = 0
    i = 0
    merged_arr = [0]*(len(arr1)+len(arr2))
    while(p1 < len(arr1) and p2 < len(arr2)):
        if arr2[p2] < arr1[p1]:
            merged_arr[i] = arr2[p2]
            p2 += 1
        else:
            merged_arr[i] = arr1[p1]
            p1 += 1
        i += 1
    while p1 < len(arr1):
        merged_arr[i] = arr1[p1]
        p1 += 1
        i += 1
    while p2 < len(arr2):
        merged_arr[i] = arr2[p2]
        p2 += 1
        i += 1
    return merged_arr

print(mergesort(arr))
