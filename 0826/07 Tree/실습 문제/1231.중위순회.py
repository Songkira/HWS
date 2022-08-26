import sys; sys.stdin = open('1231.txt', 'r')
#=================================================

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
    # print(v, end=' ') # 12 7 4 2 8 9 5 10 13 11 6 3 1

# for tc in range(1, 11):
#
#     V = int(input())
#     E = V - 1
#     word = [list(input().split()) for _ in range(V)]
#     print(word)
#     L = [0] * (V + 1)  # 1번 ~ V번 까지의 노드번호 사용 (왼쪽 자식)
#     R = [0] * (V + 1)  # 1번 ~ V번 까지의 노드번호 사용 (오른쪽 자식)
#
#     lst = [] #
#     cal = []
#     for i in range(V):
#         N = len(word[i])
#         if N == 4:
#             for j in range(N-1, N//2, -1):
#                 lst.append(word[i])
#         if N == 3:
#             for j in range(N):
#         if N == 2:
#             for j in range(N):

# --------------------------------------------------
# 교수님 코드

for tc in range(1, 11):

    N = int(input()) # 노드 수
    L = [0] * (N + 1) # 왼쪽 자식
    R = [0] * (N + 1) # 오른쪽 자식
    ch = [0] * (N + 1) # 알파벳 저장용

    for _ in range(N):
        arr = input().split()
        num = int(arr[0])   # 노드 번호
        ch[num] = arr[1]    # 알파벳

        if len(arr) == 4:
            L[num] = int(arr[2])
            R[num] = int(arr[3])
        if len(arr) == 3:
            L[num] = int(arr[2])

    def inorder(v):
        if v == 0:  # 길이 없어서 못간다
            return
        inorder(L[v])
        # 중위 순회
        print(ch[v], end = '') # 12 7 4 2 1 8 5 9 3 10 6 13 11
        inorder(R[v])

    print(f'#{tc}', end = ' ' )
    inorder(1)
    print()










