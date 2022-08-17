# 2단계 (함수 2번 호출) (그림 그리고 디버깅 하면서 보기.. 가장 빠름)
#출력하는 코드 1개만 남기고 테스트
#출력하는 코드 2개 남기고 테스트

def abc(x):
    # print('#', end=' ')
    if x==2:
        # print('#', end=' ')
        return
    # print('#', end=' ')
    for i in range(2):
        # print('#', end=' ')
        abc(x+1)
        # print('#', end=' ')
    #print('#', end=' ')

abc(0)