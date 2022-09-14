

H = [0] * 100
hsize = 0   # 초기값은 0

def push(item):
    global hsize
    # full => hsize == 99
    hsize += 1
    H[hsize] = item

    c = hsize
    p = hsize // 2
    while p and H[p] < H[c]:
        H[p], H[c] = H[c], H[p]
        c = p
        p = c // 2

def pop():
    global hsize
    # empty ==> (hsize == 0)
    ret = H[1]
    H[1] = H[hsize]
    hsize -= 1

    p, c = 1, 2  # c: 왼쪽 자식

    while c <= hsize:
        if c + 1 <= hsize and H[c] < H[c + 1]:
            c += 1
        if H[p] >= H[c]:
            break
        H[p], H[c] = H[c], H[p]
        p = c
        c = p * 2

    return ret

def empty():
    return hsize == 0

# ===========================================
data = [69, 10, 30, 2, 16, 8, 31, 22]

for val in data:
    push(val)

N = 10
while hsize:
    print(pop(), end=' ')