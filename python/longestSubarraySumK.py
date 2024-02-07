nums = [1,2,3]
k = 3
print(count)
count = 0
for i in range(len(nums)):
    sum = 0
    for j in range(i,len(nums)):
        sum += nums[j]
        if sum > k:
            break
        if sum == k:
            count += 1
    # print(j)


