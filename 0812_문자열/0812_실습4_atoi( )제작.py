# int()와 같은 atoi()함수 만들기
# def atoi(a): # atoi( ): int( )와 같은 구조로 돌아가는 함수, 자세히 들어가면 조금 다르지만
#     i = 0
#     for x in a:
#         i = i *10 + ord(x) - ord('0') # ord(): 문자 0 ~ 9 에 해당하는
#     return i                          # 0 ~ 9 숫자 값으로 바꾸시오
#
# s = '123'
# a = atoi(s) # 123 이란 정수로 바꿔라
# print(a + 1)

# ---------------------------------------
#  str() 함수 사용않고, itoa()를 구현해 봅시다.
# 양의 정수를 입력받아 문자열로 반환하는 함수
# 내가 짜는 중...
# def itoa(num):
#     while num != 0: # 무한반복 활용잘하자..
#         # print(num % 10, end=' ')
#         num = num // 10
#     # chr(num) 하면 1234가 나와야함.
#     i = ''
#     for x in num:
#         i = i * 10 + chr(ord(x)) - chr(ord('0'))
#     return i
#
# val = itoa(1234)
# print(type(val), val) # str, 1234
# # 음수를 변환할때 고려해야 할 것은?

# ------------------------------------
# 교수님 작성..
def itoa(num):
    while num != 0:
        digit = num % 10
        print(digit, end='') # 4 3 2 1
        # print(chr(ord('0') + digit), end=' ') # 4 3 2 1
        num = num // 10


val = itoa(1234)
print(type(val), val)  # str, 1234