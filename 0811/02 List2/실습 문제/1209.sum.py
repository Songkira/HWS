import sys; sys.stdin = open('1209.txt', 'r')

for _ in range(10):
    case = int(input())
    tables = []
    for r in range(100):
        tables.append(list(map(int, input().split())))
        # 코드 작성
    # tables = [list(map(int, input().split())) for _ in range(100)]

    ans = 0     # 최대값

    for r in range(100):
        r_sum = 0
        for c in range(100):
            r_sum += tables[r][c]
        if ans < r_sum:
            ans = r_sum

    for r in range(100):
        c_sum = 0
        for c in range(100):
            c_sum += tables[c][r]
        if c_sum > ans:
            ans = c_sum

    # 대각 합 구하기
    cr1_sum = 0  # 좌상단-->우하단
    cr2_sum = 0  # 우상단-->좌하단
    for r in range(100):
        cr1_sum += tables[r][r]
        cr2_sum += tables[99 - r][r]

    if ans < cr1_sum:
        ans = cr1_sum
    if ans < cr2_sum:
        ans = cr2_sum

    print(f'#{_ + 1}', ans)
