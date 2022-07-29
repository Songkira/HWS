# def list_sum(*args):
#     result = 0
#     args = set(*args)
#     for number in args:
#         result += number
#     return result

# print(list_sum([1, 2, 3, 4, 5]))
# ------------------------------------
# lst = [{'name': 'kim', 'age': 12},
# {'name': 'lee', 'age': 4}]

# def dict_list_sum(x):
#     result = 0
#     for i in range(len(x)):
#         result += x[i]['age']
#         return result

# print(dict_list_sum(lst))

# ------------------------------------

def all_list_sum(lst):
    answer = []
    for n in lst:
        for j in range(len(n)):
            answer.append(n[j])




all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) 

# ------------------------------------

# ------------------------------------