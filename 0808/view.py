for test in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
 
    for i in range(2, N - 2):
        max = arr[i-2]
        if max < arr[i-1]:
            max = arr[i-1]
        if max < arr[i+1]:
            max = arr[i+1]
        if max < arr[i+2]:
            max = arr[i+2]
 
        if arr[i] > max:
            cnt = cnt+(arr[i]-max)
 
    print(f'#{test + 1} {cnt}')