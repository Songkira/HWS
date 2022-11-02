N, K = map(int, input().split())

grade = []
for _ in range(N):
    s, g = map(int, input().split())    # 성별, 학년
    grade.append([s, g])

room = 0
# [0, 0] == 학년, 명수
m_group = [[0, 0]]*7
f_group = [[0, 0]]*7
# print(m_group, f_group)
for i in range(N):
    # num = 1
    for j in range(1, 7):
        if grade[i][1] == 1:
            m_group[j][0] = j
            m_group[j][1] += 1
        else:
            f_group[j][0] = j
            f_group[j][1] += 1
# print(m_group, f_group)