#순열 - 금은동 메달..
#조합 - 팀 만들기
# A B C D
# 전단계 >= 내가 앞으로 들어갈
# 이럴경우 컨티뉴

arr=['A','B','C','D']
path=['']*3
def abc(level):
    if level==3:
        for i in range(3):
            print(path[i],end=' ')
        print()
        return
    for i in range(4):
        if level>0 and path[level-1] >= arr[i]: continue
        path[level]=arr[i]
        abc(level+1)

abc(0)