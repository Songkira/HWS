# 백트래킹과 dp는 연결되어 있다?

# import sys; sys.stdin = open('')

# 더이상 쪼갤수 없는 유일한 단위 = 내가 종이를 이어 붙일때 쓸수있는 방법 3개\
# paper = # 내가 쓸수 있는 종이

N = 3
tmp = [] # 현재까지 붙여진 종이
cnt = 0
# def paper(n): # 현재 종이 길이 / 만들어진 종이 크기의 상태
#     if n > N: return
#     if n == N: # N과 같아질때까지 더해지는 값을 cnt +
#         global cnt; cnt += 1
#         print(*tmp)
#         return
#     else:
#         tmp.append('ㅣ')
#         paper(n + 1)
#         tmp.pop()
#
#         tmp.append('ㅁ')
#         paper(n + 2)
#         tmp.pop()
#
#         tmp.append('=')
#         paper(n + 2)
#         tmp.pop()
#
# paper(0)
# print('cnt = ', cnt)

# -----------------------
def paper(n):  # 현재 종이 길이 / 만들어진 종이 크기의 상태
    if n < 0: return
    if n == 0: # 0이 될때까지 차감되는 값을 cnt +
        global cnt; cnt += 1
        print(*tmp)
        return
    else:
        tmp.append('ㅣ')
        paper(n - 1) # 10, 20을 쓸때
        tmp.pop()

        tmp.append('ㅁ')
        paper(n - 2) # 20, 20을 쓸때
        tmp.pop()

        tmp.append('=')
        paper(n - 2) # (10, 20) 2개를 붙여 20, 20으로 만들어놨을경우
        tmp.pop()

paper(N)
print('cnt = ', cnt)