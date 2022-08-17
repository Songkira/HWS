import sys; sys.stdin = open('2005.txt', 'r')

# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
for tc in range(1, int(input())+1):
    N = int(input())

    result = [] # 서브리스트를 집어넣을 큰 리스트 생성
    for i in range(N):
        paskal = [] # 서브리스트 생성
        for j in range(i+1):
            if j == 0 or j == i:
                paskal.append(1)
            else:
                paskal.append(result[i-1][j-1] + result[i-1][j])
        result.append(paskal)

    print(f'#{tc}')
    for i in result:
        print(*i)


    # 1. 각 줄 번호와 동일한 갯수의 숫자 출력
    # 2. append?