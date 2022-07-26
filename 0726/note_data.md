### 제어문 & 함수 복습


```python
# 반복문의 break, continue
for i in range(4):
    
    if i % 2 == 0: 
        continue
        
    for j in range(4):
        if j % 2 == 1:
            continue
    
        print(i, j)
    
```


```python
for i in range(4):
        
    for j in range(4):
        if i + j > 2:
            break
    
        print(i, j)
    
```

> 
> 함수 스코프


```python
# 전역 스코프(global scope)
a = 10 # 전역 변수(global)

def func(b):
    # 지역 스코프(local scope)
    c = 20 # 지역 변수(local variable)
    print(a)
    print(b)

func(a)
```

### 자료형


```python
# sequence
# iterable
# imutable / mutable
# 문자열 - 순서가 있음(sequence), iterable, immutable
# 리스트 - sequence, iterable, mutable
# 튜플 - sequence, iterable, immutable
# 셋 - non-sequence, iterable, mutable
# 딕셔너리 - non-sequence, iterable, mutable
    #      { key : value} => key: immutable, value: 모두 가능
```


```python
# 문자열, 리스트, 셋, 딕셔너리
# 1. 생성
# 2. 조회/탐색
# 3. 수정/추가/삭제
# 4. 정렬

# '-'.join('abcde')
# '-'.join(['aa','bb','xx'])
# '-'.join({'aaa','bbb','xxx'}) -> set 은 순서 x

# '-'.join([1, 2, 3]) #-> 문자열이 아니라서 iternable이지만 안됨
# TypeError: sequence item 0: expected str instance, int found
# '-'.join(map(str, [1, 2, 3])) # '1-2-3'
```




    '1-2-3'




```python
# 문자열
mystring = 'samsung electronices' # 생성
# 특정 문자열이 있나?

# 수정/추가/삭제

# 변경된 새로운 문자열 생성

# 정렬
```




    ' acceeegilmnnorssstu'




```python
# List 
lst = [7, 8, 3, 6, 1, 5]

```


```python
# set

```


```python
# dictionary

```


```python
# enumerate string, list, tuple, range, dictionary,

```

### 얕은 복사 vs 깊은 복사


```python
# mutable 자료형을 할당하는 것은 객체 참조를 할당한다.
```


```python
origin_list = [1, 2, 3]
copy_list = origin_list

copy_list[0] = -1
print(origin_list, copy_list)
```

    [-1, 2, 3] [-1, 2, 3]
    


```python
# 새로운 리스트를 생성해서 할당하기
```


```python
origin_list = [1, 2, 3]
copy_list = origin_list[:]

copy_list[0] = -1
print(origin_list, copy_list)
```

    [1, 2, 3] [-1, 2, 3]
    


```python
# 리스트안의 요소들이 리스트(mutable)일 경우 얕은 복사(shallow copy)가 됨에 주의하시오.
```


```python
origin_list = [[1, 1, 1], 2, 3]
copy_list = origin_list[:]

copy_list[0][0] = -1

print(origin_list, copy_list)
```

    [[-1, 1, 1], 2, 3] [[-1, 1, 1], 2, 3]
    


```python
origin_list = [{1, 2, 3}, 2, 3]
copy_list = origin_list[:]

copy_list[0].add(4)
print(origin_list, copy_list)
```

    [{1, 2, 3, 4}, 2, 3] [{1, 2, 3, 4}, 2, 3]
    


```python
# 얕은 복사!!!!!!!!
import copy

origin_list = [[1, 1, 1], 2, 3]
copy_list = copy.copy(origin_list)

copy_list[0][0] = -1

print(origin_list, copy_list)
```

    [[-1, 1, 1], 2, 3] [[-1, 1, 1], 2, 3]
    


```python
#==============================
# 이게 딥~~한 복사여요...
#==============================
import copy

origin_list = [[1, 1, 1], 2, 3]
copy_list = copy.deepcopy(origin_list)    # !!!!!!!!!!!

copy_list[0][0] = -1

print(origin_list, copy_list)
```

    [[1, 1, 1], 2, 3] [[-1, 1, 1], 2, 3]
    


```python
# * 연산을 통해서 요소를 반복해서 생성하는 경우에 주의하시오.
lst = [0] * 5  # lst = [0 for i in raneg(5)]
print(lst)
```

    [0, 0, 0, 0, 0]
    


```python
# 다음을 실행해서 확인
lst = [[0] * 3] * 5
print(lst)
```

    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    


```python
lst = [[0] * 3] * 5
lst[0][0] = 1
print(lst)
```

    [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]
    


```python
lst = [0] * 3 for _ in range(3)
lst = [[for _ in range(3)] for _ in range(3)]
lst[0][0] = 1
print(lst)
```


      Input In [16]
        lst = [0] * 3 for _ in range(3)
                      ^
    SyntaxError: invalid syntax
    



```python

```


```python

```

> mutable 자료형을 함수 인자로 넘기는 경우


```python
def func(lst):
    lst[0] = -1
    print(lst)


lst = [1, 2, 3, 4]
func(lst)
print(lst)
```

    [-1, 2, 3, 4]
    [-1, 2, 3, 4]
    


```python
def func(a):
    a = -1
    print(a)
    
a = 100
func(a)
print(a)
```

    -1
    100
    


```python

```
