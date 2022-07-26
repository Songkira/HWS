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

#-----------------------------------------
# def low_and_up(word):
#     word_up = []
#     for i in range(len(word)):
#         if i % 2:
#             up_word = word[i].upper()
#             word_up.append(up_word)
#         else:
#             word_up.append(word[i])
#     return ''.join(word_up)

# print(low_and_up('apple')) # => aPpLe
# print(low_and_up('banana')) # => bAnAnA

#-----------------------------------------
def lonely(number):
    alone = []
    alone.append(number[0])
    for i in range(len(number)):
        if alone[-1] != number[i]:
            alone.append(number[i])
        else:
            pass
    return alone


# print(lonely([1, 1, 3, 3, 0, 1, 1])) # => [1, 3, 0, 1]
# print(lonely([4, 4, 4, 3, 3])) # => [4, 3