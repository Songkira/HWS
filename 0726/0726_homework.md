1. Built-in 함수와 메서드
sorted()와 .sort()의 차이점을 코드의 실행 결과를 활용하여 설명하시오
```
 .sort()는 내장함수 sorted()원본을 변형시키고 None를 리턴시킨다
```
2. .extend()와 .append()
.extend()와 .append()의 차이점을 코드의 실행 결과를 활용하여 설명하시오
```
 .append()는 리스트에 값을 추가할 수 있습니다.
 a[len(a):] = [x]와 동일
  
cafe = ['starbucks', 'tomntoms', 'hollys']
print(cafe)
# ['starbucks', 'tomntoms', 'hollys']

cafe.append('banapresso')
print(cafe)
#
['starbucks', 'tomntoms', 'hollys', 'banapresso']
```
```
 .extend()는 iterable(list,range,tuple,string)에 값을 붙일 수 있습니다.
 a[len(a):] = iterable 와 동일

cafe.extend(['wcafe', '빽다방'])
print(cafe)
# ['starbucks', 'tomntoms', 'hollys', 'banapresso', 'wcafe', '빽다방']

cafe.extend('ediya')
print(cafe)
#['starbucks', 'tomntoms', 'hollys', 'banapresso', 'wcafe', '빽다방','e', 'd', 'i', 'y', 'a']

3. 복사가 잘 된 건가?
아래의 코드를 실행 하였을 때, 변수 a와 b에 담긴 list의 요소가 같은지 혹은 다른지 여부를 판단하고 그 이유를 작성하시오.
```
a = [1, 2, 3, 4, 5]
b = a
a[2] = 5
print(a)
print(b)
```
 대입연산자(=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사
 즉, 두개 중 하나만 변경 되어도 나머지 하나도 동일하게 수정되는 현상이 나타남


