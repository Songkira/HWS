import sys; sys.stdin = open('1216.txt')

def find_palindrome(arr, N, M):
    for row in range(N):
        for s in range(N - M +1):
            e = s + M - 1
            for i in range(M//2):
                if arr[row][s + i] != arr[row][e - i]:
                    break
            else:
                return M

        for s in range(N - M +1):
            e = s + M -1
            for i in range(M//2):
                if arr[s+i][row] != arr[e -i][row]:
                    break
            else:
                return M
    return 0

for tc in range(1, 11):
    tc_num = input()
    arr = [input() for _ in range(100)]

    ans = 0
    for M in range(100, 1, -1): # 100 ~ 2까지
        ans = find_palindrome(arr, 100, M)
        if ans != 0 :
            break
    print(f'#{tc} {ans}')