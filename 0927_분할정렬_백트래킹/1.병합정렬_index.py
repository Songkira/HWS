def merge_sort(lo, hi):     # 구간 정보 (시작, 끝)
    if lo == hi: return     # 시작과 끝이 같으면
    mid = (lo + hi) >> 1    # 나누기 2 == // 2
    merge_sort(lo, mid)
    merge_sort(mid + 1, hi)
    # 병합
    # lo, hi는 건드리면 안되니까 tmp에서 쓸 임시변수 생성
    i, j, k = lo, mid + 1, lo

    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]; i += 1; k += 1
        else:
            tmp[k] = arr[j]; j += 1; k += 1

    while i <= mid:    # i가 아직 mid를 벗어나지 못했으면
        tmp[k] = arr[i]; i += 1; k += 1
    while j <= hi:
        tmp[k] = arr[j]; j += 1; k += 1

    for i in range(lo, hi + 1):
        arr[i] = tmp[i]

arr = [69, 30, 10, 2, 16, 8, 32, 21]
tmp = [0] * len(arr)
merge_sort(0, len(arr) - 1)
print(tmp)
print(arr)

