import sys; sys.stdin = open('tree_input.txt', 'r')

V, E = map(int, input().split())
arr = list(map(int, input().split()))

L = [0] * (V + 1) # 1번 ~ V번 까지의 노드번호 사용 (왼쪽 자식)
R = [0] * (V + 1) # 1번 ~ V번 까지의 노드번호 사용 (오른쪽 자식)
P = [0] * (V + 1) # 1번 ~ V번 까지의 노드번호 사용 (부모)

for i in range(0, E*2, 2):
    parent, child = arr[i], arr[i + 1]
    if L[parent] == 0:
        L[parent] = child
    else:
        R[parent] = child

    P[child] = parent

def inorder(v):
    if v == 0: # 길이 없어서 못간다
        return
    # 전위 순회
    # print(v, end=' ') # 1 2 4 7 12 3 5 8 9 6 10 11 13
    inorder(L[v])
    # 중위 순회
    # print(v, end = ' ') # 12 7 4 2 1 8 5 9 3 10 6 13 11
    inorder(R[v])
    # 후위 순회
    print(v, end=' ') # 12 7 4 2 8 9 5 10 13 11 6 3 1

inorder(1)

