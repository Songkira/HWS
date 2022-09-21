'''
10
1 4 1 6 6 10 5 7 3 8 5 9 3 5 8 11 2 13 12 14
'''
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    acts = []
    for _ in range(N):
      acts.append(tuple(map(int, input().split())))

    # 종료 시간 순으로 정렬
    acts.sort(key=lambda x: x[1])

    ft = acts[0][1]        # 첫번째 회의를 선택
    ans = 1
    for i in range(1, N):  # 두번째 회의부터 확인
        if ft <= acts[i][0]:  # 선택한 회의의 종료시간 이후에 시작하는 회의
            ans += 1
            ft = acts[i][1]   # 선택한 회의의 종료시간을 저장

    print(f'#{tc} {ans}')


