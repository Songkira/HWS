import sys; sys.stdin=open('input (1).txt', 'r')

# 오름차순 정렬 해야하는 문제
T = int(input())

for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    # 버블정렬 사용하면? 버블정렬은 끝부터 차례로 정렬한다.
    # 시간복잡도는 O(n^2)
    for i in range(n-1,0,-1): # 범위의 끝 위치부터 시작해서 1번 인덱스까지
    # 왜 1번 인덱스냐? 항상 2자리가 서로 비교해야 하므로 0번 인덱스까지 가면 인덱스 에러발생
        for j in range(0, i):# range할수록 i가 작아지므로 비교할 범위도 줄어든다.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # 이대로 print 하면 []형식으로 뜨니까, 언팩(*)사용.
    print(f'#{tc+1}', *arr)
