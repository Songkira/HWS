# strlen() 함수 구현해보기
# mystr = 'algorithm'
# # 1. 파이썬의 내장된 기능
# print(mystr[::-1])
#
# # 2. 새로운 공간에 저장, 뒤에서 읽어서 붙이기
# rev_str = ''
# for i in range(len(mystr) - 1, -1, -1):
#     rev_str += mystr[i]
# print(rev_str)

# 3. 교환을 통해서 뒤집기
# arr = input()
# N = len(arr)
# ans = 1
# for i in range(N // 2):
#     if arr[i] != arr[N - 1 - i]:
#         ans = 0
#         break

# s1 = 'abc'
# s2 = 'abc'
# s3 = 'def'
# s4 = s1
# s5 = s1[:2] + 'c'
# print(s1 is s2, s1 == s2)
# print(s1 is s3, s1 == s3)
# print(s1 is s4, s1 == s4)
# print(s1 is s5, s1 == s5)

# print('abc' == 'abc')
# print('abc' > 'abx')
# print('abc' > 'ab')


def itoa(num):
    while num != 0:
        digit = num % 10
        print(digit, end= ' ')
        # print(chr(ord('0') + digit), end=' ')
        num = num // 10

val = itoa(1234)
print(type(val), val) # str, '1234'