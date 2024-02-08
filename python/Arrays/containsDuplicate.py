nums = [1,2,3,1]
hashmap = {}
def func(nums):
    for i in nums:
        if hashmap.get(i) == 1:
            return True
        else:
            hashmap.__setitem__(i, 1)
        return False


print(func(nums))