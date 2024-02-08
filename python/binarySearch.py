nums = [-1,0,3,5,9,12]
target = 9
s, e = 0, len(nums) - 1
def bs(s,e):
    while (s <= e):
        mid = (s + e) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    return -1
print(bs(s,e))