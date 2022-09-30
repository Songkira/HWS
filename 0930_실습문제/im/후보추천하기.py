
N = int(input())    # 사진틀 개수
C = int(input())    # 전체 학생의 총 추천 횟수
# 추천받은 학생을 나타내는 번호 순서 리스트
number = list(map(int, input().split()))

# count_lst = [0] * (100 + 1)   # 번호 추천횟수 카운팅
# score = [0] * (100 + 1) # 추천횟수 카운팅한걸 카운팅하는 리스트를 또 따로 만들어야 되나?
# 딕셔너리로 만들기
picture = {}    # 사진틀 리스트

# 삭제
# .pop(인덱스) / .remove(값) / del 리스트명[인덱스] / 모두제거 =>.clear()

for i in range(C):
    # 사진틀에 사진이 있다면
    if number[i] in picture:
        # 추천횟수 증가
        picture[number[i]][0] += 1
    # 사진틀에 사진이 없다면
    else:
        if len(picture) < N:
            picture[number[i]] = [1, i]
        # 사진틀의 빈자리가 없어질때
        elif len(picture) >= N:
            # 추천 받은 횟수, 게시된 순서로 정렬
            # 추천 받은 횟수가 적고 오래 게시된 사진이 맨 앞에 오게 됨
            sort_pic = sorted(picture.items(), key=lambda x: (x[1][0], x[1][1]))
            # 맨 첫번째 사진을 지운다.
            del picture[sort_pic[0][0]]
            picture[number[i]] = [1, i]
                # # 추천받은 횟수가 가장 적은 학생의 사진 삭제
                # if count_lst[k] == min(count_lst):
                #     picture.remove(k)
                #     # 사진틀에 게시된 사진이 삭제되는 경우 추천받은 횟수 카운팅 초기화
                #     count_lst[number[k]] = 0
                # # 추천받은 횟수가 가장 적은 학생이 두명 이상일 경우, 0 은 제외
                # score[count_lst[k]] += 1
                # # if count_lst[k] != 0 and count_lst[k]
answer = sorted(picture.keys())
print(*answer)
print(picture)
