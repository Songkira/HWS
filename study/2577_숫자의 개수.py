# number_list = list(map(int, input().split()))

number = 1
for _ in range(3):
    number *= int(input())

number = list(str(number))
# print(number)
number_list = [0] * 10

for i in range(len(number)):
    for j in range(len(number_list)):
        if int(number[i]) == j:
            number_list[j] += 1
# print(number_list)

for num in number_list:
    print(num)
