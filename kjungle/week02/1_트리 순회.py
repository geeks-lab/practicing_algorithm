'''
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.


'''

# 1:40 시작 - 혼자 2:40분까지 해보기

# Binary tree traversals

'''
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

preorder (root, left_child, right_child) - ABDCEFG
inorder (left_child, root, right_child) - DBAECFG
postorder (left_child, right_child, root) - DBEGFCA

'''
import sys

# 입력 받기
# 첫쨰줄 - 노드의 개수(1<=N<=26)
N = int(sys.stdin.readline().strip())  # 다음줄도 받으려구요

# 행렬로 저장하기-> tree = [list(map(int, input().split()))for i in range(n)]
# 딕셔너리로 저장하기
tree_dict={}
for _ in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    # root를 키값으로, 밸류값을 left, right이름으로 두개 저장하고 리스트로 묶기
    tree_dict[root]=[left, right]
#{'A': ['B', 'C'], 'B': ['D', '.'], 'C': ['E', 'F'], 'E': ['.', '.']}

def preorder(root):
    if root != '.': # 자식 없을 때 까지 재귀 호출
        print(root, end='') # root
        preorder(tree_dict[root][0]) # left
        preorder(tree_dict[root][1]) # right

def inorder(root):
    if root != '.': # 자식 없을 때 까지 재귀 호출
        inorder(tree_dict[root][0]) # left
        print(root, end='') # root
        inorder(tree_dict[root][1]) # right

def postorder(root):
    if root != '.': # 자식 없을 때 까지 재귀 호출
        postorder(tree_dict[root][0]) # left
        postorder(tree_dict[root][1]) # right
        print(root, end='') # root

preorder('A') # ABDCEFG
print()
inorder('A')
print()
postorder('A') # DBEGFCA
print()



#######
    # [내가 쓴 의사코드]
    # 자식이 없을 때까지 재귀 호출 
    # left 자식 있으면 내려가기 -> 시작점으로 이동하기
    #   자식이 아무도 없으면 자기 자신 찍기 
    #     올라가서 찍기 -> left 다음 root 찍어야하니까
    #     오른자식 있으면 찍기 -> left 다음 right 이니까 -> F (tree 종료)
    #        찍은 자식으로 이동 (tree 바뀜)
    #      오른자식 없으면 올라가기 -> 처음 루트로 왔고 왼쪽은 서치 완료.