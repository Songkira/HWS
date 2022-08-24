# N = 3
# q = [0] * N
# front = -1
# rear = -1

# rear += 1           # enqueue(10)
# q[rear] = 10
#
# rear += 1           # enqueue(20)
# q[rear] = 20
#
# rear += 1           # enqueue(30)
# q[rear] = 30
#
# # #--------------------------------------
# # rear += 1           # enqueue(40)
# # q[rear] = 40
# # # 크기보다 많은 값을 넣어서 인덱스 에러 발생
# # # IndexError: list assignment index out of range
# # # --------------------------------------
#
# front += 1              # dequeue()
# print(q[front])
# # dequeue를 했다고 지워지는 건 아님. Queue 안에 남아있지만 'dequeue한 자리'이후로 계속 꺼낼것이기 때문에
# # 이미 꺼내진 얘가 지워지는 건 아니지만 그 앞에거를 특별히 가져다 쓰는 것은 아니라고? 그냥 무시하는 거라고 함.
# front += 1              # # dequeue()
# print(q[front])
#
# front += 1              # dequeue()
# print(q[front])
# 10
# 20
# 30
#--------------------------------------------

# 순환 큐
N = 3
q = [0] * N
front = 0
rear = 0

# rear = (rear + 1) % N #순환 queue           # enqueue(10)
# q[rear] = 10
#
# rear = (rear + 1) % N #순환 queue           # enqueue(20)
# q[rear] = 20
#
# rear = (rear + 1) % N #순환 queue           # enqueue(30)
# q[rear] = 30
#
# front = (front + 1) % N             # dequque()
# print(q[front])
#
# front = (front + 1) % N             # dequque()
# print(q[front])
#
# front = (front + 1) % N             # dequque()
# print(q[front])
# # 10
# # 20
# # 30

# -------------------------------------------
# 순환 큐가 아닐땐 40을 넣으면 index Error이 떴다.
# 순환 큐인 지금은?
rear = (rear + 1) % N #순환 queue           # enqueue(10)
q[rear] = 10

rear = (rear + 1) % N #순환 queue           # enqueue(20)
q[rear] = 20

rear = (rear + 1) % N #순환 queue           # enqueue(30)
q[rear] = 30

rear = (rear + 1) % N #순환 queue           # enqueue(40)
q[rear] = 40

front = (front + 1) % N             # dequque()
print(q[front])

front = (front + 1) % N             # dequque()
print(q[front])

front = (front + 1) % N             # dequque()
print(q[front])
# 40
# 20
# 30