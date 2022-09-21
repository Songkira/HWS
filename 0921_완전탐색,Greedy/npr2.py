# 재귀 호출을 통한 순열 생성
# 5개면 5!개수 전부다 구하는 경우
def f(i, k):
    if i == k:      # 인덱스 i == 원소의 개수
        print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]

# p = [1, 2, 3, 4, 5]
# f(0, 5)
# p = [1, 2, 3]
# f(0, 3)
# p = [i for i in range(1, 11)] # 10개짜리
# f(0, 10)

N = 3
p = [i for i in range(1, N+1)]
f(0, N)