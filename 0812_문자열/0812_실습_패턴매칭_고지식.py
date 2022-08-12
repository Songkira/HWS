p = 'is' # 찾을 패턴
t = 'This is a book' # 전체 텍스트
M = len(p) # 찾을 패턴의 길이
N = len(t) #  전체 텍스트의 길이

def BruteForce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]: # 불일치 할 경우
            i = i - j # 원래 시작 위치로 돌리기 위해서
            j = -1
        i = i + 1
        j = j + 1
    if j == M : return i - M # 검색 성공
    else: return -1 # 검색 실패

    # 일치하는 경우
    # i, j 사이좋게 증가

    # 불일치할 경우
    # i= 이전 시작 위치 +1
    # j = 0 # 처음으로 돌아감