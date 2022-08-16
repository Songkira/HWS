# 시간복잡도 : O(n+k) O ( n + k )

K = 4                           # 최대값
A = [0, 4, 1, 3, 1, 2, 4, 1] # 원본 자료
B = [0] * len(A)             # 정렬된 자료를 저장
C = [0] * (K + 1)            # 카운팅(횟수) 저장

for val in A: # 빈도수 계산
    C[val] += 1 # C의 각자 지정된 자릿수에 +1 되는것
# print(f'C :', C) # [1, 3, 1, 1, 2]

for i in range(1, K + 1): # 누적 빈도수 계산
    C[i] = C[i -1] + C[i]
# print(f'C :', C) # [1, 4, 5, 6, 8]

# 원본 자료들을 하나씩 옮긴다.
# A에서 하나씩 가져와서 C의 내용을 보고 B로 옮긴다.
for i in range(len(A) -1, -1, -1):
    # A[i] --> B[C의 내용을 참고] = A[i]
    C[A[i]] -=  1
    B[C[A[i]]] = A[i]
    print(f'C :',C)
    print(f'A :',A)
    print(f'B :',B)
    print('---------------------')

    # C[A[7]] -> C[1] -= 1
    # C[A[6]] -> C[4] -= 1
    # C[A[5]] -> C[2] -= 1

    # B[C[1]] -> C[1]은 4 이었지만 -1이 되서 3
    # B[C[4]] -> C[4]은 8 이었지만 -1이 되서 7
    # B[C[2]] -> C[2]은 5 였지만 -1이 되서 4
    # B[3] = A[7]-> B[7] = A[6] -> B[4] = A[5]
