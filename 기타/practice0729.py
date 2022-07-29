# from pprint import pprint
# from re import X

# data = [
#     ('java', 77),
#     ('python', 98),
#     ('html', 65),
#     ('css', 83) ,
# ]
# # 디폴트 기준으로 정렬 # 오름차순 # 첫번째 나온 값으로 정렬

# def func(x):
#     # print(x)
#     return x[0] # [('css', 83), ('html', 65), ('java', 77), ('python', 98)]
# print(sorted(data, key=func))#함수) 기준이 되는 값을 리턴해주는 함수 . map 이랑 비슷
# # 값을 전달할수도 있고 출력?도 가능
# # 리턴되는 값을 기준으로 정렬

# def func(x):
#     # print(x)
#     return x[1] # [('html', 65), ('java', 77), ('css', 83), ('python', 98)]
# print(sorted(data, key=func))
# # 두번째 값인 정수를 기준으로 정렬

# def func(x):
#     # print(x)
#     return x[1]
# print(sorted(data, key=lambda x: x[1]))

# # --------------------------------------------
# # 딕셔너리
# scores = [
#     {'name': 'java', 'score' : 77},
#     {'name': 'python', 'score' : 98},
#     {'name': 'html', 'score' : 65},
#     {'name': 'css', 'score' : 83},
# ]

# print(sorted(scores, key=lambda x:x['score']))
# # value 기준으로 정렬
# # [{'name': 'html', 'score': 65}, {'name': 'java', 'score': 77}, 
# # / {'name': 'css', 'score': 83}, {'name': 'python', 'score': 98}]

# print(sorted(scores, key=lambda x:x['score'], reverse=True))
# # 내림차순 정렬
# # [{'name': 'python', 'score': 98}, {'name': 'css', 'score': 83}, 
# # {'name': 'java', 'score': 77}, {'name': 'html', 'score': 65}]

