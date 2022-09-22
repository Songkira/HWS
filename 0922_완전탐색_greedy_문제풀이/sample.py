# 부분 집합 생성
arr = [1, 2, 3, 4]
N = len(arr)
pick = []
# 기본틀
# def backtrack(k):
#     if k == N:
#         pass
#     else:
#         backtrack(k + 1)    # k번 원소를 포함
#         backtrack(k + 1)    # k번 원소를 배제

# # 부분집합 전부 생성
# def backtrack(k):
#     if k == N:
#         print(pick)
#     else:
#         pick.append(arr[k])
#         backtrack(k + 1)    # k번 원소를 포함
#         pick.pop()
#
#         backtrack(k + 1)    # k번 원소를 배제

# # 부분집합 조건부 생성
# # pick = []
# def backtrack(k):
#     if len(pick) == 2:
#         print(pick)
#         return
#     if k == N:
#         return
#     else:
#         pick.append(arr[k])
#         backtrack(k + 1)    # k번 원소를 포함
#         pick.pop()
#
#         backtrack(k + 1)    # k번 원소를 배제

# backtrack(0)

def backtrack(k, lst): # 새로운 리스트를 매개변수로
    if len(lst) == 2:
        print(lst)
        return
    if k == N:
        return
    else:
        backtrack(k + 1, lst + [arr[k]])    # k번 원소를 포함
        backtrack(k + 1, lst)    # k번 원소를 배제

backtrack(0, [])










