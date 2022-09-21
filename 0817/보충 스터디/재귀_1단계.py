#1단계 (함수 1번 호출)

# 1234321
# 65433456
# 135797531

# def abc(x):
#
#     if x==2:
#         return
#
#     abc(x+1)
#
# abc(0)
# --------------------
# # 1234321 (1)
# def abc(x):
#     print(x, end='')
#     if x == 4:
#         return
#
#     abc(x + 1)
#     print(x, end='')
#
# abc(1)

# # 1234321 (2)
# def abc(x):
#
#     if x == 4:
#         print(x, end='')
#         return
#     print(x, end='')
#     abc(x + 1)
#     print(x, end='')
#
# abc(1)
# ---------------------
# # 65433456
# def abc(x):
#     print(x, end='')
#     if x == 3:
#         print(x, end='')
#         return
#
#     abc(x - 1)
#     print(x, end='')
#
# abc(6)
# --------------------
# # 135797531 (1)
# def abc(x):
#     print(x, end='')
#     if x == 9:
#         return
#
#     abc(x + 2)
#     print(x, end='')
#
# abc(1)

# # 135797531 (2)
# def abc(x):
#
#     if x == 9:
#         print(x, end='')
#         return
#     print(x, end='')
#     abc(x + 2)
#     print(x, end='')
#
# abc(1)
