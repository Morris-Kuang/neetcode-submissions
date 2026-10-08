class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        DFS: been thru deepest route and form area
        seen as a set to record all nodes counted
        base case: meet 0, is seen, out of boundary
        decision: up down left right

        edge cases - all 0, all 1
        """
        seen = set()
        maxArea = 0
        self.area = 0

        def dfs(x, y):
            # base: if out of boundary or meets "0" or meet counted nodes
            if (x < 0 or x == len(grid)) or (y < 0 or y == len(grid[0])):
                return
            if grid[x][y] == 0 or (x,y) in seen:
                return
            
            seen.add((x,y))
            self.area += 1
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
                if grid[i][j] == 0 or (i,j) in seen:
                    continue
                else:
                    self.area = 0
                    dfs(i,j)
                    if self.area > maxArea:
                        maxArea = self.area
                    
        
        return maxArea

                
        
        