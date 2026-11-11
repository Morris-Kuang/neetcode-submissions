from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Optimize!! Use directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] instead of four directional if
        """

        pacific, atlantic = set(), set()

        def search(i, j, paci):
            ocean = pacific if paci else atlantic

            queue = deque([(i, j)])  # put accesible neighbors in
            ocean.add((i, j))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                i, j = queue.popleft()
                curr = heights[i][j]

                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    if (0 <= ni < len(heights) and
                        0 <= nj < len(heights[0]) and
                        (ni, nj) not in ocean and
                        heights[ni][nj] >= curr):

                        ocean.add((ni, nj))
                        queue.append((ni, nj))


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


        