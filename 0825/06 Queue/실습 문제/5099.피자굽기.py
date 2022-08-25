import sys; sys.stdin = open('5099.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split()) # N : 화덕크기, M:피자의 개수
    lst = [0] + list(map(int, input().split())) # lst: 피자의 치즈양 리스트
    # 피자번호 리스트 따로 만들기
    number = [0]
    # 돌리는 화덕 크기
    Q = [0]*(N+1)
    front = 0
    rear = 0
    for i in range(1, M+1):
        number.append(i)

    for i in range(1, N+1):
        rear += 1
        Q[rear] = [number[i], lst[i]]
    print(Q)

    # cnt = 0
    # while cnt == (M-1):
    rear = (rear+1) % (N+1)
    front = (front+1) % (N+1)
    Q[rear][1] = Q[front][1]//2
    Q[rear] = Q[front]
    print(Q)
        # if Q[front][1] == 0:
        #     cnt += 1