
cute_h = 0
not_cute = 0
for tc in range(int(input())):
    cute = int(input())

    if cute == 1:
        cute_h +=1
    elif cute == 0:
        not_cute += 1

if cute_h > not_cute:
    print('Junhee is cute!')
elif cute_h < not_cute:
    print('Junhee is not cute!')