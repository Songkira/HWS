import sys; sys.stdin = open('1221.txt', 'r')

num_str = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for tc in range(1, int(input()) + 1):
    tc_num, N = input().split()
    N = int(N)
    nums = input().split()

    cnt = [0] * 10  # 0 부터 9까지 인덱스로 사용
    for num in nums:
        for i in range(10):
            if num == num_str[i]:
                cnt[i] += 1
                break

    ans = f'#{tc}'
    for i in range(10):
        ans += f' {num_str[i]}' * cnt[i]
    print(ans)

#--------------------------------------------------------------
# 딕셔너리로 풀기
for tc in range(1, int(input()) + 1):
    tc_num, N = input().split()
    nums = input().split()

    num_dict = {}
    for num in nums:
        num_dict[num] = num_dict.get(num, 0) + 1

    ans = f'#{tc}'
    for i in range(10):
        ans += f' {num_str[i]}' * num_dict[num_str[i]]
    print(ans)