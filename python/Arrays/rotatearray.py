nums = [1, 2, 3, 4, 5, 6, 7]
k = 8
# for i in range(k):
    # if k % len(arr) = 0,dont do anything
    # else len(arr)/k


#     swap_index = len(nums)-1
#     while swap_index > 0:
#         a = swap_index - 1
#         nums[a],nums[swap_index] = nums[swap_index],nums[a]
#         swap_index -= 1
# print(nums)

rev = nums[::-1]

k = k % len(nums)
l,r=0,k-1
while l < r:
    rev[l],rev[r] = rev[r],rev[l]
    l,r= l+1,r-1
l,r = k,len(nums)-1
while l < r:
    rev[l],rev[r] = rev[r],rev[l]
    l,r= l+1,r-1
