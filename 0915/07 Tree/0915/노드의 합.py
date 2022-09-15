
for tc in range(1, int(input())+1):
    # N = 노드 개수/ M = 리프 노드 개수 / L = 값을 출력할 노드 번호
    N, M, L = map(int, input().split())
    arr = [0] * (N + 1)

    for _ in range(M):
        idx, val = map(int, input().split())
        arr[idx] = val

    # 나머지 노드에 자식 노드 값의 합을 저장
    # [1] = [2] + [3] / [2] = [4] + [5]
    for i in range(N - M, 0, -1):
        if 0 <= i*2 < N+1:
            arr[i] += arr[i*2]
        else:
            continue
        if 0 <= i*2+1 < N+1:
            arr[i] += arr[i*2+1]
        else:
            continue

    print(f'#{tc}', arr[L])

