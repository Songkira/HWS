plastic_set = [0, 1, 2, 3, 4, 5, 7, 8, 0, 0]
N = len(plastic_set)

room_number = list(map(int, input()))
cnt = [0] * (N+1)

count_set = 1
for val in room_number:
    cnt[val] += 1
    if (val in plastic_set) and cnt[val] > 1:
        count_set += 1
    elif (val not in plastic_set) and cnt[val] % 2 == 1 and cnt[val] > 2:
        count_set += 1

print(count_set)