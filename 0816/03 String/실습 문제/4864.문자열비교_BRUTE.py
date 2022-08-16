import sys; sys.stdin = open("4864.txt", "r")

T = int(input())

for tc in range(1, T +1):
    str1 = input() # 찾을 문자열
    str2 = input() # 비교할 전체 문자열
    M = len(str1)
    N = len(str2)

    i = 0 # str2의 인덱스
    j = 0 # str1의 인덱스
    while j < M and i < N :
        if str2[i] != str1[j]: # 불일치할 경우
            i = i - j # 원래 시작 위치로 돌리기
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')