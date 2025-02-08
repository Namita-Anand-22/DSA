from collections import deque

def orangesRotting(grid):
    if not grid:
        return -1

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    # Step 1: Collect all rotten oranges and count fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, time)
            elif grid[r][c] == 1:
                fresh_count += 1

    # Step 2: BFS from all initially rotten oranges
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    time_elapsed = 0

    while queue:
        r, c, time_elapsed = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2  # Mark as rotten
                fresh_count -= 1
                queue.append((nr, nc, time_elapsed + 1))

    # Step 3: If there are still fresh oranges left, return -1
    return time_elapsed if fresh_count == 0 else -1
