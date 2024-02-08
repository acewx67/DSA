nums1 = [7,8,9,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
def merge():
    p1,p2 = 0,0
    ans = []
    while(p1 < m and p2 < n):
        if nums2[p2] <= nums1[p1]:
            ans.append(nums2[p2])
            p2 += 1
        else:
            ans.append(nums1[p1])
            p1 += 1
    while(p1 < m):
        ans.append(nums1[p1])
        p1 += 1
    while (p2 < n):
        ans.append(nums2[p2])
        p2 += 1
    return ans
# nums1 = merge()
# print(nums1)


'''
[1,2,3,4,0,0,0]
[2,5,6]
'''
p1 = m-1
p2 = n-1
i = len(nums1)-1
while p1 >= 0 and p2 >= 0:
    if nums2[p2] > nums1[p1]:
        nums1[i] = nums2[p2]
        p2 -= 1
        i -= 1
    else:
        nums1[i] = nums1[p1]
        p1 -= 1
        i -= 1
while p2 >= 0:
    nums1[i] = nums2[p2]
    p2 -= 1
    i -= 1
while p1 >= 0:
    nums1[i] = nums1[p1]
    p1 -= 1
    i -= 1
print(nums1)






