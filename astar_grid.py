import heapq
import random
ROWS, COLS = 20, 20
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def generate_grid(density=0.2):
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    
    for i in range(ROWS):
        for j in range(COLS):
            if random.random() < density:
                grid[i][j] = 1  
    
    grid[0][0] = 0
    grid[ROWS-1][COLS-1] = 0
    return grid
def astar(grid, start, goal):
    pq = [(0, start)]
    came_from = {}
    cost = {start: 0}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            break

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue

                new_cost = cost[current] + 1

                if neighbor not in cost or new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                    priority = new_cost + heuristic(goal, neighbor)
                    heapq.heappush(pq, (priority, neighbor))
                    came_from[neighbor] = current

    return came_from

def reconstruct_path(came_from, start, goal):
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = came_from.get(current)
        if current is None:
            return []  # no path found

    path.append(start)
    path.reverse()
    return path
grid = generate_grid(0.2)
start = (0, 0)
goal = (ROWS-1, COLS-1)

came_from = astar(grid, start, goal)
path = reconstruct_path(came_from, start, goal)

if path:
    print("Path found!")
    print("Path length:", len(path))
else:
    print("No path found")