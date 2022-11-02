# import math
# import time
#
# start = time.time()

N = int(input())
n_list = list(map(int, input().split()))
x = int(input())

cnt = 0
for i in range(N-1):
    for j in range(i+1, N):
        if n_list[i] + n_list[j] == x:
            cnt += 1

print(cnt)
# end = time.time()
# print(f"{end - start:.5f} sec")