# # API
# # 두 소프트웨어가 서로 통신할 수 있도록 연결 시켜주는 인터페이스
# # Application Programming Interface

# import requests

# url = 'https://api.agify.io/?name=kira&country_id=KR'

# response = requests.get('url') # url에 정보를 달라는(get) 요청(requests)을 보내줘
# # data = response.json()
# data = requests.get(url).json()
# print(data)
# print(type(data))
# print(data['name'], data['age'])

# # requests.get('url').json() # url에 정보를 달라는(get) 요청(requests)을 보내고
#                             # json

# url = 'https://api.agify.io/?name=kira'
# print(requests.get(url))
# # 딕셔너리 형태로 바꿔준다

# print(response.get('name'))
# print(response.get('age'))
# # key 값만 가져올수도 있다

# scores = [80, 89, 99, 83] # => 87.7
# average = sum(scores)/len(scores)
# print(average)

# x, y = map(int,input('숫자 입력 :').split())
# plus = x+y
# print(plus)

# lunch = {'칼국수':9000, '제육볶음':8000, '순두부':7000, '짜장면':6500, '닭갈비':8500}

# lunch_price = sum(lunch.values())/len(lunch.values())

# print(int(lunch_price))


# T = int(input('입력:'))
# for test_case in range(1, T + 1):
#     a, b = map(int,input().split())
#     if a > b:
#         print((f'#{test_case} >'))
#     elif a == b:
#         print((f'#{test_case} ='))
#     else:
#         print((f'#{test_case} <'))

lunch = ['짜장면', '짬뽕', '탕수육']

for idx, num in lunch:
    print(idx, num)