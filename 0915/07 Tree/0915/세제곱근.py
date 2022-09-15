
for tc in range(1, int(input())+1):
    N = int(input())
    V = round(N**(1.0/3.0))
    print(f'#{tc}', end=' ')
    if V ** 3 == N:
        print(round(V))
    else:
        print(-1)
    # 소인수 분해?