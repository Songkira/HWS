num = 100

print(f'num에 저장된 값은 {num} 입니다.')
import requests

url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021'
response = requests.get(url).json()

# print(response)
# print(response.get('drwtNo1'))
# print(response.get('drwtNo2'))
# print(response.get('drwtNo3'))
# print(response.get('drwtNo4'))
# print(response.get('drwtNo5'))
# print(response.get('drwtNo6'))

for i in range(1, 7):
	key = f'drwtNo{i}'
    
print(response.get(key))