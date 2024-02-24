a = [8,4,1,6,7,2,5,8]
a.sort()
# print(a)
rep_num = 0
sum = 0
for i in range(len(a)):
    sum += a[i]
    if i != len(a)-1 and a[i] == a[i+1]:
        rep_num = a[i]

total_sum = (len(a)*(len(a)+1))//2
# print(total_sum)
# print(sum)
mis_num = abs(sum - total_sum - rep_num)
print(rep_num,mis_num)
