print("시작")
a = 10
if a > 0: # if 안에 if문 가능
    print("양수")
elif a == 0:
    print("zero")
else:
    print("음수")
# alt + shift + 화살표 -> 복사됨 / alt + 화살표 -> 이동

print("끝")


dust = 100
# 내가 쓴거(부등호 잘못됨) / 부등호 조심!!!!!
if dust > 150:
  print("매우 나쁨")
elif 150 >= dust > 80:
  print("나쁨")
elif 80 >= dust > 30:
  print("보통")
else:
  print("좋음")

# 다른 형식
if dust > 150:
    print("매우나쁨")
elif 80 < dust and dust <= 150: # 80 < dust <= 150 도 가능(python 만)
    print("나쁨")
elif 30 < dust and dust <= 80:
    print("보통")
else:
    print("좋음")