
for tc in range(1, 3):
    N = int(input())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    op = [0] * (N + 1)      # 연산자
    val = [0] * (N + 1)     # 피연산자

    for _ in range(N):
        arr = input().split()

        idx = int(arr[0])
        if len(arr) == 4:
            op[idx] = arr[1]
            L[idx] = int(arr[2])
            R[idx] = int(arr[3])
        else:
            val[idx] = int(arr[1])

    def calc(v):
        if L[v] == 0:       # 피연산자인 경우 => 단말노드인 경우
            return val[v]
        else:               # 연산자인 경우 => 내부 노드
            l = calc(L[v])
            r = calc(R[v])

            # 후위순회
            if op[v] == '+': return l + r
            elif op[v] == '-': return l - r
            elif op[v] == '*': return l * r
            else: return l / r

    # 루트 정점의 번호는 항상 1
    print(calc(1))

