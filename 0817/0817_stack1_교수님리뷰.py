# 저장공간 생성
S = [0] * 10
top = -1        # push/ pop에 사용되는 인덱스
                # 마지막에 저장된 자료의 위치
                # 비어있으니까 + 가리킬게 없으니까 -1로 지정해둔 것.
def push(item):
    global top
    # full 상태를 체크 해야됨 # 인덱스를 벗어날수 도 있으므로
    top += 1
    S[top] = item

# def pop():
#     global top
#     # val = S[top]
#     top -= 1
#     return S[top -1]

def pop():
    global top
    # empty 상태를 체크
    val = S[top]
    top -= 1
    return val