arr = [55, 7, 78, 12, 42]
# 최대값/최소
#---------------------------------------
# 첫번째 값을 최대값으로 가정
max_val = arr[0] # 리스트 안에서 찾을때

for val in arr:   # 첫번째 값부터 읽어서 비교해도 됨
    if max_val < val:
        max_val = val
#---------------------------------------
# 입력값이 범위가 양의 정수라면
# 초기값으로 0(특정값)으로 설정
# 주의할 것은 초기값을 어떤걸로 정하는냐...
max_val = 0 # 임의의 값, 때마다 나오는 값에서, 중간계산 결과 중에서

for val in arr:   # max_val 첫번째 값으로 무조건 갱신
    if max_val < val:
        max_val = val
print(max_val)
#---------------------------------------
# 최대/최소의 인덱스를 찾기
max_idx = 0  # 첫번째 인덱스를 최대값의 위치로 가정

for i in range(1, len(arr)):
    if arr[max_idx] < arr[i]:
        max_idx = i

print(max_idx, arr[max_idx])
#---------------------------------------

max_idx = min_idx = 0  # 첫번째 인덱스를 최대/최소의 위치로 가정

for i in range(1, len(arr)):
    if arr[max_idx] < arr[i]:
        max_idx = i
    if arr[min_idx] > arr[i]:
        min_idx = i


print(arr[max_idx], arr[min_idx])
# -------------------------------------
arr = [55, 7, 78, 7, 12, 7, 42]

# 최소값이 여러개라면 가장 뒤에 나오는 값의 위치

min_idx = 0  # 첫번째 인덱스를 최대/최소의 위치로 가정

for i in range(1, len(arr)):
    if arr[min_idx] >= arr[i]:
        min_idx = i

print(min_idx)
# -------------------------------------
# 최소값과 등장 회수를 찾기

min_idx = 0  # 첫번째 인덱스를 최대/최소의 위치로 가정
cnt = 0
for i in range(1, len(arr)):
    if arr[min_idx] > arr[i]: # 새로운 최소값
        min_idx = i
        cnt = 1
    elif arr[min_idx] == arr[i]: # 같은 값
        cnt += 1

print(arr[min_idx], cnt)






