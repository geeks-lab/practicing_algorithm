# https://blog.naver.com/ndb796/221230967614

# https://c4u-rdav.tistory.com/48

'''
크루스칼
간선의 가중치가 작은 것부터 그래프에 포함시키는 것이기 때문에
모든 간선 정보를 오름차순으로 정렬을 해주고 하나씩 포함시킨다.
+ 사이클을 형성하면 안되기 루트 테이블로 union-find를 사용해
두 노드가 연결되어있는지(같은 루트 노드를 갖고 있는지) 확인한다.
'''
import sys
V, E = map(int, sys.stdin.readline().split())  # 정점, 간선
parent = [i for i in range(V + 1)]  # 부모 테이블 #자기 자신으로 초기화
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]  # 그래프 정보
graph.sort(key=lambda x: x[2])  # (from , to, cost) #코스트를 기준으로 오름차순

"""
union-find란?
두 노드가 같은 그래프에 속하는지 판별하는 알고리즘
union : 노드를 합치는 연산
find : 루트 노드를 찾는 연산
- 경로 압축을 통해 시간 복잡도를 감소 시킬 수 있음
"""

# 부모찾기 함수
def find(x):
    global parent
    if parent[x] != x:  # 부모가 자기 자신이 아니라면
        parent[x] = find(parent[x])  # 계속 올라가기 (경로 압축)
    return parent[x]
# union(서로수 - 사이클 확인)
def union(f, t):
    global parent
    f = find(f)
    t = find(t)
    if f < t:  # 정점 번호가 작은게 우선
        parent[t] = f
    else:
        parent[f] = t
# MST 비용 계산
totalCost = 0
# 최소 신장 트리
MST = []
for info in graph:
    f, t, cost = info
    if find(f) != find(t):  # f와 t가 서로 다른 집합에 속해 있으면 (부모가 같지 않다면)
        union(f, t)
        MST.append((f, t)) #튜플로 
        totalCost += cost
# print(MST)
print(totalCost)