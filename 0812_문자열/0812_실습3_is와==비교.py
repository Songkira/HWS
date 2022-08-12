
# # is, == 연산자 비교 결과
s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'

#
print(f's1 == s2 :', s1 == s2) # True
print(f's1 is s2 :', s1 is s2) # True
print(id(s1), id(s2)) # 같은 객체를 가지고 있음.
print(f's1 == s3 :', s1 == s3) # False
print(f's1 is s3 :', s1 is s3) # False
print(id(s1), id(s3))
print(f's1 == s4 :', s1 == s4) # True
print(f's1 is s4 :', s1 is s4) # True
print(id(s1), id(s4))
print(f's1 == s5 :', s1 == s5) # True # 같은 내용(값)이냐?
print(f's1 is s5 :', s1 is s5) # False # 같은 객체냐?
print(id(s1), id(s5))
#
# print('abc' == 'abc') # True
# print('abc' > 'abx') # False 'abx'가 'abc'보다 순서가 더 빠르냐
# print('abc' > 'ab') # True 'ab'가 'abc'보다 순서가 더 빠르냐