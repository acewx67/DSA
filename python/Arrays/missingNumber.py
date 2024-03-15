nums = [9,6,4,2,3,5,7,0,1]

def solve(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i+1] != nums[i]+1:
            return nums[i+1]-1
# print(solve(nums))
def sol(nums):
    sum1 = sum(nums)
    m = len(nums)
    n_nums_sum = (m*(m+1))//2
    return n_nums_sum - sum1
print(sol(nums))


