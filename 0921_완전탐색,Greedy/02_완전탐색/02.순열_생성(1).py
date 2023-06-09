# -------------------------
# 교환을 통한 순열 생성
# -------------------------
arr = [10, 20, 30]

def perm(k, n):

    if k == n:
        print(arr)
        return

    for i in range(k, n):
        arr[i], arr[k] = arr[k], arr[i]
        perm(k + 1, n)
        arr[i], arr[k] = arr[k], arr[i]

perm(0, len(arr))
