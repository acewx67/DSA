nums = [0,0,1,1,1,2,2,3,3,4]
i = 1
j = 1
while j < len(nums):
    if nums[j] == nums[j-1]:
        j += 1
    else:
        nums[i] = nums[j]
        i += 1
        j += 1
print(nums)
print(i)


