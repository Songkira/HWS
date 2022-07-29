import random
# 1 ~ 45 까지 숫자들 집합
nums = range(1, 46)

lotto_nums = random.sample(nums, 6)

print(lotto_nums)