# fibo_dp 에서 파생된 수식
a = 0
b = 1
n = 20

for _ in range(n-1):
    a, b= b, a+b # 0 1 1 2 3 5 ...
    # a=0, b=1 -> a=1, b=1 -> a=1, b=2 -> a=2, b=3 -> a=3, b=5 ->....
print(b) # 6765
