# 파이썬에서 우선순위큐를 사용
# 1. PriorityQueue
# from queue import PriorityQueue
# data = [69, 10, 30, 2, 16, 8, 31, 22]
#
# Q = PriorityQueue()
# for val in data:
#     Q.put(val)
# while not Q.empty():
#     print(Q.get(), end=' ')

# 2. heapq
from heapq import heappush, heappop, heapify
data = [69, 10, 30, 2, 16, 8, 31, 22]

heapify(data)
while data:
    print(heappop(data))

# HEAP = []
# for val in data:
#     heappush(HEAP, val)
#
# while HEAP:
#     print(heappop(HEAP))
