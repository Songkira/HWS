1. 평균 점수 구하기
key 값으로 과목명, value 값으로 점수를 가지는 dictionary를 전달 받아, 전체 과목의
평균 점수를 반환하는 함수 get_dict_avg 함수를 작성하시오.

```
def get_dict_avg(dict1):
    result = 0
    for i in dict1.values():
        result += i
    return result / len(dict1.keys())
```

get_dict_avg({
'python' : 80,
'web' : 83,
'algorithm' : 90,
'django' : 89,
}) # => 85.5

2. 혈액형 분류하기
여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의
종류, value는 사람 수인 dictionary를 반환하는 count_blood 함수를 작성하시오

``` 
def count_blood(lst):
    dict_type = {}
    for key in lst:
        if key in dict_type:
            dict_type[key] += 1
        else:
            dict_type[key] = 1
    return dict_type
```

count_blood([
'A', 'B', 'A', 'O', 'AB', 'AB’,
'O', 'A', 'B', 'O', 'B', 'AB’,
]) # => {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
