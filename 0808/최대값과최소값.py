import sys; sys.stdin=open('sample_input.txt', 'r')
# 최대값의 '위치'와 최소값의 '위치' 의 차이값 구하는 문제
# T = int(input())
#
# for tc in range(T):
#     n = int(input())
#     arr = list(map(int, input().split()))

# # 이것도 버블정렬 사용하면 될것 같음
#     for i in range(n-1,0,-1):
#         for j in range(0, i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1],arr[j]
#     print(arr)
#     # 정렬된상태니까 단순계산만 진행하면 될듯
#     # 왜냐면 작은 수가 여러개 라도 가장먼저 나오는 위치이고
#     # 큰수가 여러개라도 마지막 위치니까 고정되어이 있음.
#     # print(arr[-1]-arr[0])
#
#     # 문제 또 잘못 이해함-> 위치값을 빼는 거였음.
#     # 가장 큰수 여러개면 맨 마지막 위치니까 n 이고
#     # 작은 수가 여러개면 가장 먼저 나오는 위치니까 1일텐데..
#     print(f'#{tc+1}', n - 1)
#-------------------------------------------

# 최대, 최소 값이라서 정렬필요한줄 알았는데 아니었음
# 절대값 구하는 거니까 abs 사용
T = int(input())

for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    max_idx = 0
    min_idx = 0
    for i in range(n):
        # 가장 큰수는 맨 뒤에 있는걸로 가정하므로, 같은 크기의 수가 나오면 정리('<='일때, max_idx = i).
        if arr[max_idx] <= arr[i]:
            max_idx = i
        # 가장 작은 수는 맨 앞에 있는걸로 가정하므로, 같은 크기의 수가 나오면 정리하지 않음(신경쓰지않음).
        if arr[min_idx] > arr[i]:
            min_idx = i

    print(f'#{tc+1}', abs(max_idx - min_idx))