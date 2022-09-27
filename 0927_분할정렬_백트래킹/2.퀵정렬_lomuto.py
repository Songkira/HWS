# Lomuto_Algorithm
# 코드가 간결하다고 좋은건 아님

def quick_lomuto(lo, hi):
    # lo, hi를 보고 계속 갈지 말지 판단
    if lo >= hi: return # 진행할 필요가 없으니 종료

    # partition
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= arr[hi]: # arr[hi] = 피봇
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[i], arr[hi] = arr[hi], arr[i]

    # 분할 위치는 pivot이 있는  i
    quick_lomuto(lo, i - 1)
    quick_lomuto(i + 1, hi)


arr = [69, 30, 10, 2, 16, 8, 32, 21]
# 같은 값이 여러개이면?
# arr = [1, 1, 1, 1, 0, 0, 0, 0, 0]
quick_lomuto(0, len(arr) - 1)
print(arr)
