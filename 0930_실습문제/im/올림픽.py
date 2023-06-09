import sys
input = sys.stdin.readline
'''
4 3
1 1 2 0
2 0 1 0
3 0 1 0
4 0 0 1
'''
# 2
N, K = map(int, input().split())    # N = 국가의 수, K = 등수를 알고 싶은 국가
# 1 <= N <= 1000 / 1 <= K <= N

country = [list(map(int, input().split())) for _ in range(N)]
# 규칙
# 1. 금메달이 제일 많은 나라
# 2. 금메달 수가 같으면, 은메달 수가 더 많은 나라
# 3. 금, 은 메달 수가 같으면, 동메달 수가 더 많은 나라
# 메달수 총합은 1,000,000

# 풀이 생각중...
# 가중치를 줄까?
# [i][1]=금메달은 *3, [i][2]=은메달은 *2, [i][3]=동메달은 *1
# 점수가 같으면 공동 등수 (예시 1 2 2 4)
score = [0] * (N+1)

for i in range(N):
    sumV = country[i][1] * 3 + country[i][2] * 2 + country[i][3] * 1
    rank = country[i][0]
    score[rank] = sumV

print(score)
lst = sorted(score)
print(lst)


