import sys
input = sys.stdin.readline

N = int(input())
high_road = list(map(int, input().split()))

maxV = 0
ans = []

# for i in range(N):
#     if 0 <= i+1 < N and 0 <= i -1 < N:
#         if high_road[i] < high_road[i+1]:
#             e = high_road[i + 1]
#             if maxV < high_road[i+1] - high_road[i]:
#                 maxV = high_road[i + 1] - high_road[i]
#         elif high_road[i - 1] > high_road[i]:
#             s = high_road[i - 1]
#         if high_road[i] > high_road[i - 1]:
#             s = high_road[i - 1]
#             if maxV < high_road[i] - high_road[i - 1]:
#                 maxV = high_road[i] - high_road[i - 1]
#         elif high_road[i+1] < high_road[i]:
#             e = high_road[i + 1]
# road = e - s
# if maxV < road:
#     maxV = road

for i in range(N-1):
    if high_road[i] < high_road[i+1]:
        maxV += high_road[i+1] - high_road[i]
    elif high_road[i] >= high_road[i+1]:
        ans.append(maxV)
        maxV = 0

ans.append(maxV)

print(max(ans))

# for i in range(N-1):
#     for j in range(i+1, N):
#         if high_road[i] > high_road[j]:
#             s = high_road[j]
#         if high_road[i] < high_road[j]:
#             e = high_road[j]
#
#     road = e - s
#
#     if maxV < road:
#         maxV = road
#
# print(e, s)
# print(maxV)