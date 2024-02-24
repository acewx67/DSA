nums = [3,3,7,7,10,11,11]
def dupBS():
    if len(nums) == 1:
        return 0
    if nums[0] != nums[1]:
        return 0
    if nums[len(nums) - 1] != nums[len(nums) - 2]:
        return len(nums) - 1
    s = 0
    e = len(nums) - 1

    while (s <= e):
        mid = (s + e) // 2
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return mid
        if nums[mid - 1] == nums[mid]:
            #                 if mid-1 is even and mid is odd,then target is on right side
            if (mid - 1) % 2 == 0:
                s = mid + 1
            else:
                e = mid - 1
        elif nums[mid] == nums[mid + 1]:
            if (mid) % 2 == 0:
                s = mid + 2
            else:
                e = mid - 1
    return -1
print(dupBS())
print(nums[dupBS()])