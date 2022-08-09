# input() = > 문자열
# input().split() ==> 문자열 리스트
# map(int, input().split()) => 정수들을 저장하는 맵객체
# list(map(int, input().split())) ==> 정수들의 리스트

# a, b = map(int, input().split()) # map unpack
# print(a, b)

import sys # 들어오는 데이터 받기

# 키보드로 입력할 내용을 파일에 미리 저장해놓고
# 파일에서 읽어온다.
sys.stdin = open('input.txt')

a, b = map(int, input().split()) # map unpack
print(a, b)