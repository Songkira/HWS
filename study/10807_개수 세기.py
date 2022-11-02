N = int(input())
number_lst = list(map(int, input().split()))
V = int(input())

cnt = 0
for i in number_lst:
    if V == i:
        cnt += 1

print(cnt)