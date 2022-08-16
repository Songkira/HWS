import sys; sys.stdin = open("4839.txt", "r")

# T = int(input())
#
# for tc in range(T):
#     P, A, B = map(int, input().split())
#     start = 1
#     end = P
#
#     cnt_A = 0
#     cnt_B = 0
#
#     while start <= end:
#         middle = (start + end)//2
#         if middle == A:
#             break
#         elif middle > A:
#             end = middle

# ------------------------
# if 10 & 1: # 홀수 확인 / 홀수는 2진수로 만들었을 때 2**0의 위치 값이 1이면 홀수
#     pass
# else: # 짝수 확인
#     pass

# 이진 탐색
key = 11211212
arr = [] # 정렬된 자료들
N= len(arr)

def binary_search(N, key):
    #  찾을 범위에서 중간 위치 값을 선택
    start, end = 1, N
    cnt = 0
    while start <= end: #` start == end 이면 mid == start == end 가 된다.
        # mid = (start+end) >> 1 # 소수점 이하 버리기.
        mid =(start+end) // 2
        cnt += 1
        if key == arr[mid]: # 찾음!!!
            return cnt
        elif key < arr[mid]: # 왼쪽에서 찾아야지
            end = mid - 1
        else:
            start = mid + 1
    return 0
# 바운드 써치?
for tc in range(1, int(input()) + 1):
    P, A, B = map(int, input().split())

    cntA = binary_search(P, A)
    cntB = binary_search(P, B)

print(cntA, cntB)