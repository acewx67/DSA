import sys

nums = [10,9,8,6,3]

def bubble(nums,index):
    if index >= len(nums):
        return nums
    min_i = -1
    min_num = sys.maxsize
    for i in range(index,len(nums)):
        if nums[i] < min_num:
            min_num = nums[i]
            min_i = i
    nums[min_i],nums[index] = nums[index],nums[min_i]
    return bubble(nums,index+1)
print(bubble(nums,0))

