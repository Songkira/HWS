#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     Q = [0] * N
#     front = rear = 0
#
#     for i in range(1, N+1): # Q에 1부터 N까지의 숫자를 넣어줌
#         rear = (rear + 1) % N
#         Q[rear] = i
#         print(Q)
#         # print('-------')
#     # 가장 마지막에 남는 카드가 필요하니 작업은 N-1까지만
#     for i in range(N-1):
#         front = (front+2) % N
#         rear = (rear+1) % N
#         print(rear, front)
#         Q[rear] = Q[front]
#         print(Q)
#     print(f'#{tc}', Q[rear])
# ------------------------------------
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     front = -1
#     rear = -1
#     card = [0] * N
#
#     while True:
#         if front == rear - 1:
#             break
#         for i in range(N):
#             rear = (rear + 1) % N
#             card[rear] = i + 1
#
#         for i in range(N - 1):
#             front = (front + 2) % N
#             rear = (rear + 1) % N
#             card[rear] = card[front]
#
#     print(f'#{tc}', card[rear])

# -------------------------------------
# # 선형 큐 방식
# def dequeue():
#     global front
#     front += 1
#     return Q[front]
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     Q = [0] * 99999
#     front = -1
#     rear = -1
#
#     for i in range(1, N + 1):  # Q에 1부터 N까지의 숫자를 넣어줌
#         rear = rear + 1
#         Q[rear] = i
#
#     # 마지막 카드 하나만 남으면 되니까 rear와 front 값이 같아지면 멈춤.
#     while rear != front:
#         i = dequeue()
#         if front % 2:
#             rear += 1
#             Q[rear] = i
#
#     print(f'#{tc}', Q[rear])

# -------------------------------------------
# 원형큐
# 데이터가 웬만큼 많다고 생각되면 원형큐가 더 효율적.
# front 자리는 채워져있어도 데이터 없는셈 치기때문에 원칙적으로 자리를 +1(예. [0]) 로 해서 만들어줘야함.
#

for case in range(1, int(input()) + 1):
    N = int(input())
    q = [0] + [i for i in range(1, N + 1)]  # 카드(큐)
    front = 0
    rear = N
    print(q)
    # front == rear 은 빈공간[]이 됨.
    # front == rear-1이면 한칸 만 남음.
    # 즉 front != rear-1 은 한칸 만 남기고 멈추라는 의미.
    while front != rear - 1:
        front = (front + 2) % (N + 1)  # 2칸 넘어감
        rear = (rear + 1) % (N + 1)
        q[rear] = q[front]  # 2칸 넘어간 후 나오는 값을 뒤에 추가
        print(front, rear)
        print(q)
    print(f'#{case} {q[rear]}')