import sys; sys.stdin = open('4873.txt', 'r')

for tc in range(1, int(input()) + 1):
    word = list(input())
    N = len(word)
    top = -1
    # 새로운 리스트 만들기
    new = []
    # new += word[0]
    # middle?

    for i in range(N):
        if word[i] not in new:
            new.append(word[i])
        else:
            if new[top] == word[i]:
                new.pop()
            else:
                new.append(word[i])
    ans = len(new)
    print(f'#{tc} {ans}')
