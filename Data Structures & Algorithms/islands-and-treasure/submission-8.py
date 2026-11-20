from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        CORRECT ANS: Multi-source BFS through 0s diffuse all at the same distance!! promise O(MN)
        1. Have all 0s put in the queue
        2. First start for all 0s with distance 1, then 2, then 3... (and only consider the INFs)
        3. use bfs queue to only consider INF as the next node to visit, stop when no more to visit in queue

        edge case: land cell cannot be turned
        """
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            x, y = queue.popleft()
            
            for dx, dy in direction:
                nx, ny = x + dx, y + dy

                # if out of boundary
                if nx < 0 or nx >= len(grid):
                    continue
                if ny < 0 or ny >= len(grid[0]):
                    continue
                
                # if it is a '-1' then skip
                if grid[nx][ny] == -1:
                    continue

                # if grid = INF
                if grid[nx][ny] == 2147483647:
                    grid[nx][ny] = grid[x][y] + 1
                    queue.append((nx, ny))    

