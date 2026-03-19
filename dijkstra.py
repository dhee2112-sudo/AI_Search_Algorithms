import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

graph = {
    "Delhi": {"Jaipur": 280, "Lucknow": 500},
    "Jaipur": {"Delhi": 280, "Mumbai": 1140},
    "Lucknow": {"Delhi": 500, "Patna": 600},
    "Mumbai": {"Jaipur": 1140, "Bangalore": 980},
    "Bangalore": {"Mumbai": 980},
    "Patna": {"Lucknow": 600}
}

start = "Delhi"
result = dijkstra(graph, start)

print("Shortest distances from", start)
for city, dist in result.items():
    print(city, ":", dist)