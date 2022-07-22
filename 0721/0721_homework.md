1. 위치 인자와 키워드 인자
다음과 같이 함수가 선언되어 있을 때, 보기 (1)~(4) 중에서 실행 시
오류가 발생하는 코드를 고르시오.

def ssafy(name, location='서울’):
print(f'{name}의 지역은 {location}입니다.')
# (1)
ssafy(＇가흔')
# (2)
ssafy(location=＇부울경', name=＇승현')
# (3)
ssafy(＇지우', location='서울')
# (4)
ssafy(name=＇승호’, ‘광주')

답 : (4) # 

2. 가변 인자 리스트
가변 인자 리스트를 사용하여, 개수가 정해지지 않은 여러 정수들을 전달 받아
해당 정수들의 평균 값을 반환하는 my_avg 함수를 작성하시오

my_avg(77, 83, 95, 80, 70) # => 81.0

def my_avg(*args):
    result = 0
    for sum in args:
        result += sum
        result_avg = result / len(args)
    return result_av

3. 반환값
다음과 같이 함수를 선언하고 호출하였을 때, 변수 result에 저장된 값과
그 값이 나온 이유를 작성하시오.

def my_func(a, b):
c = a + b
print(c)

result = my_func(3, 7)

답 : None

함수 내에 print()를 쓰면 반환되지 않는다.
return 을 써야 반환된다. 
# 'my_fucn'은 반환 값이 없기때문에 result에 None이 저장된다.

4. 이름 공간(Namespace)
Python에서 변수를 찾을 때 접근하는 이름 공간을 순서대로 작성하시오.

1. Local scope(지역변수)


2. Enclosed scope(외부 함수의 지역변수)


3. Global scope(전역변수)


4. Built-in scope(내장형)

5. 매개변수와 인자, 그리고 반환
아래의 보기 (1) ~ (4) 중에서, 옳지 않은 것을 고르시오.
(1) 함수는 오직 하나의 객체만 반환할 수 있으므로
'return a, b＇와 같이 쓸 수 없다.
(2) 함수에서 return을 작성하지 않으면 None 값을 반환한다.
(3) 함수의 매개변수(parameter)는 함수를 선언할 때 설정한 값이며,
전달 인자(argument)는 함수를 호출할 때 넘겨주는 값이다.
(4) 가변 인자를 설정할 때는 함수 선언 시 매개변수 앞에 * 을 붙이고, 
이 때는 함수내에서 tuple로 처리 된다.

답 : (1)

6. 재귀 함수
재귀 함수를 사용했을 때 얻을 수 있는 장점과 단점을 반복문과 비교하여 작성하시오

1. 자기 자신을 호출하는 재귀함수는 알고리즘 구현시 많이 사용된다.
2. 코드가 더 직관적이고 이해하기 쉬운 경우가 있음. 
3. Python Tutor에 보면, 함수가 호출될 때마다 메모리 공간에 쌓이는 것을 볼 수 있다.
4. 이 경우, 메모리 스택이 넘치거나(Stack overflow) 프로그램 실행 속도가 늘어지는 단점이 생긴다.
5. 파이썬에서는 이를 방지하기 위해 1,000번이 넘어가게 되면 더이상 함수를 호출하지 않고, 종료된다.