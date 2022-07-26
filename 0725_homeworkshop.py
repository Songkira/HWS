```def count_vowels(word):
#1
    num_vowels = 0
    for vowel in 'ieaou':
        num_vowels += word.count(vowel)
    return num_vowels
#2 (단순한 방법)
    for vowel in 'ieaou':
        for ch in word:
            if vowel == ch:
                num_vowels += 1
    return num_vowels ```          
# ----------------------------------
# 정사각형 만들기
```
def only_square_area(width, height):
# 1
    square_list =[]
    for w in width:
        for h in height:
            if w == h:
                square_list.append(w*h)
    return square_list
# 2
    return[w * h for w in width for h in height if w==h]
#  3. set 이용법
    square_list = []
    wh_set = in set(width) & set(height)
    for wh in wh_set:
        square_list.append(wh**2)```

workshop 01
```def get_dict_avg(score_dict):
# 1
    total_score = 0
    subject = 0
    for keys in score_dict:
        total_score += score_dict[keys]
        subject += 1
    return total_score / subject
# 2 파이썬만 가능
    return sum(score_dict.values())/len(score_dict)```

# workshop 02
```
def count_blood(blood_list):
# 1
    blood_dict = {}
    for blood in blood_list:
        if blood in blood_dict:
            blood_dict[blood] += 1
        else:
            blood_dict[blood] = 1 # 없으면 새로 추가
    return blood_dict
# 2
    blood_dict[blood] = blood_dict.get(blood, 0) + 1
    return blood_dict```



