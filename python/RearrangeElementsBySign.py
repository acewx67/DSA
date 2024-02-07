nums = [-1,1]
pos,neg = [],[]
for num in nums:
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)
t = 0
for i in range(0,len(nums),2):
    nums[i] = pos[t]
    t += 1
t = 0
for i in range(1,len(nums),2):
    nums[i] = neg[t]
    t += 1
print(nums)
