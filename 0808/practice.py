# input() = > 문자열
# input().split() ==> 문자열 리스트
# map(int, input().split()) => 정수들을 저장하는 맵객체
# list(map(int, input().split())) ==> 정수들의 리스트

a, b = map(int, input().split()) # map unpack
print(a, b)