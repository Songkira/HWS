import sys; sys.stdin = open('1224.txt', 'r')

'''
[1단계] 중위표기법 => 후위표기법으로 변환
1) 입력 받은 중위 표기식에서 토큰을 읽는다.
2) 토큰이 피연산자이면 토큰을 출력한다
3) 토큰이 연산자(괄호포함)일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고, 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop 한 후 토큰의 연산자를 push한다. 만약 top에 연산자가 없으면 push한다.
4) 토큰이 오른쪽 괄호 ‘)’이면 스택 top에 왼쪽 괄호 ‘(‘가 올 때까지 스택에 pop 연산을 수행하고 pop 한 연산자를 출력한다. 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않는다.
5) 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1부터 다시 반복한다.
6) 스택에 남아 있는 연산자를 모두 pop하여 출력한다.
 - 스택 밖의 왼쪽 괄호는 우선 순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮다.
'''

'''
[2단계] 후위표기법 수식을 계산 
1) 피연산자를 만나면 스택에 push 한다. 
2) 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push 한다. 
3) 수식이 끝나면, 마지막으로 스택을 pop하여 출력한다.
'''
# 교수님 풀이
icp = {'+': 1, '*': 2, '(': 3, ')': 0} # in-coming priority
isp = {'+': 1, '*': 2, '(': 0, ')': 0} # in-stack priority
N = int(input())
infix = input()
postfix = ''
S = []

# for token in infix:
#     if token in icp:    # 연산자
#         if token == ')':
#             while S and S[-1] != '(': # 현재 꼭대기에있는게 ')'(여는 괄호)가 아니면
#                 postfix += S.pop()
#             S.pop()
#         else: # '+', '*', '('
#             while S and icp[token] <= isp[S[-1]]:  # 스택의 우선순위가 크거나 같으면 스택에 있는 얘를 뽑아서 출력
#                 postfix += S.pop()
#             S.append(token)
#     else:
#         postfix += token
# while S:
#     postfix += token
# -----------------------------------------

# for token in postfix:
#     if token in icp:
#         b = S.pop()# 처음 pop한거
#         a = S.pop()# 뒤에 pop한거?
#         if token == '+':
#             S.append(a + b)
#         else:
#             S.append(a * b)
#     else:
#         S.append(int(token))
# print(postfix)
#--------------------------------------------------------------
# # 내가 쓴 코드
# def calculate(arr):
#     stack = []
#     for i in range(len(arr)):
#         if arr[i] == '+':
#             B = stack.pop()
#             A = stack.pop()
#             stack.append(A + B)
#         elif arr[i] == '-':
#             B = stack.pop()
#             A = stack.pop()
#             stack.append(A - B)
#         elif arr[i] == '*':
#             B = stack.pop()
#             A = stack.pop()
#             stack.append(A * B)
#         elif arr[i] == '/':
#             B = stack.pop()
#             A = stack.pop()
#             stack.append(A / B)
#         else:
#             stack.append(arr[i])
#     return stack
#
#
# for tc in range(1, 11):
#     prior = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
#
#     N = int(input())
#     arr = input()
#     stack = []
#     stack_num = []
#     for n in range(N):
#         if arr[n].isdigit():
#             stack_num.append(int(arr[n]))
#         elif arr[n] == '(':
#             stack.append((arr[n]))
#         elif arr[n] == ')':
#             while stack[-1] != '(':
#                 stack_num.append(stack.pop())
#             stack.pop()
#         else:
#             while stack and prior[arr[n]] <= prior[stack[-1]]:
#                 stack_num.append(stack.pop()) # pop한것들은 lst에 추가 시켜줌
#             stack.append(arr[n]) # 위의 조건이 완료 되면 stack에 추가
#
#     while len(stack) != 0:  # stack에 남아있는 연산자들 lst에 추가
#         stack.append(stack.pop())
#
#     print(f'#{tc}', *calculate(stack_num))
# #1 672676
# #2 1974171
# #3 12654
# #4 38756
# #5 4035
# #6 155304
# #7 6964
# #8 2819
# #9 24711
# #10 208785

# ---------------------------------------------------
# def calculate(post_ex):
#     n = len(post_ex)
#     stack = []
#     for i in range(n):
#         # 숫자면 stack
#         if post_ex[i].isdigit():
#             stack.append(post_ex[i])
#         else:
#             # 곱하기 나오면 두개빼서 곱하고 다시 넣음
#             if post_ex[i] == '*':
#                 stack.append(int(stack.pop()) * int(stack.pop()))
#             # 더하기 나오면 두개 빼서 더하고 다시 넣음
#             elif post_ex[i] == '+':
#                 stack.append(int(stack.pop()) + int(stack.pop()))
#             else:
#                 stack.pop()
#     return stack[0]
#
#
# def make_post(expression):
#     isp = {'+': 1, '-': 1, '*': 2, '/': 2, ')': 0, '(': 0}
#     icp = {'+': 1, '-': 1, '*': 2, '/': 2, ')': 0, '(': 3}
#     stack = []
#     ans = ""
#     for s in expression:
#         if s.isdigit():
#             ans += s
#         elif s == ')':
#             while stack and stack[-1] != '(':
#                 ans += stack.pop()
#             stack.pop()
#         else:
#             while stack and icp[s] <= isp[stack[-1]]:
#                 ans += stack.pop()
#             stack.append(s)
#     while stack:
#         ans += stack.pop()
#     return ans
#
#
# for test in range(1, 11):
#     n = int(input())
#     print(f'#{test} {calculate(make_post(input()))}')