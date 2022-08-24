# 원형큐 사용시
import sys; sys.stdin = open('암호생성기.txt', 'r')

# 최소로 저장하기 위한 공간을 만들려면 필요한 크기는 얼마로 잡아야 되나? 9
QSIZE = 9 # 8개의 데이터를 받아야하고 front 공간 1개 필요
Q = [0] * QSIZE    # 저장소
# 원형큐는 front = rear = 0으로 시작해야함.
front = rear = 0

def enqueue(item):  # 삽입
    global rear
    # full-check 필요 ==> rear == 마지막 인덱스
    # mod 연산/ 모듈러 연산?
    rear = (rear + 1) % QSIZE
    Q[rear] = item

def dequeue():
    global front
    front = (front + 1) % QSIZE
    return Q[front]

def isFull():
    return (rear + 1) % QSIZE

def isEmpty():
    return front == rear

for tc in range(1, 11): # 매 테스트케이스마다 Q 초기화 되야함=> 비우는 것
    tc_num = input()
    arr = list(map(int, input().split()))

    front = rear = 0
    for val in arr:
        enqueue(val)

    cnt = 1
    while Q[rear]:
        val = dequeue()
        val -= cnt
        cnt = 1 if cnt == 5 else cnt + 1
        # if cnt == 6:
        #     cnt = 1
        # if val <= 0:        # 중단
        #     enqueue(0)
        val = 0 if val < 0 else val
        enqueue(val)

# print(Q)
# print(front, rear)
# # [4, 1, 3, 0, 3, 6, 2, 2, 9]
# # 4 3
# # front [4]자리의 3은 없는 거. rear 은 [3]
    print(f'#{tc}', end= ' ')
    while front != rear:
        print(dequeue(), end=' ')
        # 6 2 2 9 4 1 3 0
    print()
# print(Q)
# print(front, rear)
# # [0, 9550, 9556, 9550, 9553, 9558, 9551, 9551, 9551]
# # 0 8
# front는 0 / rear은 9551 (인덱스 8자리) 을 가리키고 있음