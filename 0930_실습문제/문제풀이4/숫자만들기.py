def dfs(depth, value):
    global maxV, minV
    if depth == n:
        minV = min(minV, value)
        maxV = max(maxV, value)
        return

    res = num[depth]
    calc = [value + res, value - res, value * res, int(value/res)]
    for i in range(4):      # 4개의 연산자에 대해서
        if opr[i] > 0:
            opr[i] -= 1
            dfs(depth+1, calc[i])
            # 갔다가 돌아오면 원상복구 시켜야 된다.
            opr[i] += 1


for tc in range(1, int(input())+1):
    n = int(input())

    # opr = [+, -, *, /] 정수값으로
    opr = list(map(int, input().split()))
    num = list(map(int, input().split()))

    print(opr)

    maxV = 1e9
    minV = -1e9

    dfs(1, num[0])
    print(f'#{tc} {maxV - minV}')
