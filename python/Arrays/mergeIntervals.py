intervals = [[1,4],[2,3]]
intervals.sort()
def merge(intervals):
    for i in range(len(intervals)-1):
        if intervals[i][1] >= intervals[i+1][0] and intervals[i][1] <= intervals[i+1][1]:
            if intervals[i][0] > intervals[i+1][0]:
                intervals[ i + 1 ] = [ intervals[ i+1 ][ 0 ] , intervals[ i + 1 ][ 1 ] ]
                intervals[i] = 0
            else:
                intervals[i+1] = [intervals[i][0],intervals[i+1][1]]
                intervals[i] = 0
                i += 1

    return intervals
ans = []
merge(intervals)
length = len(intervals)
i = 0
while i < length:
    if type(intervals[i]) != list:
        intervals.pop(i)
        length -= 1
    i += 1
print(intervals)
