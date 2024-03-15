nums = [7,1,6,0]
k = 7
def lenOfLongSubarr (arr, n, k) :
    hm={}
    max_len=0
    curr_sum=0
    for i in range(n):
        curr_sum+=arr[i]
        if curr_sum==k:
            max_len=max(max_len,i+1)
        rem=curr_sum-k
        if rem in hm:
            max_len=max(max_len,i-hm[rem])
        if curr_sum not in hm:
            hm[curr_sum]=i
    return max_len
# print(lenOfLongSubarr(nums,len(nums),k))

def sol(nums,k):
    i,j = 0,0
    max_len = 0
    while i < len(nums):
        j = i
        sum = 0
        while j < len(nums):
            sum += nums[j]
            if sum > k:
                break
            if sum == k and j+1 > max_len:
                max_len = (j-i)+1
            j += 1
        i += 1
    return max_len
print(sol(nums,k))