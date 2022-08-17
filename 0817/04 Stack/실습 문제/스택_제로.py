import sys; sys.stdin = open('sample_input (2).txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    stack = []

    for i in arr:
        if i != 0:
            stack.append(i)
        elif i == 0:
            stack.pop()

    sum = 0
    for i in stack:
        sum += i

    print(f'#{tc} {sum}')
