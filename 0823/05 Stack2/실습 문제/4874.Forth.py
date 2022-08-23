import sys; sys.stdin = open('4874.txt', 'r')
#1 84
#2 error
#3 168
# def calculate(arr):
#     stack = []
#     a = 'error'
#     try:
#         for i in range(len(arr)):
#             if arr[i] == '+':
#                 B = stack.pop()
#                 A = stack.pop()
#                 stack.append(A + B)
#             elif arr[i] == '-':
#                 B = stack.pop()
#                 A = stack.pop()
#                 stack.append(A - B)
#             elif arr[i] == '*':
#                 B = stack.pop()
#                 A = stack.pop()
#                 stack.append(A * B)
#             elif arr[i] == '/':
#                 B = stack.pop()
#                 A = stack.pop()
#                 stack.append(A / B)
#             else:
#                 stack.append(arr[i])
#         return stack
#     except:
#         return "".join(a)


for tc in range(1, int(input())+1):
    arr = input().split()
    N = len(arr)
    stack = []
    for n in range(N):
        if arr[n].isdigit():
            stack.append(int(arr[n]))
        elif arr[n] == '+' or arr[n] == '*' or arr[n] == '/' or arr[n] == '-':
            if len(stack) > 1:
                if arr[n] == '+':
                    B = stack.pop()
                    A = stack.pop()
                    stack.append(A + B)
                elif arr[n] == '-':
                    B = stack.pop()
                    A = stack.pop()
                    stack.append(A - B)
                elif arr[n] == '*':
                    B = stack.pop()
                    A = stack.pop()
                    stack.append(A * B)
                elif arr[n] == '/':
                    B = stack.pop()
                    A = stack.pop()
                    stack.append(A // B)
            else:
                result = 'error'
                break
        elif arr[n] == '.':
            if len(stack) == 1:
                result = stack[0]
            else:
                result = 'error'

    print(f'#{tc} {result}')
# ---------------------------------------------
# for tc in range(1, int(input()) + 1):
#     arr = list(input().split())
#     new_arr = []
#     for i in arr:
#         if i == '.':
#             if len(new_arr) == 1:
#                 result = new_arr[0]
#             else:
#                 result = 'error'
#         elif i == '+' or i == '-' or i == '*' or i == '/':
#             if len(new_arr) > 1:
#                 if i == '+':
#                     num2 = new_arr.pop()
#                     num1 = new_arr.pop()
#                     new_num = int(num1) + int(num2)
#                     new_arr.append(new_num)
#                 elif i == '*':
#                     num2 = new_arr.pop()
#                     num1 = new_arr.pop()
#                     new_num = int(num1) * int(num2)
#                     new_arr.append(new_num)
#                 elif i == '-':
#                     num2 = new_arr.pop()
#                     num1 = new_arr.pop()
#                     new_num = int(num1) - int(num2)
#                     new_arr.append(new_num)
#                 elif i == '/':
#                     num2 = new_arr.pop()
#                     num1 = new_arr.pop()
#                     new_num = int(num1) // int(num2)
#                     new_arr.append(new_num)
#             else:
#                 result = 'error'
#                 break
#         else:
#             new_arr.append(i)
#
#     print(f'#{tc} {result}')



