import sys; sys.stdin = open('5248.txt', 'r')

# N = 10      # 정수

# # disjoint-set
# p = [i for i in range(N + 1)]       # make_set()

# find-set(x)
# def find_set(x):    # path compression
#     if x != p[x]:   # 루트
#         p[x] = find_set(p[x])
#         return p[x]
#     return x

# # x, y가 속한 두 집합을  union
# a = find_set(x)
# b = find_set(y)
# if a != b:
#     p[a] = b
#     p[b] = a

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    p = [i for i in range(N + 1)]   # make_set()
    lst = list(map(int, input().split()))
    for i in range(0, M*2, 2):
        s, e = lst[i], lst[i + 1]

        if find_set(s) != find_set(e):
            union(s, e)
            N -= 1

    print(f'#{tc} {N}')
