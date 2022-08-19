max = 0
for tc in range(1, 5+1):

    score = list(map(int, input().split()))
    sum = 0
    for i in range(4):
        sum += score[i]

    if max < sum:
        max = sum

print(tc, max)
