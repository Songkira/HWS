# def f(n):           # 팩토리얼 n! 1! = 1
#     if n == 1:
#         return 1
#     else:
#         return n * f(n-1)
#
# print(f(20)) # 2432902008176640000
#
# for i in range(21):
#     print(f(i))
    # RecursionError: maximum recursion depth exceeded in comparison
    # 0이 포함되어 있어서...

# # 수정
# for i in range(1, 21):
#     print(f(i))

def f(n):           # 팩토리얼 n! 1! = 1
    if n <= 1: # 0이 포함되지 않도록
        return 1
    else:
        return n * f(n-1)

for i in range(21):
    print(i, f(i))
# 0 1
# 1 1
# 2 2
# 3 6
# 4 24
# 5 120
# 6 720
# 7 5040
# 8 40320
# 9 362880
# 10 3628800
# 11 39916800
# 12 479001600
# 13 6227020800
# 14 87178291200
# 15 1307674368000
# 16 20922789888000
# 17 355687428096000
# 18 6402373705728000
# 19 121645100408832000
# 20 2432902008176640000