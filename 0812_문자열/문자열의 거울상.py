# 문자열의 거울상
T = int(input())

for tc in range(T):
    palindrome = list(input())
    L = len(palindrome)

    for i in range(L // 2):
        palindrome[i], palindrome[L -1 -i] = palindrome[L -1 -i], palindrome[i]
    # print(palindrome)
    # palindrome 뒤집고 나서
    # 문자 바꾸기 진행
    for j in range(len(palindrome)):
        if palindrome[j] == 'b':
            palindrome[j] = 'd'

        elif palindrome[j] == 'p':
            palindrome[j] = 'q'

        elif palindrome[j] == 'd':
            palindrome[j] = 'b'

        elif palindrome[j] == 'q':
            palindrome[j] = 'p'

    print(f'#{tc+1}', ''.join(palindrome))

# -------------------------------------------