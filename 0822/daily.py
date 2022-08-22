import sys; sys.stdin = open('계산기.txt', 'r')

# 우선순위 만들기
def priority(x):
    if x == '*':
        return 3
    elif x == '+':
        # pop가로안에 아무것도 안써도 맨마지막 데이터 방출
        return 2
    else:
        return 1



for tc in range(1):
    n = int(input())
    arr = list(input())

    size = 100
    stack_num = [0] * size
    stack_san = [0] * size
    top = -1
# print(arr)
    for i in range(n):
        top += 1
        if i % 2 == 0:
            stack_num[top] = int(arr[i])
        if i % 2 == 1:
            top -= 1
            stack_san[top] = arr[i]
            if stack_san[top-1] == '*' and stack_san[top] == '+':
                stack_san.pop()
                top -= 1

    print(stack_num)
    print(stack_san)