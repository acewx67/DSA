intervals = [[1,9],[1,4],[2,1000],[3,4],[6,90],[8,9]]
intervals.sort()
print(intervals)
ans = []
ans.append(intervals[0])
i = 1
j = 0
while i < len(intervals)-1:
    if ans[j][1] < intervals[i][0]:
        ans.append(intervals[i])
        i += 1
        j += 1
    elif ans[j][1] <= intervals[i][1]:
        ans[j][1] = intervals[i][1]
        i += 1
    # elif ans[j][1] > intervals[i][1]:
    else:
        i += 1
        # ans.append(intervals[i])
        # i += 1
        # j += 1
print(ans)















# def merge(intervals):
#     for i in range(len(intervals)-1):
#         if intervals[i][1] >= intervals[i+1][0] and intervals[i][1] <= intervals[i+1][1]:
#             if intervals[i][0] > intervals[i+1][0]:
#                 intervals[ i + 1 ] = [ intervals[ i+1 ][ 0 ] , intervals[ i + 1 ][ 1 ] ]
#                 intervals[i] = 0
#             else:
#                 intervals[i+1] = [intervals[i][0],intervals[i+1][1]]
#                 intervals[i] = 0
#                 i += 1
#
#     return intervals
# ans = []
# merge(intervals)
# length = len(intervals)
# i = 0
# while i < length:
#     if type(intervals[i]) != list:
#         intervals.pop(i)
#         length -= 1
#     i += 1
# print(intervals)
