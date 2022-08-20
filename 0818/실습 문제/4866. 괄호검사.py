import sys; sys.stdin = open('4866.txt', 'r')

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

    else:
        if len(stack):
            ans = 0
        else:
            ans = 1

    print(f'#{tc} {ans}')
