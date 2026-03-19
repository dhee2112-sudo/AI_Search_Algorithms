import random
from astar_grid import astar, generate_grid, reconstruct_path

ROWS, COLS = 20, 20

grid = generate_grid(0.1)
start = (0, 0)
goal = (ROWS-1, COLS-1)

current = start

while current != goal:
    came_from = astar(grid, current, goal)
    path = reconstruct_path(came_from, current, goal)

    if not path:
        print("❌ No path found!")
        break

    # Move ONE STEP forward
    if len(path) > 1:
        next_step = path[1]
    else:
        next_step = goal

    current = next_step
    print("➡️ Moving to:", current)

    # Add dynamic obstacle
    x, y = random.randint(0, ROWS-1), random.randint(0, COLS-1)

    if (x, y) != current and (x, y) != goal:
        grid[x][y] = 1
        print("⚠️ New obstacle at:", (x, y))

print("🏁 Reached goal!" if current == goal else "❌ Failed")