# 힙
SIZE = 100
H = [0] * SIZE
last = 0            # 마지막 노드의 번호 / 전체 노드 수

# def init(): # 힙 초기화
#     global last
#     last = 0

def push(item):
    # full 상태를 체크: last == SIZE - 1
    # 마지막 노드의 다음 위치에 저장
    global last
    last += 1
    H[last] = item
    # 여기까지가 완전 이진트리 구조 설정

    # 부모-자식 간의 대소 관계를 체크
    c, p = last, last//2

    while p > 0 and H[c] > H[p]:    # p > 0 : 부모가 있는지 확인
        H[c], H[p] = H[p], H[c]
        # c, p = p, c//2
        c = p
        p = c // 2
    # else:                         # 부모가 없든가, 대소관계가 없든가
    #     break

def pop():
    # empty check: last == 0
    global last
    ret = H[1]
    H[1] = H[last]    # 마지막 노드를 루트에 복사
    last -= 1         # 마지막 노드 삭제

    p, c = 1, 2       # 엄밀히 말하면 왼쪽 자식

    # while True:
    #     # 왼쪽 자식이 있는지 체크, 마지막 노드 번호보다 큰 값인지 확인
    #     if c > last: break
    #     # 왼쪽 자식이 없으면, 오른쪽 자식 있는지 체크
    #     # 오른쪽 자식이 더 크면
    #     if c + 1 > last and H[c] < H[c + 1]:
    #         c += 1
    #     if H[c] > H[p]:
    #         H[c], H[p] = H[p], H[c]
    #         p = c
    #         c = p * 2
    #     else:
    #         break
    while c <= last: # 왼쪽 자식이 있는지 체크, 마지막 노드 번호보다 큰 값인지 확인
        # 오른쪽 자식 있는지 체크, 오른쪽 자식이 더 크면
        if c + 1 <= last and H[c] < H[c + 1]:
            c += 1
        if H[c] <= H[p]: break

        H[c], H[p] = H[p], H[c]
        p = c
        c = p * 2

    return ret


data = [69, 10, 30, 2, 16, 8, 31, 22]

for val in data:
    push(val)

while last > 0:
    print(pop(), end=' ')