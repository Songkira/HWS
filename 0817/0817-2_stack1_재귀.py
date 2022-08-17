# f(i, N) -> i = 현재단계, N = 목표
# 예시 : f(0, 3) -> 0(현재 단계)에서 3단계까지 진행해라.

# def f(i, N):
#     if i == N:
#         print(i) # 3 / 목표치에서 할일.
#         return
#     else: # 현재(각 진행단계)단계에서 할일을 정해줌. 보통은 가장 많이 일한다.
#         print(i) # 0 1 2
#         f(i+1, N)
#
# f(0, 3)
# # 0
# # 1
# # 2
# # 3
#-------------------------------------------------------------------------
# def f(i, N):
#     if i == N:
#         print(i)
#         return
#     else:
#         print(i)
#         f(i+1, N)
#
# # f(0, 1000)
# # RecursionError: maximum recursion depth exceeded while calling a Python object
# # 재귀 호출의 깊이를 초과했어! 계산횟수 대략 1000번 넘어가면 오류.

def f(i, N):
    if i == N:
        print(i)
        return
    else:
        print(i)
        f(i+1, N)

f(0, 100) # 제한 횟수 내라 오류 안남.
