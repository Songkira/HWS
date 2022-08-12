# 염기서열
p = "CATTCCCTGCGCCGC"
t = "ATTTGTGCATGTTTGAGCTCATTCCCTGCGCCGCTTTACGTACGAGAAACTGAACGTACATTCCCTGCGCCGC"

# 구간합이랑 원리적으로 똑같음.
n, m = len(t), len(p)

i = j = 0
# while i < n and j < m: # 처음 일치하는 경우 하나만 찾으면 종료됨.
#     if p[j] == t[i]: # 일치한 경우
#         i, j = i+1, j+1
#     else:           # 불일치한 경우
#         i = i - j + 1
#         j = 0
# if j == m:
#     print(t[i-m:i]) # 19 CATTCCCTGCGCCG
# ----------------------------------
# while i < n: # 여러개 찾을 경우
#     if p[j] == t[i]: # 일치한 경우
#         i, j = i+1, j+1
#         if j == m:
#             print(i - m,t[i - m:i])
#             j = 0
#     else:           # 불일치한 경우
#         i = i - j + 1
#         j = 0
# 19 CATTCCCTGCGCCGC
# 58 CATTCCCTGCGCCGC
#----------------------------------------
while i < n: # 여러개 찾을 경우 / 일치, 불일치 위아래 코드 순서 바꾼경우
    if p[j] != t[i]: # 불일치한 경우
        i = i - j
        j = -1
    else:           # 일치한 경우
        i, j = i + 1, j + 1
        if j == m:
            print(i - m, t[i - m:i])
            j = 0
#----------------------------
# 텍스트에서 패턴이 존재할 수 있는 모든 시작 위치
# for i in range(n - m +1): # 0 ~ n-m
#     # i = 매칭할 텍스트의 시작위치
#     for j in range(m):
#         if p[j] != t[i + j]:
#             break
#     else:
#         print(i, t[i:i + j]) # 19 CATTCCCTGCGCCG