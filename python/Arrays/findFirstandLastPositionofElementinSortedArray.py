nums = [2,3,4,5,5,5,5,6,8,9]
target = 5
s = 0
e = len(nums)-1
ans = [-1]*2
def bs(s,e):
    while(s<=e):
        mid = (s+e)//2
        if nums[mid] == target:
            if ans[0] == -1 and mid == 0 or nums[mid-1]<target:
                ans[0] = mid
                if ans[1] != -1:
                    return ans
            else:
                e = mid - 1
            # if ans[1] == -1 and mid == len(nums)-1 or nums[mid+1] > target:
            #     ans[1] = mid
            #     if ans[0] != -1:
            #         return ans
            # else:
            #     s = mid + 1
        elif nums[mid] < target:
            s = mid + 1
        else:
            e = mid - 1
    return ans
print(bs(s,e))
