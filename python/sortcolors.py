nums = [2,0,2,1,1,0]
r,w,b=0,-1,-1

s = 0
for i in range(len(nums)):
    if nums[i] == 0:
        nums[s],nums[i] = nums[i],nums[s]
        s += 1

for i in range(len(nums)):
    if nums[i] == 1:
        nums[s],nums[i] = nums[i],nums[s]
        s += 1
for i in range(len(nums)):
    if nums[i] == 2:
        nums[s],nums[i] = nums[i],nums[s]
        s += 1
print(nums)




