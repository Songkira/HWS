# 4 단계 (그림참조)
#
# 항의 개수를 입력받은 후
# 각 항에서 숫자 1개씩 택하여 모두 더했을떄
# 합이 10 이상이 나오는 경우는 몇가지??
#
# 항
# 1
# 3
# 5
# -7

# sum 매개변수

arr=[1,3,5,-7]

cnt=0
def abc(x,sum):
    global cnt
    if x==3: # 항의개수  바닥조건
        if sum>=10:
            cnt+1
        return

    for i in range(4):
        abc(x+1,sum+arr[i])

abc(0,0) # x sum
print(cnt)

#----------------------------------
#sum 을 전역변수로 활용

arr=[1,3,5,-7]

sum=0
cnt=0
def abc(x):
    global sum,cnt
    if x==3:
        if sum>=10:
            cnt+=1
        return

    for i in range(4):
        sum+=arr[i]
        abc(x+1)
        sum-=arr[i]

abc(0)