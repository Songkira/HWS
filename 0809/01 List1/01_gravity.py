arr = [7, 4, 2, 0, 0, 6, 0, 7, 0]
N = len(arr)
# 꼭대기 상자의 낙차값을 계산

# ans = 0
# for i in range(N):
#     # 상자에서 벽까지 거리
#     height = N - 1 - i
#     # 밑에 깔리는 상자들의 개수 카운팅
#     for j in range(i + 1, N):
#         if arr[i] <= arr[j]:
#             height -= 1
#
#     if ans < height:
#         ans = height
#
# print(ans)

ans = 0 # 낙차가 가장 큰 값을 비교할 변수
for i in range(N):
    # 상자에서 벽까지 거리
    height = N - 1 - i # 최대 높이 - 1 - 상자 위치 : 20 - 1 - 0 => 20 -1 -1 => 20 -1 -2
    # 왜 1을 빼냐면 시작 위치가 0부터 시작이라서

    # 밑에 깔리는 상자들의 개수 카운팅
    for j in range(i +1, N):
        if arr[i] <= arr[j]:
            height -= 1

    if ans < height:
        ans = height

print(ans)
