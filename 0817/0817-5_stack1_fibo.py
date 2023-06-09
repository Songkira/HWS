# 메모리제이션 활용 / 77line 부터 출력 속도가 다름을 비교

# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)

# ----------------------------------------
# for i in range(21):
#     print(i, fibo(i))
# 0 0
# 1 1
# 2 1
# 3 2
# 4 3
# 5 5
# 6 8
# 7 13
# 8 21
# 9 34
# 10 55
# 11 89
# 12 144
# 13 233
# 14 377
# 15 610
# 16 987
# 17 1597
# 18 2584
# 19 4181
# 20 6765
# ----------------------------------------
# for i in range(101): # 30 부터 좀 느려짐
#     print(i, fibo(i))
# 0 0
# 1 1
# 2 1
# 3 2
# 4 3
# 5 5
# 6 8
# 7 13
# 8 21
# 9 34
# 10 55
# 11 89
# 12 144
# 13 233
# 14 377
# 15 610
# 16 987
# 17 1597
# 18 2584
# 19 4181
# 20 6765
# 21 10946
# 22 17711
# 23 28657
# 24 46368
# 25 75025
# 26 121393
# 27 196418
# 28 317811
# 29 514229
# 30 832040
# 31 1346269
# 32 2178309
# 33 3524578
# 34 5702887
# 35 9227465
# 36 14930352
# 37 24157817
# .
# .
# ----------------------------------------
# def fibo(n):
#     if n >= 2 and memo[n]==0:
#
#         return memo[n]
#
# memo = [0] * 101
# memo[0] = 0
# memo[1] = 1
# for i in range(101):
#     print(i, fibo(i))

# -----------------------------------
def fibo(n):
    if memo[n] == -1: # -1 이 아니면 계산된 것
        memo[n] = fibo(n-1) +  fibo(n-2) # 계산된 적이 없으면 계산해라.
    return memo[n]

memo = [-1] * 101 # 201
memo[0] = 0
memo[1] = 1
for i in range(101): # 201
    print(i, fibo(i))

# 위 코드에 비해 계산이 10배는 빨라진것 같음. range(201)로 바꿔도 마찬가지
# 중복이 많이 줄어든다.
