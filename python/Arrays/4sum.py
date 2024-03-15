nums = [-3, -1, 0, 2, 4, 5]
target = 0
nums.sort()
print(nums)
ans = []
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    j = i + 1
    while j < len(nums):
        while j > i+1 and nums[j] == nums[j - 1]:
            j += 1
        l,r = j+1,len(nums)-1
        while l < r:
            _sum = nums[i] + nums[j] + nums[l] + nums[r]
            if _sum == target:
                ans.append([nums[i],nums[j],nums[l],nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif _sum < target:
                l += 1
            else:
                r -= 1
        j += 1
print(ans)



