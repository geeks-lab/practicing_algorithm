# 전위 순회한 결과로부터 후위 순환 결과 구하는 프로그램 작성하기(이진트리임)

# 전위 순회 결과 -> 50 30 24 5 28 45 98 52 60
# 알 수 있는 사실
# 50 이 루트이고 50 보다 작은건 왼쪽 섭트리, 50보다 크면 오른쪽 섭트리

import sys
sys.setrecursionlimit(10 ** 6)
num_list = []

while 1:
    try:
        num_list.append(int(sys.stdin.readline()))
    except:
        break

def postorder(first, end):
    if first > end: # 재귀 종료 조건 : 루트가 남은것보다 크면 안되서
        return
    mid = end + 1 # root 보다 큰 값이 존재 하지 않는 경우에 # mid 9
    for idx in range(first+1,end+1):
        if num_list[first] < num_list[idx]: # 루트보다 큰 값을 mid로 설정하는거(인덱스)
            mid = idx
            break
        
    
    postorder(first+1, mid-1) # 왼쪽 서브트리
    postorder(mid, end) # 오른쪽 서브트리
    print(num_list[first]) # 후위 순회니까 자기 자신을 지금 찍어

postorder(0,len(num_list)-1) # 0, 8




