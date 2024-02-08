nums = [1,1,1]
k = 2
map = {0: 1}
sum = 0
count = 0
for num in nums:
    sum += num
    if sum - k in map:
        count += map.get(sum - k)
    if sum in map:
        map[sum] = map.get(sum) + 1
    else:
        map[sum] = 1
print(count)
'''https://leetcode.com/problems/subarray-sum-equals-k/discuss/2301103/Python-HashMap-O(n)-(Explanation)'''
