# 부분집합

# 하나의 부분집합 = 4번 선택 -> tree높이, 함수 호출 깊이
N = 4
arr = [i + 1 for i in range(N)]
# 선택지 2가지 -> 함수 호출 횟수
# 선택 저장 => 경로
# 원소의 갯수만큼 재귀호출 필요

cnt = 0
# pick = [0]
# def backtrack(k, cur_sum):   # k: 현재 노드의 높이, 함수 호출 깊이, k번 선택을 한 상태
#     # k 번 원소에 대한 선택 => cur_sum 에는 0 ~ k-1 원소들에 대한 선택이 저장
#     if k == N:
#         global cnt; cnt += 1
#         print(pick, sum(pick), cur_sum)
#     else:
#         # 첫번째 선택 => 저장, 계산작업
#         # k번 원소를 포함
#         pick.append(arr[k])
#         backtrack(k + 1, cur_sum + arr[k])
#         pick.pop()
#         # 초기상태로 돌아와서, 두번째 선택
#         # k 번 원소를 미포함
#         backtrack(k + 1, cur_sum)
# ---------------------------------------------------
# pick = [0] * N
# def backtrack(k, cur_sum):   # k: 현재 노드의 높이, 함수 호출 깊이, k번 선택을 한 상태
#     # k 번 원소에 대한 선택 => cur_sum 에는 0 ~ k-1 원소들에 대한 선택이 저장
#     if k == N:
#         global cnt; cnt += 1
#         print(pick, sum(pick), cur_sum)
#     else:
#         # 첫번째 선택 => 저장, 계산작업
#         # k번 원소를 포함
#         pick[k] = arr[k]
#         backtrack(k + 1, cur_sum + arr[k])
#         pick[k] = 0
#         # 초기상태로 돌아와서, 두번째 선택
#         # k 번 원소를 미포함
#         backtrack(k + 1, cur_sum)
# backtrack(0, 0)
# --------------------------------------------
pick = [0]
def backtrack(k, cur_sum, num):
    if k == N:
        global cnt; cnt += 1
        print(pick, sum(pick), cur_sum)
        print(len(pick), num)
    else:
        # 첫번째 선택 => 저장, 계산작업
        # k번 원소를 포함
        pick.append(arr[k])
        backtrack(k + 1, cur_sum + arr[k], num + 1)
        pick.pop()
        # 초기상태로 돌아와서, 두번째 선택
        # k 번 원소를 미포함
        backtrack(k + 1, cur_sum, num)

backtrack(0, 0, 0)
# print('cnt= ', cnt)