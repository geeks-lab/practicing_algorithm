# 구현이 쉽지만 느린 방법 O(V^2)

import sys
input = sys.stdin.readline
INF = int(1e9)

#n, m = 노드 개수, 간선 개수
n, m = map(int, input().split())
start = int(input()) #시작 노드
# 각 노드에 대해 (연결 노드, 거리) 값을 담기 위한 그래프
graph = [ [] for _ in range(n+1) ]
#다익스트라 알고리즘 수행 시 방문 여부 체크를 위한 리스트
visited = [0] * (n + 1) 
#최단 거리 테이블 
distance = [INF] * (n + 1)

for _ in range(m):
  #a노드에서 b노드로 가는 간선의 거리 c
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

#최단 거리 테이블의 최소값을 얻기 위한 함수
def get_smallest_node():
  idx = 0 
  min_value = INF
  for i in range(1, n + 1):
    if distance[i] < min_value and visited[i] == 0:
      min_value = distance[i]
      idx = i
  return idx

def dijkstra(start):
  #시작 노드에서 시작 노드까지의 거리 0 저장
  distance[start] = 0
  #시작 노드를 포함한 n개의 노드 방문
  for _ in range(n+1):
    #현재 가장 최단 거리가 짧은 노드를 꺼내서 방문 처리
    cur = get_smallest_node()
    visited[cur] = 1
    #현재 방문한 노드와 연결된 노드들에 대해 최단 거리 테이블 갱신
    for next in graph[cur]:
      #현재 노드까지의 최단 거리 + 현재 노드에서 다음 노드 까지의 거리
      cost = distance[cur] + next[1]
      #기존의 다음 노드까지의 최단 거리보다 현재 노드를 거친 다음 노드까지의 거리가 더 짧으면 테이블 갱신 
      if distance[next[0]] > cost:
        distance[next[0]] = cost

dijkstra(start)

for i in range(1, n+1):
  if i == INF:
    print("INFINITY")
  else:
    print(distance[i])