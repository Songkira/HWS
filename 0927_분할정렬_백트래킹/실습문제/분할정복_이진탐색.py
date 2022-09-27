import sys; sys.stdin = open('분할정복_이진탐색.txt', 'r')

    # l, r = s, e # l = 시작, r = 끝
    # mid = (l + r) // 2
    # 왼쪽 => l ~ mid-1 / 오른쪽 => mid + 1 ~ r

# 양쪽 구간을 번갈아 선택하게 되는 숫자의 개수 (cnt)

def binary_search(lo, hi, key, num):
    global cnt
    # 중간 위치 선택
    mid = (lo + hi) // 2
    if A[mid] == key:
        cnt += 1
        return
    elif A[mid] > key:  # 왼쪽 = 1
        if num != 1:
            binary_search(lo, mid - 1, key, 1)
    elif A[mid] < key:  # 오른쪽 = 2
        if num != 2:
            binary_search(mid + 1, hi, key, 2)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))

    cnt = 0
    for i in range(len(B)):
        if B[i] in A:
            binary_search(0, N - 1, B[i], 0)

    print(f'#{tc} {cnt}')