
N = int(input())    # 사진틀 개수
C = int(input())    # 전체 학생의 총 추천 횟수
# 추천받은 학생을 나타내는 번호 순서 리스트
number = list(map(int, input().split()))

count_lst = [0] * (100 + 1)   # 번호 추천횟수 카운팅
score = [0] * (100 + 1)# 추천횟수 카운팅한걸 카운팅하는 리스트를 또 따로 만들어야 되나?
picture = []    # 사진틀 리스트

# 삭제
# .pop(인덱스) / .remove(값) / del 리스트명[인덱스] / 모두제거 =>.clear()

for i in range(C):
    # 리스트 내 번호를 인덱스로 삼아 추천횟수 카운팅
    count_lst[number[i]] += 1
    # 사진틀에 추가
    picture.append(number[i])
    if len(picture) == N:   # 사진틀의 갯수가 N과 일치하게 되면
        for k in range(len(count_lst)): # 번호 추천횟수 카운팅 리스트 인덱스 확인
            # 추천받은 횟수가 가장 적은 학생의 사진 삭제
            if count_lst[k] == min(count_lst):
                picture.remove(k)
                # 사진틀에 게시된 사진이 삭제되는 경우 추천받은 횟수 카운팅 초기화
                count_lst[number[k]] = 0
            # 추천받은 횟수가 가장 적은 학생이 두명 이상일 경우, 0 은 제외
            score[count_lst[k]] += 1
            # if count_lst[k] != 0 and count_lst[k]

print(picture)
print(count_lst)
print(score)