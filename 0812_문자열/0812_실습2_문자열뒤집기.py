# # 문자열 뒤집기
# # 1. 자기 문자열에서 뒤집기
mystr = 'algorithm'
# print(mystr[::-1]) # mhtirogla

# # arr = list(mystr) # list 는 reverse 가있긴함
# # print(arr) # ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm']
#
# # 2. 새로운 공간에 저장, 뒤에서 읽어서 붙이기
# rev_str = ''
# for i in range(len(mystr) -1, -1, -1):
#     rev_str += mystr[i]
#
# print(rev_str) # mhtirogla

# 3. 교환을 통해서 뒤집기 / 회문 검사때 사용
arr = list(mystr)
N = len(arr)
for i in range(N // 2):
    # i <==> N - 1 - i
    arr[i], arr[N -1 -i] = arr[N - 1 - i], arr[i]
print(arr) # ['m', 'h', 't', 'i', 'r', 'o', 'g', 'l', 'a']
print(''.join(arr)) # mhtirogla

# -------------------------------------------------------------