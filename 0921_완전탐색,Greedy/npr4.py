# # 재귀 호출을 통한 순열 생성3
# N개 중에 R개 구하는 경우
def f(i, k, r):
    if i == k:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
                used[j] = 1         # a[j] 사용됨으로 표시
                p[i] = a[j]         # p[i]는 a[j]로 결정
                f(i+1, k, r)           # p[i+1] 값을 결정하러 이동
                used[j] = 0         # a[j]를 다른 자리에서 쓸 수 있도록 해제


N = 3  # 주어진 개수
R = 3   # 고르는 개수
a = [i for i in range(1, N+1)]
# a = [1, 2, 4, 7, 8, 3]
used = [0] * N
p = [0] * R
f(0, N, R)