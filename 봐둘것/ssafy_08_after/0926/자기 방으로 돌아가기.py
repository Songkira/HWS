import sys; sys.stdin=open('자기 방으로 돌아가기.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    # room_ = [0] * (400+1)

    # room_even = []  # 짝
    # room_odd = []   # 홀
    # for i in range(1, 400+1):
    #     if i % 2:
    #         room_odd.append(i)
    #     else:
    #         room_even.append(i)

    for _ in range(N):
        pla, ret = map(int, input().split())

