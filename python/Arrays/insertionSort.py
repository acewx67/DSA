nums = [5,3,4,2,1]

# def insertionSort(nums):
#     i = 0
#     while i < len(nums)-1:
#         j = i + 1
#         while j > 0:
#             if nums[j] >= nums[j-1]:
#                 break
#             else:
#                 nums[j],nums[j-1] = nums[j-1],nums[j]
#             j -= 1
#         i += 1
#     return nums
# print(insertionSort(nums))

for i in range(len(nums)-1):
    for j in range(i+1,0,-1):
        if nums[j] < nums[j-1]:
            nums[j],nums[j-1] = nums[j-1],nums[j]
        else:
            break
print(nums)




