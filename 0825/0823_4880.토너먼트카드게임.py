import sys; sys.stdin = open('4880.txt', 'r')
#1 3
#2 5
#3 1
# 문제의 크기를 이분화 해서 찾을수 있음 (중간값을 찾아서 나누는건가?)
# arr = [55, 78, 12, 20, 45, 7, 42]
#
# def find_mid(s, e):
#     print(s, e)
#     if s == e:
#         return
#     else:
#         mid = (s + e) // 2
#         l = find_mid(s, mid)
#         r = find_mid(mid + 1, e)
#
# find_mid(0, len(arr)-1)
# --------------------------------------------
# 0 6
# 0 3
# 0 1
# 0 0
# 1 1
# 2 3
# 2 2
# 3 3
# 4 6
# 4 5
# 4 4
# 5 5
# 6 6
# ----------------------------------------

# def find_mid(s, e):
#
#     if s == e:
#         return arr[s]
#     else:
#         mid = (s + e) // 2
#         l = find_mid(s, mid)
#         r = find_mid(mid + 1, e)
#
#         if l < r: return l
#         return r
#
# print(find_mid(0, len(arr)-1)) # 시작과 끝 인덱스

# -----------------------------------
# 토너먼트 카드게임
# 1: 가위, 2: 바위, 3: 보
#          1, 2, 3
lose = [0, 2, 3, 1] # 지는 경우

def play(s, e): # 승자를 return 해주는 함수
    if s == e:
        return s
    else:
        mid = (s + e) // 2
        lwin = play(s, mid)
        rwin = play(mid + 1, e)
        if lose[arr[lwin]] == arr[rwin]: # 왼쪽이 진거
            return rwin
        return lwin # 비겼을 경우

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = play(0, len(arr) - 1)
    print(ans+1)
