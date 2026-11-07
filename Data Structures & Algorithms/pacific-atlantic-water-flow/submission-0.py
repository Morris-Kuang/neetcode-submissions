from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        bfs for each node: <0 for r, c => Pacific | > len() Atlantic

        approach: traverse backwards from the cliff and find the one bigger to mark them down (able to flow into that ocean)
        result: intersect grids
        """

        pacific, atlantic = set(), set()

        def search(i, j, paci):
            ocean = pacific if paci else atlantic

            queue = deque([(i, j)])  # put accesible neighbors in
            ocean.add((i, j))

            while queue:
                i, j = queue.popleft()
                curr = heights[i][j]  

                # left
                if i - 1 >= 0 and heights[i-1][j] >= curr and (i-1, j) not in ocean:
                    ocean.add((i-1, j))
                    queue.append((i-1, j))
                
                # right
                if i + 1 < len(heights) and heights[i+1][j] >= curr and (i+1, j) not in ocean:
                    ocean.add((i+1, j))
                    queue.append((i+1, j))
                
                # up 
                if j - 1 >= 0 and heights[i][j-1] >= curr and (i, j-1) not in ocean:
                    ocean.add((i, j-1))
                    queue.append((i, j-1))

                # down 
                if j + 1 < len(heights[0]) and heights[i][j+1] >= curr and (i, j+1) not in ocean:
                    ocean.add((i, j+1))
                    queue.append((i, j+1))


        # pacific
        for i in range(len(heights[0])):
            search(0, i, True)
            pacific.add((0, i))

        for i in range(len(heights)):
            search(i, 0, True)
            pacific.add((i, 0))

        # atlantic
        row = len(heights) - 1
        col = len(heights[0]) - 1
        for i in range(len(heights[0])):
            search(row, i, False)
            atlantic.add((row, i))

        for i in range(len(heights)):
            search(i, col, False)
            atlantic.add((i, col))
        
        # take intersect elements
        res = []
        for c in pacific:
            if c in atlantic:
                res.append(c)
        
        return res


        