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
#-----------------------------------------
# 행(문자열)에서 주어진 길이의 회문을 찾을수 있으면 OK!!

# 문자열이 주어졌을때
# arr = 'SDGFTLMMHOOOHMMLTGDS'
# N = 20
# M = 13
#
# # s 와 e 가 같이 증가하면서 같은 문자 나올때까지 i를 0으로 유지된다. 왜지?
# # 'M - 1 길이만큼' 이라는 첫번째 조건이 충족 되야함.
# # arr[s+i] != arr[e-i] -> arr[0+0]!=[12-0]-> if S != H 라는 조건이 맞으니까 멈춤(break)
# # 그래서 i가 0이 유지되는 것처럼 보였던거지. 조건이 맞아서 멈추고 위 for문으로 돌아가는 거니까
# # [0+0]==[12-0] -> [1+0]==[13-0] -> [2+0][14-0]->...
# # if arr[s + i] != arr[e - i] 조건이 틀리게 되면 -> arr[4+0]==arr[16-0] -> T == T
# # 즉, arr[s+i]==arr[e-i]이면 break로 가지 않고 i가 증가하면서 계속 확인.
# # 결론은 break로 한번도 안가게되면 회문이 있다는 거.
# # 중간에 조건이 맞게되면(!=) break로 가게되고 중지되면서 다시 확인하기 위해 s랑 e는 증가할거야.
# # 그리고 회문이라는 두번째 조건이 충족될려면 앞숫자는 커지고(+i) 뒷숫자는 줄어들어야지(-i)
# for s in range(N - M + 1):
#     e = s + M - 1
#     for i in range(M // 2):
#         if arr[s + i] != arr[e - i]:
#             break
#     else:
#         print(f'회문찾음! {arr[s:e+1]}') # 회문 조건 충족한 글자 보여주기

#-----------------------------------------
# # 모든 가능한 경우/ 회문이 있을수 있는 시작 위치
# for s in range(N - M + 1):
#     e = s + M - 1
#     for i in range(M // 2):
#         if arr[s + i] != arr[e - i]:
#             break
#     else:
#         ans = ''
#         for i in range(s, e+1):
#             ans += arr[i]
#         break
# print(ans)
#------------------------------------------
def find_palindrome(arr, N, M):
    # 모든 행에 대해서
    # 모든 가능한 경우/ 회문이 있을수 있는 시작 위치
    for row in range(N):
        # N - M + 1 <= i 가 N - M 이상 넘어가게 되면 out of range 즉, index에러 뜬당
        for s in range(N - M +1): # 시작점
            e = s + M - 1 # 끝점
            for i in range(M // 2):
                if arr[row][s + i] != arr[row][e - i]: # arr[0][0+0] != arr[0][9-0]
                    break
            # if문과 else가 문단이 달라 궁금해서 같은 선상 아래 뒀더니
            # 20 13 돌릴때 글자 arr[0][4]와 arr[0][16]의 B가 겹치면서
            # 조건이 하나만 맞은 상태 인데(arr[0][5]와 arr[0][17] 부터는 안맞음)
            # 바로 else로 내려가 ans에 글자 추가하기 시작 그래서 회문이 아닌 문자열이 출력됨
            # 그래서 for 문 아래에다 입력(for 문 바로 아래에 else 가능한줄 몰랐음)

            # for 문과 else 문 같은 문단에 두면 조건(!=)이 안맞을때, 즉 (==) 조건이라서
            # break 한번도 안걸린거고, 회문인지 확인된후 else 로 내려가는것임.
            else:
                ans = ''
                for i in range(s, e+1):
                    ans += arr[row][i]
                return ans
        # 모든 열에 대해서
        for s in range(N - M + 1):
            e = s + M - 1
            for i in range(M // 2):
                if arr[s + i][row] != arr[e - i][row]: # arr[0+0][0] != arr[9-0][0]
                    break
            else:
                ans = ''
                for i in range(s, e +1):
                    ans += arr[i][row]
                return ans

for tc in range(1, int(input())+1):
    # N = 가로,세로 길이 / M = 회문의 길이
    N, M = list(map(int, input().split()))
    arr = [input() for _ in range(N)]

    ret = find_palindrome(arr, N, M)
    print(ret)