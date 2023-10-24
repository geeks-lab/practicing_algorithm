'''
1. 트리에 속하지 않은 정점들 중
2. 트리에 인접한 간선에서
3. 최소 가중치의 간선을 선택
-------------------------
1. visited 리스트를 사용하여 처리
2. 정점이 트리에 편입 될 때마다 정점의 인접 간선 정보를 업데이트
3. 정점 별 최소 비용을 업데이트하여 다음 최소 가중치 간선을 고름 (min_adj)
'''
from heapq import *

#인접 리스트 저장용
adj = defaultdict(list)
#인접 리스트는 adj[V1] = [[weight,V2],..] 
#형식으로 저장되어있다.
...

# 트리의 노드들 저장 (vistied와 같은 역할)
Tree_node = set([0])
# 트리에 인접한 간선을 저장하는 cand_list
# 첫 간선으로 0번째 노드의 간선을 몽땅 저장
cand_list = adj[0]
# heap 구조화시켜 최저 가중치 간선이 제일 앞으로 옴
heapify(cand_list)
# 최소 신장 트리 값을 저장할 MST
MST = 0

while cand_list:
	# 트리에 인접한 간선을 하나씩 꺼내서 (최소 순으로 꺼내진다.)
	w, node = heappop(cand_list)
    	# 간선의 목적지가 트리가 아니면 (cycle 방지)
	if node not in Tree_node:
    		# 정점을 트리에 편입 (가중치가 최소닌까) 
		Tree_node.add(node)
        	# 가중치 추가
		MST += w
        # 트리에 정점이 추가되었으니 트리 인접 간선 추가요
	for e in adj[node]:
    		# 근데 트리면 안댐 ㅋ
    		if e[1] not in Tree_node:
        	# heappush로 넣어서 
            	# 가중치 최소 간선이 제일 앞으로..
        		heappush(cand_list,e)