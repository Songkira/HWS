
cnt = 1
def inorder(n):
    global cnt

    if n > N : return
    inorder(n * 2)
    tree[n] = cnt
    cnt += 1
    inorder(n * 2 + 1)

for tc in range(1, int(input())+1):
    # 1부터 N까지의 자연수를 이진 탐색 트리에 저장
    # 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리 ==> 중위순회
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 1

    inorder(1)
    print(f'#{tc}', tree[1], tree[N//2])

