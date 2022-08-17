
def abc(x):
    # print('#', end=' ')
    if x == 2:
        print('#', end=' ')
        return
    # print('#', end=' ')
    for i in range(2):
        # print('#', end=' ')
        abc(x + 1)
        # print('#', end=' ')
    # print('#', end=' ')


abc(0)
#-------------------------
# 1단계 (함수 1번 호출)
#
# 1234321
# 65433456
# 135797531
#
# 2단계 (함수 2번 호출) (그림리고 디버깅 하면서 보기.. 가장 빠름)
# #출력하는 코드 1개만 남기고 테스트
# #출력하는 코드 2개 남기고 테스트
#-------------------------
# 누적합 출력하기 !!!
# 2 8 12 13 21
# sum 변수를
# 1 전역변수로 놓고
# 2 매개변수 (지역변수)


# 1 전역변수 sum 활용하기
arr = [2, 6, 4, 1, 8]

sum = arr[0]


def abc(x):
    global sum
    print(sum)
    if x == 4:
        return
    sum += arr[x + 1]
    abc(x + 1)

abc(0)

# 2 매개변수 sum 이용
arr = [2, 6, 4, 1, 8]

def abc(x, sum):
    print(sum)
    if x == 4:
        return
    abc(x + 1, sum + arr[x + 1])


abc(0, arr[0])