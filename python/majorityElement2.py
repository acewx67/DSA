nums = [1,2]
map = {}
for i in range(len(nums)):
    if map.get(nums[i]):
        map[nums[i]] += 1
    else:
        map[nums[i]] = 1
ans = []
for i in map:
    if map[i] > len(nums)/3:
        ans.append(i)
print(ans)

