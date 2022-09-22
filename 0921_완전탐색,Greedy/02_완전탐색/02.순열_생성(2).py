# -------------------------
# used[] 배열을 활용해서 순열 생성
# order[] : 실제 요소를 순서대로 저장
# -------------------------
arr = [10, 20, 30]
used = [0] * len(arr)
order = [0] * len(arr)

def perm(k, n):
    if k == n:
        print(order)
        return

    for i in range(n):
        if used[i]: continue

        used[i] = 1
        order[k] = arr[i]

        perm(k + 1, n)

        used[i] = 0

perm(0, len(arr))

# def perm(k, n, used):   # used : 정수로 담아서
#     if k == n:
#         print(order)
#         return
#
#     for i in range(n):
#         if used & (1 << i): continue
#         order[k] = arr[i]
#         perm(k + 1, n, used | (1 << i))
#
# perm(0, len(arr), 0)
