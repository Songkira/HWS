# 1. 내가 한거
# def duplicated_letters(word):
#     word_lst = []
#     word_2 = []
#     for i in word:
#         if i not in word_lst:
#             word_lst.append(i)
#         else:
#             word_2.append(i)
#             set_w2 = set(word_2)
#             lst_w2 = list(set_w2)
#     return lst_w2

# duplicated_letters('apple') # => [‘p’]
# duplicated_letters('banana') # => [’a’, ‘n’]
# # 2
# def duplicated_letters(words): 
#     result = []
#     words = list(words) # 문자단위로 쪼개서 저장
#     for word in words: # ['a','p','p','l','e']
#         i = 0
#         words.remove(word) # word = 'p'
#         if word in words: # 지웠는데도 남아있으면
#             if word not in result:
#                 result.append(word)
#         words.insert(i, word)
#     return result
# # 3 
# def duplicated_letters(word):
#     chr_set = set() # 문자열을 담을 셋을 선언 및 초기화
#                     # 문자가 문자열에서 중복된다면 셋에 해당 문자
#     for chr in word:
#         if word.count(chr) >1:
#             chr_set.add(chr)

#     return list(chr_set)
#  
# # 4 set, conut 없이 작성된 코드(교수님)
# def duplicated_letters(word):
#     once = [] # 처음나온 문자를 저장
#     mult = [] # 중복해서 나온 문자를 저장
#     for ch in word: 
#         if ch not in once: # 처음 나온 문자인가?
#             once += [ch] # list끼리 합칠꺼면 append 외에 += 해도 됨
#         elif ch not in mult: # 중복된 문자인데 mult에 없는건가?
#             mult += [ch]
#     return mult

#-----------------------------------------
# 1. 내가 한거
#  def low_and_up(word):
#     word_up = []
#     for i in range(len(word)):
#         if i % 2:
#             up_word = word[i].upper()
#             word_up.append(up_word)
#         else:
#             low_word = word[i].lower()
#             word_up.append(low_word)
#     return ''.join(word_up)

# print(low_and_up('apple')) # => aPpLe
# print(low_and_up('banana')) # => bAnAnA
# 2. 교수님
# def low_and_up(word):
#     ret = ''
#     for idx, val in enumerate(word):
#         if idx % 2 == 0: # 짝수 
#             ret += val.lower()
#         else:            # 홀수
#             ret += val.upper()
#     return ret

#     for idx, val in enumerate(word):
#         if idx % 2 == 0:
#             ret += word[i].lower()
#         else:
#             ret += word[i].upper()
#     return ret
# # 3 
# def low_and_up(words):
#     words = words.lower()
#     new_word =[]
#     n = 0
#     for i in words:
#         if n % 2:
#             new_word.append(i.upper())
#         else:
#             new_word.append(i)
#         n += 1
#     new_word = ''.join(new_word)
#     return new_word

#-----------------------------------------
# 1. 내가 한거
# def lonely(number):
#     alone = []
#     alone.append(number[0])
#     for i in range(len(number)):
#         if alone[-1] != number[i]:
#             alone.append(number[i])
#         else:
#             pass
#     return alone


# print(lonely([1, 1, 3, 3, 0, 1, 1])) # => [1, 3, 0, 1]
# print(lonely([4, 4, 4, 3, 3])) # => [4, 3]
# # 2
# def lonely(number):
#     k = n = 0
#     lonely_number = []
#     for i in lonely_number:
#         if k == 0:
#             lonely_number.append(i)
#             n += 1
#             k += 1
#         else:
#             if i == lonely_number[n-1]:
#                 pass
#             else:
#                 lonely_number.append(i)
#                 n += 1
#     return lonely_number