nums = [5, 8, 3, 2, 1, 4,4,4,2,2,5,8,3]
def sol(nums):
    nums.sort()
    i,j = 0,0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] != nums[j]:
                break
            if nums[i] == nums[j]:
                j -= 1
                nums.pop(j)
            j += 1
        i += 1
    return nums
sol(nums)
print(nums)
count = 0
max_count = 0
for i in range(0,len(nums)-1):
    if nums[i+1] - nums[i] == 1:
        count += 1
        max_count = max(max_count,count)
if max_count > 0:
    print(max_count+1)
else:
    print(max_count)