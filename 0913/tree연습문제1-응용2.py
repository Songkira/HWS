# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
# 주어진 트리를 root부터 전위/중위/후위를 순회하는 경우
# 각각 마지막 정점은?

def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:     # 부모가 없으면 root
            return i
            # root = i
            # break

def preorder(n):    # 전위순회
    global cnt
    if n:           # n 이 0이 아니면
        cnt = n
        # print(n, end = ' ')    # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])
# ------------------------------
# 중위순회
def inorder(n):
    if n:
        inorder(ch1[n])
        print(n, end = ' ')    # visit(n)
        inorder(ch2[n])

# -----------------------------
# 후위순회
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end = ' ')    # visit(n)


V = int(input())        # 정점 개수, 마지막 정점번호
arr = list(map(int, input().split()))
E = V - 1

# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V + 1)
ch2 = [0]*(V + 1)

# 자식을 인덱스로 부모 번호 저장
par = [0] * (V + 1)
# 1
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:         # 아직 자식이 없으면
        ch1[p] = c          # 자식1로 저장
    else:
        ch2[p] = c
    par[c] = p

root = find_root(V)
# print(root)
cnt = 0
preorder(root)
print(cnt) # 13
# inorder(root)
# print()
# postorder(root)
# print()