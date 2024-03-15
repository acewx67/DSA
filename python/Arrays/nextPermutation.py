nums = [1,2,3]
# Optimized SOL:
i = 0
for j in range(len(nums)-1,-1,-1):
    if nums[j] < nums[j-1]:
        continue
    else:
        i = j-1
        print(i)
        break
if i >= 0:
    for k in range(len(nums)-1,i,-1):
        if nums[k] > nums[i]:
            nums[i],nums[k] = nums[k],nums[i]
            break
nums[i+1:] = reversed(nums[i+1:])
print(nums)


