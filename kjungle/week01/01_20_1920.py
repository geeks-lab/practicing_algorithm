
# 수 찾기 이분탐색



# 첫줄 : 자연수 n
# 두번쨰줄 : A[1], A[2], …, A[N]


'''
이분탐색 - 정렬 해주고 mid가 찾던 값인지 양쪽에서 옭매이면서 확인

Left = 0
Right = n -1

가운데  = left + right // 2
'''


n = int(input())
alist = list(map(int, input().split(' ')))
alist.sort()

m = int(input())
targets = list(map(int, input().split(' ')))

def binary(target):
    left = 0
    right = n - 1

    while left <= right: # left랑 right랑 만나면 종료
        mid = (left + right) // 2 # 가운데
        if alist[mid] == target:
            return True # 찾았당
        
        # 옮메여가자
        if target < alist[mid]:
            right = mid - 1
        elif target > alist[mid]:
            left = mid + 1

for i in range(m):
    if binary(targets[i]):
        print(1)
    else:
        print(0)

        
            



        
               


    #2차 배열
    #data=[list(map(int,input().split()))for i in range(n)]
#poussin()

