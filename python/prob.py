# def func(s):
#     s = s.lower()
#     ans = ""
#     print(range(len(s)))
#     for i in range(len(s)):
#         if s[i].isalpha():
#             ans += s
#     print(ans)
#     start = 0
#     end = len(ans)-1
#     while start < end:
#         print(start)
#         print(end)
#         if ans[start] == ans[end]:
#             start += 1
#             end += 1
#         else :
#             return False
#     return True
str = "A man, a plan, a canal: Panama"
ans = ""
str = str.lower()
for i in range(len(str)):
    if str[i].isalpha():
        ans += str[i]
print(ans)
start = 0
end = len(ans)-1
while start <= end:
    if ans[start] == ans[end]:
        start += 1
        end -= 1
    else:
        print("false")
        break
print("true")

k = 2
nums = [12,45,67,34,12,34,5]
nums = nums.sort()
count = 0

