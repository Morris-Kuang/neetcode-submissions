class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        DFS to traverse the lands connected, then look for a second one
        use dict to record the seen nodes
        
        """
        seen = set()
        count = 0

        def dfs(x, y):
            # base: if out of boundary or meets "0" or meet counted nodes
            if (x < 0 or x == len(grid)) or (y < 0 or y == len(grid[0])):
                return
            if grid[x][y] == "0" or (x,y) in seen:
                return
            
            seen.add((x,y))
            # choice: up, down, left, right
            if (y-1) >= 0:
                dfs(x, y-1)
            if (y+1) < len(grid[0]):
                dfs(x, y+1)
            if (x-1) >= 0:
                dfs(x-1, y)
            if (x+1) < len(grid):
                dfs(x+1, y)

            return
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0" or (i,j) in seen:
                    continue
                else:
                    count += 1
                    dfs(i,j)
        
        return count

                