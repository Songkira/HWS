import sys; sys.stdin = open('10988.txt')

# 딕셔너리 X, 정렬 X, 배열과 for문 으로만!!!

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    MinV_lst = [0] * (N + 1)

    for i in range(N):
        for j in range(N):
            if j == lst[i]:
                MinV_lst[j] = lst[i]
    print(MinV_lst)

    sort_lst = [0]
    for i in range(1, len(MinV_lst)):
        if MinV_lst[i] != 0:
            sort_lst.append(MinV_lst[i])
    print(sort_lst)

    print(f'#{tc} {sort_lst[K]}')