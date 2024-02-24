def solve( ) :
    nums = [2,3,-2,4]
    curr_min = nums[0]
    ans = nums[0]
    max_prod = nums[0]

    for i in range(1, len( nums ) ) :
        temp_min = curr_min
        curr_min = min(nums[i],max_prod * nums[i],curr_min * nums[i])
        max_prod = max(nums[i],max_prod * nums[i],temp_min * nums[i])
        ans = max(max_prod,ans)
    return ans
print(solve())
