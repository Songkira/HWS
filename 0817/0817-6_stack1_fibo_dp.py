def fibo_dp(n):
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return # 생략 가능 / 명시하는게 원칙이긴 함.

table = [0] * 101
fibo_dp(100)
print(table[100]) # 354224848179261915075
print(table[20]) # 6765

# # N이 주어진다. 피보나치(N)을 구하시오. (  0 <= N <= 100 )
# 문제 있을시
# T(테스트케이스 갯수) 가 엄청 많을때 ( T <= 1000 )
# 미리 구해다 놓고 가져다 출력?
# table = [0] * 101
# fibo_dp(100)

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     print(f'#{tc} {table[N]}')


