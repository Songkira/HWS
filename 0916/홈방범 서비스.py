# 방법 1 - 너비우선(김덕호)
def cost(K):
    return K **2 + (K-1)**2

def bfs(r, c, N, K):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    q = [0]*(N*N)
    front = rear = -1

