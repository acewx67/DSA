count = {}
nums = [2,2,1,1,1,2,2]
for num in nums:
    if count.get(num):
        count[num] = count.get(num) + 1
    else:
        count[num] = 1
max = -1
maxNum = -1
for i in count:
    if count.get(i) > max:
        max = count.get(i)
        maxNum = i
print(count)
print(maxNum)