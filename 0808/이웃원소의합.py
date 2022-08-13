import sys; sys.stdin=open('input.txt', 'r')
# 인접한 두 원소의 합이 최대인 경우

T = int(input())

for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    # 까닥하면 인덱스 에러 나니까 조심.
    # 굳이 중첩반복문 안만들어도 정수의 개수에서 -1을 하면
    # 마지막 인덱스(arr[-1]) 까지 i가 안가고 arr[-2]까지만 가게됨
    #  그러면 [i+1]을 수식에 포함 가능.
    max = 0
    for i in range(n-1):
        if max < arr[i]+arr[i+1]:
            max = arr[i] + arr[i+1]
    print(f'#{tc+1}', max)


