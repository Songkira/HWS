from _collections import deque
# import 사용 금지면 당연히 쓰면 안되는 거임.

q = []

q.append(10)
q.append(20)
q.append(30)
#
# print(q.pop(0))
# print(q.pop(0))
# print(q.pop(0))
# # 10
# 20
# 30

print(q.popleft())
print(q.popleft())
print(q.popleft())
# 이걸 쓰면 속도문제가 해결되긴함