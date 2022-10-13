N = int(input())

lst = []
for _ in range(N):
    num = int(input())
    lst.append(num)
lst.sort()

arr = []
for i in range(N):
    res = 0
    for j in range(lst[i], lst[i]+5):
        if j not in lst:
            res += 1
    arr.append(res)
print(min(arr))


#     if lst[i]+1 == lst[i+1]:
#         res += 1
#     if MaxV < res:
#         MaxV = res
#
# print(5 - MaxV)

# nice = []
# # 올바른 배열은 원소중 5개가 연속적인 것.
# for i in range(N-1):
#     if lst[i]+1 == lst[i+1]:
#         # nice.append()
#         continue
#     else:
#         lst.pop(i+1)