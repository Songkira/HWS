N = int(input())

for _ in range(N):
    one, two = input().split()
    one_lst = list(one)
    two_lst = list(two)
    sort_one = sorted(one_lst)
    sort_two = sorted(two_lst)

    # for i in range(len(one_lst)):
    #     for j in range(len(two_lst)):
    #         if i == j and one_lst[i] == two_lst[j]:
    #             print('Possible')
    #             break
    #         else:
    #             print('Impossible')
    #             break
    if sort_one == sort_two:
        print('Possible')
    else:
        print('Impossible')