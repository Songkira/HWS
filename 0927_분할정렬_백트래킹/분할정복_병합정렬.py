# 김덕호 코드

def merge_sort(lst, s, e):
    if s + 1 == e:
        return [lst[s]]
    m = (s + e) // 2
    l = merge_sort(lst, s, m)
    r = merge_sort(lst, m, e)

    res = []
    lenL, lenR = len(l), len(r)
    idxL, idxR = 0, 0
    while idxL < lenL and idxR < lenR:
        if l[idxL] <= r[idxR]:
            res.append(l[idxL])
            idxL += 1
            continue
        res.append(r[idxR])
        idxR += 1

    if idxL < lenL:
        global cnt
        cnt += 1
        for i in range(idxL, lenL):
            res.append(l[i])
    if idxR < lenR:
        for i in range(idxR, lenR):
            res.append(r[i])
    return res


for case in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    sortedNums = merge_sort(nums, 0, N)
    print(f'#{case}', sortedNums[N // 2], cnt)

# ------------------------------------------

