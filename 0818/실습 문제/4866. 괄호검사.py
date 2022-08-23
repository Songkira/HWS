import sys; sys.stdin = open('4866.txt', 'r')


# def push(item):
#     global top
#     top += 1
#     if top >= 0:
#       stack[top] = item

# def push(item):
#     # global top
#     stack.append(item)
#     # top += 1
#
# def pop():
#     if len(stack) == 0:
#         return
#     else:
#         return stack.pop(-1)
for tc in range(1, int(input()) + 1):
    words = input()
    lst1 = ['[', '{', '(']
    stack = []

    for i in words:
        if i in lst1:
            stack.append(i)
        elif i == '}':
            if len(stack) == 0:
                ans = 0
                break
            elif stack.pop() != '{':
                ans = 0
                break
        elif i == ')':
            if len(stack) == 0:
                ans = 0
                break
            elif stack.pop() != '(':
                ans = 0
                break
    # if len(stack) != 0:
        # for i in words:
        #     if i == ')':
        #         if stack[top] == '(':
        #             stack.pop()
        #         else:
        #             break
        #     elif i == '}':
        #         if stack[top] == '{':
        #             stack.pop()
        #         else:
        #             break
    # else:
    #     print(f'#{tc} 0')
    #     break
    else:
        if len(stack):
            ans = 0
        else:
            ans = 1

    print(f'#{tc} {ans}')
    #
    # for case in range(1, int(input()) + 1):
    #     code = input()
    #     stack = []  # 여는 괄호를 저장할 리스트
    #     for ch in code:  # 입력받은 문자열 순회
    #         if ch in openPa:  # 여는 괄호인 경우 리스트에 추가
    #             stack.append(ch)
    #         elif ch == '}':  # '}'인 경우
    #             if len(stack) == 0:  # pop 하기 전 리스트가 비었다면 0
    #                 ans = 0
    #                 break
    #             elif stack.pop() != '{':  # pop 하고 반환값이 '{'가 아닌 경우 0
    #                 ans = 0
    #                 break
    #         elif ch == ')':  # ')'인 경우 pop 하고 반환값이 '('가 아닌 경우 0
    #             if len(stack) == 0:  # pop 하기 전 리스트가 비었다면 0
    #                 ans = 0
    #                 break
    #             elif stack.pop() != '(':
    #                 ans = 0
    #                 break
    #     else:
    #         if len(stack):  # 리스트에 괄호가 남아있으면 0
    #             ans = 0
    #         else:
    #             ans = 1  # 리스트가 비었다면 1
    #     print(f'#{case} {ans}')
    # # 다른건 생략하고 괄호만 남기기?
    # # 괄호 리스트를 따로 만들고 그것과 비교하기?
    #
    # bracket1 = []
    # bracket2 = []
    # for i in words:
    #     for j in range(len(lst1)):
    #         if i == lst1[j]:
    #             bracket1.append(i)
    #     for k in range(len(lst2)):
    #         if i == lst2[k]:
    #             bracket2.append(i)
    # print(bracket1, bracket2)

    # if len(bracket1) == len(bracket2):
    #     print(f'#{tc} 1')
    # else:
    #     print(f'#{tc} 0')