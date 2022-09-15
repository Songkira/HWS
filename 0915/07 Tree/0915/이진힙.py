last = 0
def push(item):
    # full 상태를 체크: last == SIZE - 1
    # 마지막 노드의 다음 위치에 저장
    global last
    last += 1
    tree[last] = item  # 여기까지가 완전 이진트리 구조 설정

    # 부모-자식 간의 대소 관계를 체크
    c, p = last, last//2

    while p > 0 and tree[c] < tree[p]:    # p > 0 : 부모가 있는지 확인
        tree[c], tree[p] = tree[p], tree[c]
        # c, p = p, c//2
        c = p
        p = c // 2
    # else:                         # 부모가 없든가, 대소관계가 없든가
    #     break

for tc in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int, input().split()))
    tree = [0] * (N + 1)
    #
    # last = 1
    # for num in lst:
    #     tree[last] = num
    #     last += 1
    # # print(tree)
    #     c, p = last, last // 2
    #     while p and tree[c] > tree[p]:
    #         tree[c], tree[p] = tree[p], tree[c]
    #         c = p
    #         p = c // 2
    #     print(tree)

    end = 0
    last = 0
    for val in lst:
        push(val)
        # print(tree)
    #  마지막 노드의 조상 노드에 저장된 정수의 합
    while N:
        N = N // 2
        end += tree[N]

    print(f'#{tc}', end)