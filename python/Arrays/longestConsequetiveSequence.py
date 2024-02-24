# def sol():
#     a = [5, 8, 3, 2, 1, 4]
#     n = 6
#     a.sort()
#     d = {}
#     for i in range(len(a)):
#         if d.get(a[i]):
#             d[a[i]] += 1
#         else:
#             d[a[i]] = 1
#     keys = list(d.keys())
#     print(keys)
#     ind = 0
#     count = 0
#     for i in range(len(keys)):
#         if len(d) == 0:
#             break
#         if d.get(keys[ind]-1):
#             count += 1
#             d[keys[ind]-1] -= 1
#             d[keys[ind]] -= 1
#             if d[keys[ind]] <= 0:
#                 d.pop(keys[ind])
#             if d[ keys[ ind ]-1 ] <= 0 :
#                 d.pop( keys[ ind ]-1 )
#         ind += 1
#     print(count)
#
#
#
#     # print(a)
#     # count = 0
#     # for i in range(len(a)-1):
#     #     if a[i+1] - a[i] == 1:
#     #         count += 1
#     # return count
# # print(sol())
# def bs(arr,num):
#     s = 0
#     e = len(arr)-1
#
#     while s<=e:
#         m = (s + e) / 2
#         if arr[m] == num:
#             return m
#         elif arr[m] > num:
#             e = m-1
#         else:
#             s = m+1
#     return -1
#
# def solve():
#     a = [5, 8, 3, 2, 1, 4]
#     a.sort()
#     for i in range(len(a)):
#         if bs(a,a[i]-1) != -1:
#
#
#
#
#
#
#
