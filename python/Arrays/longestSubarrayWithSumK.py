nums = [10, 5, 2, 7, 1, 9]
k = 15

def sol(nums,k,i):
    if len(nums) <= 0:
        return 0
    sum = nums[i] + sol(nums[i+1:])
    if sum == k:
