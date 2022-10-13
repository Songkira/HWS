plastic_set = [0, 1, 2, 3, 4, 5, 7, 8, 0, 0]
N = len(plastic_set)

room_number = list(map(int, input()))
cnt = [0] * (N+1)

count_set = 1
for val in room_number:
    if val == 6 or val == 9:
        if cnt[6] <= cnt[9]:
            cnt[6] += 1
        else:
            cnt[9] += 1
    else:
        cnt[val] += 1


print(max(cnt))