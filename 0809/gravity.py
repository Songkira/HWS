# 가장 꼭대기에 있는 상자의 낙차값만 구하면 됨.
# 왜냐면, 최대 만 구하면 되기 때문. 나머지는 배제.

# 거리는 0 ~ N-1
# (N-1)-i # 현재 i 위치에서 N까지의 거리
# 현재 i 위치를 보고 쭉훑으면서 i와 같거나 큰값이 있는지
# 모든 상자들의 꼭대기의 낙차값 구하기

arr = [7, 4, 2, 0, 0, 6, 0, 7, 0]
N = len(arr)

# 꼭대기 사자의 낙차값을 계산

ans = 0
for i in range(N):
    # 상자에서 벽까지 거리
    height = N - 1 - i
    # 밑에 깔리는 상자들의 개수 카운팅
    # i 위치의 다음칸부터
    for j in range(i + 1, N):
        if arr[i] <= arr[j]:
            height -= 1

    if ans < height:
        ans = height

print(ans)