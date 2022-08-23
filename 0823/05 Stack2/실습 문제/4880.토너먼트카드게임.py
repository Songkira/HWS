import sys; sys.stdin = open('4880.txt', 'r')
#1 3
#2 5
#3 1
# 문제의 크기를 이분화 해서 찾을수 있음 (중간값을 찾아서 나누는건가?)
arr = [55, 78, 12, 20, 45, 7, 42]

def find_mid(s, e):
    if s == e:
        return arr[s]
    else:
        mid = (s + e) // 2
        l = find_min(s, mid)
        r = find_min(mid + 1, e)

        if l < r: return l
        return r

print(find_mid(0, len(arr)-1)) # 시작과 끝 인덱스