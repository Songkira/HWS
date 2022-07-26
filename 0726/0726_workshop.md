1. 무엇이 중복일까
문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는
duplicated_letters 함수를 작성하시오
```
duplicated_letters(‘apple’) # => [‘p’]
duplicated_letters(‘banana’) # => [’a’, ‘n’]
```
```python
def duplicated_letters(word):
    word_lst = []
    word_2 = []
    for i in word:
        if i not in word_lst:
            word_lst.append(i)
        else:
            word_2.append(i)
            set_w2 = set(word_2)
            lst_w2 = list(set_w2)
    return lst_w2
```
2. 소대소대
문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여
반환하는 low_and_up 함수를 작성하시오. 
이때, 전달 받는 문자열은 알파벳으로만 구성된다
```
low_and_up(‘apple’) # => aPpLe
low_and_up(‘banana’) # => bAnAnA
```
```python
def low_and_up(word):
    word_up = []
    for i in range(len(word)):
        if i % 2:
            up_word = word[i].upper()
            word_up.append(up_word)
        else:
            word_up.append(word[i])
    return ''.join(word_up)
```
3. 솔로 천국 만들기
정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남
기고 제거한 list를 반환하는 lonely 함수를 작성하시오. 
이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야 한다.
```
lonely([1, 1, 3, 3, 0, 1, 1]) # => [1, 3, 0, 1]
lonely([4, 4, 4, 3, 3]) # => [4, 3]
```
```python
def lonely(number):
    alone = []
    alone.append(number[0])
    for i in range(len(number)):
        if alone[-1] != number[i]:
            alone.append(number[i])
        else:
            pass
    return alone
```