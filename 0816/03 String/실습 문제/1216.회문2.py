import sys; sys.stdin = open('1216.txt')

def find_palindrome(arr, N, M):


for tc in range(1, 11):
    ic_num = input()
    arr = [input() for _ in range(100)]

    ans = 0
    for M in range(100, 1, -1): # 100 ~ 2까지
        ret = find_palindrome(arr, 100, M)
        if ans != 0 :
            break
    print(ans)