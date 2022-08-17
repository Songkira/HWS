# 초심자의 회문검사
T = int(input())

# for tc in range(T):
#     palindrome = input()
#
#     if palindrome == palindrome[::-1]:
#         print(f'#{tc+1}', 1)
#     else:
#         print(f'#{tc+1}', 0)

for tc in range(T):
    arr = input()
    N = len(arr)
    # ans = 1
    for i in range(N//2):
        if arr[i] != arr[N -1 -i]:
           ans = 0
           break
    else:
        ans = 1
    print(f'#{tc+1}', ans)
#----------------------------------------