# Selection_sort.py
# 완전 탐색
# 최선의 경우는 한번에 찾을때
# 최악의 경우는 원하는 수를 못찾을때
# 값이 하나도 없는것을 알고 처리할때
# 시간복잡도는 최악의 경우를 가정.

arr = [3, 6, 7, 1, 5, 4]

n = len(arr)

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=",")
    print()
print()
