1. 숫자의 입력과 출력
입력 받은 데이터를 숫자로 변환하고 덧셈해서 출력하는 프로그램을 작성하시오.
(힌트 : input() 함수를 활용하여 데이터를 입력받을 수 있다.) 

x, y = map(int,input('숫자 입력 :').split())
plus = x+y
print(plus)


2. Dictionary를 활용하여 평균 구하기
좋아하는 점심메뉴를 이용하여 key는 메뉴, value는 가격인 dictionary를 만들고,
점심메뉴의 평균 값을 출력하시오

lunch = {'칼국수':9000, '제육볶음':8000, '순두부':7000, '짜장면':6500, '닭갈비':8500}

lunch_price = sum(lunch.values())/len(lunch.values())

print(int(lunch_price))