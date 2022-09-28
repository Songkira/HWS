from collections import deque
def merge_sort(lst):
    global cnt
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    l = deque(merge_sort(lst[:mid]))
    r = deque(merge_sort(lst[mid:]))
    if l[-1] > r[-1]:
        cnt += 1

    # l, r은 정렬된 리스트
    ret = []
    while l and r:
        if l[0] <= r[0]:
            ret.append(l.popleft())
        else:
            ret.append(r.popleft())
    if l: ret.extend(l)
    if r: ret.extend(r)

    return ret  # 병합

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    lst = list(merge_sort(arr))
    print(f'#{tc} {lst[N//2]} {cnt}')