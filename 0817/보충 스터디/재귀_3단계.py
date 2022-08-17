
# 3단계
# 누적합 출력하기
arr=[3,6,3,1,6]

# 3 9 12 13 19 13 12 9 3

# 1.sum을 전역으로 놓고 (global)
# 2.sum을 매개변수로 놓고
# 함수 진입하고 리턴하면서 출력하기















# -----------------------------
# 누적합 출력하기 !!!
# 2 8 12 13 21
# sum 변수를
# 1 전역변수로 놓고
# 2 매개변수 (지역변수)


# 1 전역변수 sum 활용하기
arr = [2, 6, 4, 1, 8]
# 21 13 12 8 2

sum = arr[0]

def abc(x):
    global sum
    print(sum)
    if x == 4:
        return
    sum += arr[x + 1]
    abc(x + 1)


abc(0)

# 2 매개변수 sum 이용
arr = [2, 6, 4, 1, 8]
# 21 13 12 8 2

def abc(x, sum):
    print(sum)
    if x == 4:
        return
    abc(x + 1, sum + arr[x + 1])


abc(0, arr[0])