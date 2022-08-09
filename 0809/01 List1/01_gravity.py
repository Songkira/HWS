arr = [7, 4, 2, 0, 0, 6, 0, 7, 0]
N = len(arr)
# 꼭대기 상자의 낙차값을 계산

ans = 0
for i in range(N):
    # 상자에서 벽까지 거리
    height = N - 1 - i
    # 밑에 깔리는 상자들의 개수 카운팅
    for j in range(i + 1, N):
        if arr[i] <= arr[j]:
            height -= 1

    if ans < height:
        ans = height

print(ans)