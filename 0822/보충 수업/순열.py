# 순열
# A B C D 카드 3묶음
# 각 묶음에서 1장씩 뽑았을때 나올수 있는 모든 경우 출력
# ( 단, 한번 뽑았던 알파벳은 다시 나오면 않된다!!) -> 순열


arr=['A','B','C','D']
path=['']*3
used=[0]*4
def abc(level):
    if level==3:
        for i in range(3):
            print(path[i],end=' ')
        print()
        return
    for i in range(4):
        if used[i]==1: continue
        used[i]=1
        path[level]=arr[i]
        abc(level+1)
        used[i]=0

#
# 들어가기 전에 1체크
# 리턴후에 0으로 원상복구 해주는데
# 이리 1이 체크가 되어 있다면 들어가지 않겠다!

abc(0)