# N = int(input()) # 줄/행
# arr = [list(map(int, input().split())) for _ in range(N)]
import sys
sys.stdin=open('input.txt','r')

for test in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max = 0

    for i in range(100):
        sum0 = 0
        for j in range(100):
            sum0 += arr[i][j]
        if max < sum0:
            max = sum0

    for j in range(100):
        sum1 = 0
        for i in range(100):
            sum1 += arr[i][j]
        if max < sum1:
            max = sum1

    for i in range(100):
        sum2 = 0
        for j in range(100):
            if i == j:
                sum2 += arr[i][j]
        if max < sum2:
            max = sum2

    for i in range(100):
        sum3 = 0
        for j in range(100):
            sum3 += arr[i][99-j]
        if max < sum3:
            max = sum3

    print(f'#{N} {max}')