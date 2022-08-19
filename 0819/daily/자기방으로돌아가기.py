import sys; sys.stdin = open('자기방으로돌아가기.txt', 'r')
# 카운트?
for tc in range(1, int(input())+1):
    cnt = [0] * 201 # 방번호를 1 ~ 200 사이의 값으로 매핑
    N = int(input())
    
    for _ in range(N):
        a, b = map(int, input().split())
        # 방 번호를 1 ~ 200 사이의 값으로 매핑
        a, b = (a + 1) // 2, (b + 1) // 2

        if a > b:
            a, b = b,a
        for i in range(a, b+1):
            cnt[i] += 1

    ans = 0
    for val in cnt:
        if ans < val:
            ans = val
    print(f'#{tc}', ans)