# Hoare_Algorithm

def quick_hoare(lo, hi):
    # lo, hi를 보고 계속 갈지 말지 판단
    if lo >= hi: return # 진행할 필요가 없으니 종료

    # partition
    i, j = lo, hi
    p = arr[lo]     # pivot
    while i <= j:
        # i <= hi : 경계를 벗어나지 않게
        while i <= hi and p >= arr[i]:
            i += 1
        # j는 항상 pivot에서 멈출것이기때문에 범위설정 안해도 됨.
        while p < arr[j]:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[lo], arr[j] = arr[j], arr[lo]
    # 분할 위치는 pivot이 있는  j
    quick_hoare(lo, j - 1)
    quick_hoare(j + 1, hi)


# # arr = [69, 30, 10, 2, 16, 8, 32, 21]
# # 같은 값이 여러개이면?
# arr = [1, 1, 1, 1, 0, 0, 0, 0, 0]
# quick_hoare(0, len(arr) - 1)
# print(arr)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_hoare(0, len(arr) - 1)
    print(f'#{tc} {arr[N//2]}')