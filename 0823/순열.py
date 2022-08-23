# 현재상태를 나타내는 데이터가 있어야함.

# 상태공간 트리
arr= [10, 20, 30, 40]
N = 4

# for i in range(N):
#     arr[0], arr[i] = arr[i], arr[0] # 인덱스 0 위치만 바뀜
#     print(arr,'-----------')
#     arr[0], arr[i] = arr[i], arr[0]
#     print(arr)
# # [10, 20, 30, 40] -----------
# # [10, 20, 30, 40]
# # [20, 10, 30, 40] -----------
# # [10, 20, 30, 40]
# # [30, 20, 10, 40] -----------
# # [10, 20, 30, 40]
# # [40, 20, 30, 10] -----------
# # [10, 20, 30, 40]

# ------------------------------------
# for i in range(N):
#     arr[0], arr[i] = arr[i], arr[0]
#     # ==============================
#     for j in range(1, N):
#         arr[1], arr[j] = arr[j], arr[1]
#         print(arr)
#         arr[1], arr[j] = arr[j], arr[1]
#     #================================
#     arr[0], arr[i] = arr[i], arr[0]
# ---------------------------------------
# N 개일때 0 ~ N-2까지 시작 범위 바꿔서 for 문 중첩
# N 이 되면 끝내야 되니까 N-1이 포함될 범위까지 산정
# for i in range(N):
#     arr[0], arr[i] = arr[i], arr[0]
#     # ==============================
#     for j in range(1, N):
#         arr[1], arr[j] = arr[j], arr[1]
#         # ==============================
#         for k in range(2, N):
#             arr[2], arr[k] = arr[k], arr[2]
#             print(arr)
#             arr[2], arr[k] = arr[k], arr[2]
#         # ================================
#         arr[1], arr[j] = arr[j], arr[1]
#     #================================
#     arr[0], arr[i] = arr[i], arr[0]

#--------------------------------------

def perm(k):
    if k == N:
        print(arr)
        return
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k+1)
            arr[k], arr[i] = arr[i], arr[k]
perm(0)