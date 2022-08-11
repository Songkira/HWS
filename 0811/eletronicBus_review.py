import sys; sys.stdin = open('4831.txt')

# 대략? 제대로 못적은듯.. 정확한 코드는 아님
# T = int(input())
# for t in range(1, T +1):
#     K, N, M = map(int, input().split())
#     M_nums = [list(map(int, input().split()))]
#     charge = [0] * (N + 1)
#
#     start = 0 # 현재 정류장 번호
#     charge_count = 0 # 충전 횟수
#     while start + K < N:
#         check = start
#     # While True:
#         # if start + K >= N:
#             # break
#         for k in range(K, 0, -1):
#             if charge[start + k] == 1:
#                 charge_count += 1
#                 start += k
#                 break
#         if check == start:
#             charge_count = 0
#             break
#
#     print(f'#{t} {charge_count}')
#=======================================
# 교수님
T = int(input())
for t in range(1, T +1):
    # 3 10 5
    K, N, M = map(int, input().split())
    # [0] + [1 3 5 7 9] + [10]
    # len(station) = M + 2
    station = [0] + list(map(int, input().split())) + [N]

    cur = 0 # 현재 위치
    cnt = 0 # 충전 쵯수
    for i in range(1, M+2): # i 와 i-1 비교
        # 충전소 사이의 거리를 체크
        if station[i] - station[i-1] > K: # 갈 수 없음
            break
        # 충전할 위치를 결정
        if cur + K < station[i]:
            cur = station[i-1]
            cnt += 1
    print(cnt)