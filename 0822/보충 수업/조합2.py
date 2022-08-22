# # 조합 구현 !!


arr=['A','B','C','D']
path=['']*3
def abc(level,start):
    if level==3:
        for i in range(3):
            print(path[i],end=' ')
        print()
        return
    for i in range(start,4):
        path[level]=arr[i]
        abc(level+1,i+1)

abc(0,0)  # level start