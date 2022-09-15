lst = []
for _ in range(9):
    x = int(input())
    lst.append(x)
print(lst)
sumx = sum(lst)
rem = []
for i in range(9-2+1):
    for j in range(i+1, 9):
        twosum = lst[i]+lst[j]
        if sumx - twosum == 100:
            rem.append(lst[i])
            rem.append(lst[j])
            print(rem)
        break
        lst.pop(lst[i])
        lst.pop(lst[j])

lst.sort()
for i in range(len(lst)):
    if lst[i] != rem[0] and lst[i] != rem[1]:
        print(lst)