# 여러 개의 값을 저장하는 변수에서 반복하여 값을 꺼내어 사용
# for ■ ■ in ★★:
    # ●● 
dust = [59, 24, 70]
# for (변수) in (데이터집합):
    # ●●
for value in dust: # 데이터 갯수만큼 반복
    print(value)

for i in range(3):
    print(i, dust[i]) # 위 반복문과 동일 결과 나옴