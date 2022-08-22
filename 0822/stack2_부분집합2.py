# def f(i, N, s, t):
#     global answer
#     if s == t:              # 부분집합의 합이 t면
#         answer += 1
#     elif i == N:            # 모든 원소가 고려된 경우
#         return
#     else:
#         f(i+1, N, s+A[i], t) # A[i]가 포함된 경우
#         f(i+1, N, s, t)      # A[i]가 포함되지 않은 경우
#
#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# bit = [0] * 10
# answer = 0
# f(0, 10, )
# print(answer)
# ----------------------------------------------------
# def f(i, N, s, t):
#     global answer
#     if i == N:            # 모든 원소가 고려된 경우
#         if s == t:  # 부분집합의 합이 t면
#             answer += 1
#         return
#     else:
#         f(i+1, N, s+A[i], t) # A[i]가 포함된 경우
#         f(i+1, N, s, t)      # A[i]가 포함되지 않은 경우
#
#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# bit = [0] * 10
# answer = 0
# f(0, 10, 0, 10)
# print(answer)
#-------------------------------------

# def f(i, N, s, t):
#     global answer
#     global cnt
#     cnt += 1
#     if i == N:      # 모든 원소가 고려된 경우
#         if s == t:  # 부분집합의 합이 t면
#             answer += 1
#         return
#     else:
#         f(i+1, N, s+A[i], t) # A[i]가 포함된 경우
#         f(i+1, N, s, t)      # A[i]가 포함되지 않은 경우
#
#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# bit = [0] * 10
# answer = 0
# cnt = 0
# f(0, 10, 0, 10)
#
# print(answer, cnt) # 10 2047

#--------------------------------------
def f(i, N, s, t):
    global answer
    global cnt
    cnt += 1
    if i == N:      # 모든 원소가 고려된 경우
        if s == t:  # 부분집합의 합이 t면
            answer += 1
        return
    elif s> t: # 조건을 걸면?
        return
    else:
        f(i+1, N, s+A[i], t) # A[i]가 포함된 경우
        f(i+1, N, s, t)      # A[i]가 포함되지 않은 경우


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
answer = 0
cnt = 0
# f(0, 10, 0, 10)
# print(answer, cnt) # 10 415
# f(0, 10, 0, 55)
# print(answer, cnt) # 1 2047
f(0, 10, 0, 4)
print(answer, cnt) # 2 111