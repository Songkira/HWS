
# i = 0
# while i <3:
#     print('Hello!!')
#     i += 1

# def print_hello(i):
#     if i < 3:
#         return
#     else:
#         print('Hello!!')
#         print_hello( i + 1 )
#
# print_hello(0)
# -----------------------------------

# def print_hello(i, n):
#     if i == n:
#         return
#     else:
#         print('Hello!!')
#         print_hello(i + 1, n)
#
# print_hello(0, 3)
#------------------
cnt = 0
def print_hello(i, n):
    if i == n:
        global cnt;
        cnt += 1
    else:
        print_hello(i + 1, n)

print_hello(0, 3)
print('cnt =', cnt) # 1
#---------------------
# 재귀 2개일때
cnt = 0
def print_hello(i, n):
    if i == n:
        global cnt;
        cnt += 1
    else:
        print_hello(i + 1, n)
        print_hello(i + 1, n)

print_hello(0, 3) # (0,4)이면 cnt = 16
print('cnt =', cnt) # 8

#--------------------------
# 재귀 3개일때
cnt = 0
def print_hello(i, n):
    if i == n:
        global cnt;
        cnt += 1
    else:
        print_hello(i + 1, n)
        print_hello(i + 1, n)
        print_hello(i + 1, n)

print_hello(0, 3)
print('cnt =', cnt) # 27
#---------------------
N = 3
cnt = 0
bits = [0] *N
def print_hello(i, n):
    if i == n:
        global cnt;
        cnt += 1
        print(bits)
    else:
        bits[i] = 1
        print_hello(i + 1, n)
        bits[i] = 0
        print_hello(i + 1, n)

print_hello(0, N)
# [1, 1, 1]
# [1, 1, 0]
# [1, 0, 1]
# [1, 0, 0]
# [0, 1, 1]
# [0, 1, 0]
# [0, 0, 1]
# [0, 0, 0]
print('cnt =', cnt) # 27
