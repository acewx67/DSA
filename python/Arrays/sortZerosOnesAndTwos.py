nums=[0,1,2,0,1,2]
# DUTCH NATIONAL FLAG ALGORITHM
low,mid,high = 0,0,len(nums)-1
while mid <= high:
    if nums[mid] == 0:
        nums[mid],nums[low] = nums[low],nums[mid]
        low += 1
        mid += 1
    elif nums[mid] == 2:
        nums[mid],nums[high] = nums[high],nums[mid]
        high -= 1
    else:
        #nums[mid] == 1:
        mid += 1
print(nums)