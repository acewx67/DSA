nums = [1, 2, 3]
index = 0
list = []


def perms(nums, index):
    if index >= len(nums):
        list.append(nums)
        return
    for i in range(index,len(nums)):
        nums[i], nums[index] = nums[index], nums[i]
        perms(nums.copy(), index + 1)
        nums[i], nums[index] = nums[index], nums[i]
    return


perms(nums, 0)
print(list)


# def solve(nums,index):
#     if index >= len(nums):
#         list.append(nums)
#         return
#     for i in range(index,len(nums)):
#         nums[index],nums[i] = nums[i],nums[index]
#         solve(nums.copy(),index+1)
#         nums[index], nums[i] = nums[i], nums[index]
#     return
# solve(nums,0)
# print(list)


# def solve(ans):
#     ans[0] = 3
#     return ans
# print(solve(ans.copy()))
# print(ans)
