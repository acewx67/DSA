nums = [1, 2, 3, 4, 5]
for i in range(len(nums)):
    l = i
    while l < len(nums):
        print(nums[i : l + 1])
        l += 1
