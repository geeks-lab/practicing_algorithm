import heapq
def dijkstra(graph,start):
    distances={node:float('inf')for node in graph}
    distances[start]=0
    queue=0
    heapq.heappush(queue,[distances[start],start])
    while queue:
        current_distance,current_destination=heapq.heappop(queue)
        if distances[current_destination]<current_distance:
            continue
        for new_destination,new_distance in graph[currnet_destination].items():
            distance=current_distance+new_distance
            if distance<distances[new_destination]:
                distances[new_destination]=distance
                heqpq.heappush(queue,[distance,new_destination])
    return distances
graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
start_node = 'A'  # 시작 노드를 선택
shortest_distances = dijkstra(graph, start_node)
print(shortest_distances)