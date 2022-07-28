1. Type Class
Python은 객체 지향 프로그래밍 언어이다. Python에서 기본적으로 정의되어 있는 클래스를 최소 5가지 이상 작성하시오.
```
__init__, __del__, __str__, __repr__, __len__, __lt__, __le__
```

2. Magic Method
아래에 제시된 매직 메서드들이 각각 어떠한 역할을 하는지 간단하게 작성하시오.

```
__init__, __del__, __str__, __repr__
```

```
__init__ : 어떤 클래스의 인스턴스(객체)가 생성될때 인터프리터에 의해 자동으로 호출되는 메소드
__del__ : 객체가 소멸되기 직전에 호출되는 메소드
__str__ : 해당 객체의 출력형태를 지정
        입력받은 객체의 문자열 버전을 반환
__repr__: 어떤 객체의 '출력될 수 있는 표현'을 문자열의 형태로 반환
```

3. Instance Method
.sort() 와 같이 문자열, 리스트, 딕셔너리 등을 조작 할 때 사용하였던 것들은 클래스에 정의된 메서드들이었다. 이처럼 문자열, 리스트, 딕셔너리 등을 조작하는 메서드를 최소 3가지 이상 그 역할과 함께 작성하시오
```
.add(), .update(), .count(), .strip(), .remove()
```

4. 오류의 종류
아래에 제시된 오류들이 각각 어떠한 경우에 발생하는지 간단하게 작성하시오.
ZeroDivisionError, NameError, TypeError, IndexError,
KeyError, ModuleNotFoundError, ImportError
```
ZeroDivisionError : 0으로 나눌때 발생
NameError : namespace 상에 이름이 없는 경우 
TypeError : 타입 불일치, argument 누락 및 개수 초과
KeyError : 해당 키가 존재하지 않는 경우
IndexError : 인덱스가 존재하지 않거나 범위를 벗어나는 경우
ModuleNotFoundError : 모듈이 존재하지 않음
ImportError : 모듈은 있으나 존재하지 않는 클래스/함수를 가지고 올 경우
```