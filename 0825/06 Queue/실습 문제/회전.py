import sys; sys.stdin = open('회전.txt', 'r')

# 선형큐
# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     Q = list(map(int, input().split())) + [0]* 99999
#
#     front = -1
#     rear = N - 1
#     print(rear, front)
#
#     for i in range(M):
#         rear += 1
#         front += 1
#         Q[rear] = Q[front] # rear 자리에 front 데이터 입력
#                             # front는 데이터 없음 == 빈공간 으로 정해져있음
#         # print(rear, front)
#     # 남아있는 수열중 맨 앞에 있는 숫자를 출력해야함
#     # front 자리는 데이터 없는셈 치기때문에 그다음 인덱스(+1) 출력
#     print(f'#{tc}', Q[front+1])

# ===========================================
# 원형 큐
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    Q = [0] + list(map(int, input().split()))

    front = 0
    rear = N

    for i in range(M):
        front = (front+1) % (N + 1)
        rear = (rear+1) % (N + 1)
        Q[rear] = Q[front]

    # 인덱스 범위를 벗어나서 런타임에러 발생
    # print(f'#{tc}', Q[front+1])
    #===================================
    # 원형 큐니까 mod로 나눠줘야 인덱스가 맞게 나옴
    print(f'#{tc}', Q[(front+1) % (N + 1)]) 