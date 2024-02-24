nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(nums)
nums.reverse()
print(nums)
# if K > length of array, k == k%lengthofarray
k = k % len(nums)
# reverse the array
nums.reverse()

# reverse array from 0 to k-1 index

l, r = 0, k - 1
while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1
# reverse array from k index to end of array
print(nums)
l, r = k, len(nums) - 1

while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1
print(nums)