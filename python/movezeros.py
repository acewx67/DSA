
nums = [0,5,6,1,0,9,0,2,0]
i,j=0,0

for k in range(len(nums)):
    if(nums[j] != 0):
        nums[i] = nums[j]
        i += 1
    j += 1
for i in range(i,len(nums)):
    nums[i] = 0

