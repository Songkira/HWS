import sys; sys.stdin = open('피자 굽기.txt', 'r')

# 이수민 코드
# for tc in range(1, int(input())+1):
#     N,M = map(int, input().split())
#     Q = [0] * (N + 1)
#     front = rear = 0
#
#     def enqueue(item):  # 삽입
#         global rear
#         rear = (rear + 1) % (N+1)
#         Q[rear] = item
#
#     def dequeue():
#         global front
#         front = (front + 1) % (N+1)
#         return Q[front]
#
#     def isFull():
#         return (rear + 1) % (N+1)
#
#     def isEmpty():
#         return front == rear
#
#     pizza = list(map(int, input().split()))
#     for i in range(M):
#         enqueue((pizza[i], i + 1))
#         while isFull():
#             chz, num = dequeue()
#             new_pizza = (chz // 2, num)
#             if new_pizza[0] != 0:
#                 enqueue(new_pizza)
#
#         while True:
#             if isEmpty():
#                 break
#             chz, num = dequeue()
#             new_pizza = (chz // 2, num)
#             if new_pizza[0] != 0:
#                 enqueue(new_pizza)
#
#     print(f'#{tc}', num)

# ------------------------------------------------------
# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     cheeze = list(map(int, input().split()))
#     Q = [[[0, 0]] + [[cheeze[i], i]] for i in range(N)]
#
#     i = N - 1
#     front, rear = 0, N
#     while True:
#         for q in Q:         # 비어있는지
#             if q[0] != 0:   # 체크
#                 front = (front + 1) % (N+1)
#                 rear = (rear + 1) % (N+1)
#                 if Q[front][0] // 2 == 0:
#                     if i + 1 <M:
#                         i += 1
#                         Q[rear] = [cheeze[i], i]
#                     else:
#                         Q[rear] = [0, Q[front][1]]
#                 else:
#                     Q[rear] = [Q[front][0] // 2, Q[front][1]]
#                 break
#         else:
#             break
#
#     print(f'#{tc} {Q[rear-1][1]+1}')

# ------------------------------------------------
# 교수님 코드
SIZE = 30
Q = [0] * (SIZE + 1)
front = rear = 0

def enqueue(item):  # 삽입
    global rear
    rear = (rear + 1) % SIZE
    Q[rear] = item

def dequeue():
    global front
    front = (front + 1) % SIZE
    return Q[front]

def isFull():
    return (rear + 1) % SIZE

def isEmpty():
    return front == rear

for tc in range(1, int(input())+1):
    N, M = map(int, input().split()) # N : 화덕 크기, M :피자 개수
    pizza = [0] + list(map(int, input().split()))
    # 큐 초기화

    # N 개의 피자를 삽입
    for i in range(1, N + 1):
        enqueue(i)

    # 남은 피자에 대한 정보
    remain = N + 1
    while (front + 1) % SIZE != rear:# 하나만 남을때까지
        num = dequeue()
        pizza[num] //= 2
        if pizza[num] == 0:
            if remain <= M:
               enqueue(remain)
               remain += 1

        else:
            enqueue(num)

    print(f'#{tc} {Q[rear]}')









