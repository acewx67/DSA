nums = [1, 2, 7, -4, 3, 2, -10, 9, 1]
sum = 0
max_sum = 0
max_sum_sp = -1   #sp = startPoint
max_sum_ep = -1   #ep = endPoint
for i in range(len(nums)):
    if sum == 0:
        sp = i
    sum += nums[i]
    if sum > max_sum:
        max_sum = sum
        max_sum_sp = sp
        max_sum_ep = i
    elif sum < 0:
        sum = 0
print(nums[max_sum_sp:max_sum_ep+1])