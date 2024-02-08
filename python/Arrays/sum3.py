nums = [-1,0,1,2,-1,-4]
map = {}
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        sum = nums[i] + nums[j]
        if map.get(sum):
            map[sum] += 1

