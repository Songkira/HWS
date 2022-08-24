# 선형큐
# 1. 직접구현
# Q의 크기를 예측하고 만들어 넣어야함. == 최소 정점의 크기(보통 문제에 명시되어 있음)
# Q = [0] * 10    # 저장소
# front = rear = -1

# def enqueue(item):  # 삽입
#     global rear
#     # full-check 필요 ==> rear == 마지막 인덱스
#     # rear가 마지막 인덱스를 가르키고 있으면 full
#     rear += 1
#     Q[rear] = item
#
# def dequeue():
#     # 이미 증가된 상태이기때문에 다음 dequeue 가 끝난 상황에서는
#     # 실제 저장된 내용은 front가 가리키는 곳에 그대로 남아있음. 하지만
#     # dequeue 하고나서 그 이후의 상황에서 front가 가리키는 곳은 데이터가 없는 공간.
#     # # 데이터가 있긴 있는데, 데이터가 없는 공간으로 간주한다!!!
#     global front
#     # 비어있을수 있따. empty-check ==> front == rear
#     # 비어있는지 비어있지 않은지 확인하고 꺼내는 행위를 하도록 코드를 항상 그렇게 짜야된다
#     front += 1
#     return Q[front]
#
# def isEmpty():
#     return front == rear

# enqueue(1)
# enqueue(2)
# enqueue(3)
#
# while not isEmpty():
#     print(dequeue())
# 1
# 2
# 3
# ---------------------------------------------

# 원형큐 구현
# QSIZE = 10
# Q = [0] * QSIZE    # 저장소
# front = rear = -1

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
    # 돌릴 필요가 있으면 돌리고, 없으면 앞으로 안돌리고
    # front == (rear + 1)% QSIZE 상황이면
    # 이렇게 했더니 rear 가 front가 가리키는 공간을 가리킴
    # front가 가리키는 공간은 비어있는 공간임. 거기에 저장하면 안됨
    # 비어있다. 라는 그냥 front 전용 공간임.
    # rear를 직접 증가시키면 안됨.
    return (rear + 1) % QSIZE

def isEmpty():
    return front == rear

import time
start = time.time()

# 스택 걸리는 시간 확인용
# stack = []
# for i in range(1000000):
#     stack.append(i)
#
# while stack:
#     stack.pop()
#
# print(time.time() - start) # 0.1680152416229248
#

# ----------------------------------------

# stack = []
# for i in range(100000):
#     stack.append(i)
#
# while stack:
#     stack.pop(0) # 맨앞에있는거 하나씩 빼는거
#     # 스택 => 단순히 앞에있는거 빼는 작업 뿐만 아니라
#     # 뒤에있는 얘들을 앞으로 하나씩 옮기는 작업도 추가됨
#
# print(time.time() - start)
# # 1000000개 일때: 안끝남
# # 100000개 일때: 11.534234...초

# -------------------------------
# queue를 사용할때 속도

# Q = [0] * 1000000
# front = rear = -1
# for i in range(1000000):
#     rear += 1
#     Q[rear] = i
#
# while front != rear:
#     front += 1
#     Q[front]
#
# print(time.time() - start)
# # 1000000개 일때: 0.20270705223...초
# # 100000개 일때: 0.021165370941...초

# -----------------------------------
# deque를 쓸때(import하는거)
from collections import deque

Q = deque()

for i in range(100000):
    Q.append(i)

while Q:
    Q.pop()
    # popleft() 리스트 앞쪽

print(time.time() - start)
# 1000000개 일때: 0.1508021....초
# 100000개 일때: 0.04380178...초

# -----------------------------------
# 선형큐의 경우
# 메모리의 영역을 잡는 것도 일
# ex. [0]*100만 기타 등등...
# 메모리를 처음 잡아놓고 쓰니까 매번 생각할 일 없음

# 1. queue를 쓸때는 List는 피하고(들어가는 양이 얼마안됨) append/pop 이 시간 잡아먹어서 안쓰는게 좋음
# 쓴다면 직접 구현해서 선형큐처럼 메모리 확보후 잡아놓고 front, rear 늘려가면서 쓰던가
# 2. 원형큐를 쓴다는 것은 메모리를 효율적으로 쓴다는 것과 동일
# 최대크기를 잡아놓고 쓸려면 굳이 원형큐를 쓸 필요 없음.
# 3. 둘다 싫으면 deque을 쓰던가 (자제) 왜냐면 파이썬에서만 사용 가능하니까. 다른 언어에서도 적용할수 있는 방법 익히기