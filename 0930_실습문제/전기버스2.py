# by 윤승환
def find(station, idx, cnt):    # idx : 정류장 번호, cnt : 추천횟수
    global ans

    next = station[idx] + idx
    if cnt >= ans:
        return

    if next >= N:
        ans = min(cnt, ans)
        return

    find(station, next, cnt + 1)
    for i in range(next - 1, idx, -1):
        if station[i] > station[next]:
            find(station, i, cnt + 1)


for t in range(1, int(input()) + 1):
    station = list(map(int, input().split()))
    N = station[0]
    ans = 101
    find(station, 1, 0)
    print(f'#{t}', ans)

# -----------------------------------------------
# by 김덕호

def backtrack(s, charge, cnt):
    if charge < 0:
        return
    global ans
    if cnt >= ans:
        return
    if s == N - 1:
        ans = min(ans, cnt)
        return
    # 교체하지 않고 간다.
    if charge:
        backtrack(s + 1, charge - 1, cnt)
    # s번 정류장에서 교체하고 간다.
    backtrack(s + 1, arr[s] - 1, cnt + 1)


for case in range(1, int(input()) + 1):
    datas = list(map(int, input().split()))
    N = datas[0]
    arr = [datas[i] for i in range(1, N)]
    ans = N
    backtrack(1, arr[0] - 1, 0)
    print(f'#{case}', ans)

# -----------------------------------------
# by 길상욱

for T in range(int(input())):
    arr = list(map(int,input().split()))
    n = arr[0]
    dp = [0] * (n+1)
    for i in range(n - 1, 0, -1):
        if i + arr[i] >= n + 1:
            dp[i] = 1
        else:
            dp[i] = min(dp[i + 1:i+arr[i]+1]) + 1
    print(f'#{T+1}', 0 if arr[1] + 1 >= n else dp[1] - 1)



