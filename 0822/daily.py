import sys; sys.stdin = open('계산기.txt', 'r')

# # 우선순위 만들기
# def priority(x):
#     if x == '*':
#         return 3
#     elif x == '+':
#         # pop가로안에 아무것도 안써도 맨마지막 데이터 방출
#         return 2
#     else:
#         return 1
#
#
#
# for tc in range(1):
#     n = int(input())
#     arr = list(input())
#
#     size = 100
#     stack_num = [0] * size
#     stack_san = [0] * size
#     top = -1
# # print(arr)
#     for i in range(n):
#         top += 1
#         if i % 2 == 0:
#             stack_num[top] = int(arr[i])
#         if i % 2 == 1:
#             top -= 1
#             stack_san[top] = arr[i]
#             if stack_san[top-1] == '*' and stack_san[top] == '+':
#                 stack_san.pop()
#                 top -= 1
#
#     print(stack_num)
#     print(stack_san)

#--------------------------------------------------------------
for case in range(1, 11):
    N = int(input())  # 케이스 길이

    # set은 해쉬?를 사용해서 List 보다 용량을 적게 잡아먹음.
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # 피연산자
    operator = ['+', '-']  # 연산자
    middle = input()  # 중위 표기법
    top = -1  # top
    stack = [[] for _ in range(N)]  # 스택
    rear = ''  # 후위 표기법
    for i in range(N):
        if middle[i] in num:  # 피연산자인 경우
            rear += middle[i]  # 후위 표기법에 추가
        else:  # 연산자인 경우
            if top == -1:  # 스택이 빈 경우
                top += 1  # 스택에 연산자 추가
                stack[top] = middle[i]
            else:  # 스택이 비어있지 않은 경우
                if middle[i] == '+':  # +인 경우 우선 순위가 낮아 모든 연산자 꺼냄
                    while top > -1:  # top에 같은 연산자가 있으면 꺼내기
                        rear += stack[top]
                        top -= 1
                    top += 1  # 스택에 추가
                    stack[top] = middle[i]
                else:
                    while top > -1 and stack[top] == middle[i]:  # *인 경우(우선 순위가 가장 높기 때문에 같은 연산자만 제거)
                        rear += stack[top]
                        top -= 1
                    top += 1  # 스택에 추가
                    stack[top] = middle[i]
    # if top != -1:
    while top > -1:  # 스택이 비어있지 않으면 비우기
        rear += stack[top]
        top -= 1

    for i in range(N):
        if rear[i] in num:  # 숫자를 스택에 추가
            top += 1
            stack[top] = int(rear[i])
        else:
            num2 = stack[top]; top -= 1
            num1 = stack[top]; top -= 1# 스택에서 숫자 2개를 꺼내서 연산
            if rear[i] == '+':  # + 연산자
                stack[top] = num1 + num2  # 다시 스택에 넣기
            else:
                # * 연산자
                stack[top] = num1 * num2
            top += 1
    print(f'#{case} {stack[top]}')