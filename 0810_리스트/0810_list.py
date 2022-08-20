# N = int(input())
# # arr = list(map(int, input().split())) # 일단 한 행을 읽는 것
# # arr = [list(map(int, input().split())) for _ in range(N)]# 한 행을 N번만큼 반복해서 읽는 것 # 공백으로 나눔

# # 그냥 읽어도 iterable이면(ex. 123) 나눠지니까 split 없이 사용
# arr = [list(map(int, input())) for _ in range(N)]# 한 행을 N번만큼 반복해서 읽는 것

# # 개별의 원소 접근
# for i in range(N): # 행 접근 /방향 : 아래
#     for j in range(N): # 열 접근 방향: 오른쪽
#         print(arr[i][j], end=' ')
#     print()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 열, 행 순서는 그때 그때 다름. 문제 잘 읽어보기
for i in range(N): # 행 접근 /방향 : 아래
    for j in range(M): # 열 접근 방향: 오른쪽
        print(arr[i][j], end=' ')
    print()

# 각 행에 대한 열의 크기가 모두 같다 의 경우 활용하시길...
# for i in range(len(arr)): # 행 접근 /방향 : 아래 /N = len(arr) 배열의 이름
#     # 2차원에서 인덱스를 하나만 쓰면 그 행을 나타냄.
#     for j in range(len(arr[0])): # 열 접근 방향: 오른쪽 / 행에 대한 정보를 주면 몇개의 열을 갖고있는지 알아내는 역할.
#         print(arr[i][j], end=' ')
#     print()
