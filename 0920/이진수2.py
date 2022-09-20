
for tc in range(1, int(input())+1):
    N = float(input())

# num = 1*(2**-1)
# print(num)
# 차례로 더해서 같은 숫자로 만들면?
    two_lst = [] 
    for i in range(1, 12+1):
        if N < 1*(2**(-i)):
            two_lst.append('0')
        else:
            N -= 1*(2**(-i))
            two_lst.append('1')
        if N == 0:
            print(f'#{tc}', ''.join(two_lst))
            break

    if N != 0:
        print(f'#{tc}', 'overflow')