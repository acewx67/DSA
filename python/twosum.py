nums = [2,7,11,15]
target = 9
numsmap = {}
def ques():
    for i in range(len(nums)):
        if type(numsmap.get(target - nums[i])) == int:
            return [i, numsmap.get(target-nums[i])]
        else:
            numsmap[nums[i]] = i
    return [-1, -1]
print(ques())



