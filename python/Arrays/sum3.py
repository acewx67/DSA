nums = [-1,0,1,2,-1,-4]
nums.sort()
ans = []
i = 0
while i < len(nums):
    l = i + 1
    r = len(nums)-1
    target = -(nums[i])
    while l < r:
        if nums[l] + nums[r] == target:
            ans.append([nums[i],nums[l],nums[r]])
            while nums[l] == nums[l+1]:
                l += 1
            while nums[r] == nums[r-1]:
                r -= 1
        if nums[l] + nums[r] > target:
            r -= 1
        else:
            l += 1
    i += 1
    while i<len(nums) and nums[i] == nums[i-1]:
        i += 1
print(ans)