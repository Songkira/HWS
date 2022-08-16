import sys; sys.stdin = open('4861.txt', 'r')


# for tc in range(1, int(input())+1):
#     N, M = list(map(int, input().split()))
#     arr = [input().split() for _ in range(N)]
    # 일단 기준이 되는 문자열을 찾아야되는데 어디서부터?
    # 구간합?
    #
    # # word = ''
    # for chr in arr:
    #     word = ''
    #     for i in range(N):
    #         for j in range(M//2):
    #             if chr[i][j] != chr[i][M - 1 - j]:
    #                 pass
    #             else:
    #                 word = chr[i]
    #     print(word)
        # for i in range(N):
        #      for j in range(M):
        #          if chr[i] == chr[M - 1 - i]:


    # s = e = 0
    # middle = M // 2
    # for i in range(N):
    #     for j in range(M):
    #         if arr[i][j] !=


    # print(f'#{tc} {arr}')

# 행(문자열)에서 주어진 길이의 회문을 찾을수 있으면 OK!!

# 문자열이 주어졌을때
arr = 'ASDGFJFTLMMHOOOHMMLT'
N = 20
M = 13

for i in range(N//2):
    if arr[i] != arr[N -1 -i]:
        break
else:
    print('회문찾음!')

# 모든 가능한 경우/ 회문이 있을수 있는 시작 위치

# 모든 가능한 경우/ 회문이 있을수 있는 시작 위치
for s in range(N - M + 1):
    e = s + M - 1
    for i in range(N // 2):
        if arr[s + i] != arr[e - i]:
            break
    else:
        ans = ''
        for i in range(s, e+1):
            ans += arr[i]
        break
print(ans)

def find_palindrome(arr, N, M):
    # 모든 행에 대해서
    # 모든 가능한 경우/ 회문이 있을수 있는 시작 위치
    for row in range(N - M + 1):
        e = s + M - 1
        for i in range(N // 2):
            if arr[row][s + i] != arr[row][e - i]:
                break
        else:
            ans = ''
            for i in range(s, e+1):
                ans += arr[row][i]
            return ans

        for row in range(N - M + 1):
            e = s + M - 1

            for i in range(N // 2):
                if arr[s + i][row] != arr[e - i][row]:
                    break


for tc in range(1, int(input())+1):
    N, M = list(map(int, input().split()))
    arr = [input() for _ in range(N)]