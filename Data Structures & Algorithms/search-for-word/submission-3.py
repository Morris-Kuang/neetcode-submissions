class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        start from 0,0
        decision 1: add down one
        decision 2: add right one
        decision 3: add left one
        if meets the word return true
        """

        sol = []
        res = False
        visited = set()

        def backtrack(x, y):
            nonlocal res

            if x == len(board) or y == len(board[0]):
                return
            
            if x < 0 or y < 0:
                return

            if (x,y) in visited:
                return
            
            sol.append(board[x][y])
            visited.add((x,y))

            if "".join(sol) == word:
                res = True
                return            
            
            #decision 1 - include self, go to down one
            backtrack(x+1, y)             
            #decision 2 - include self, go to right one
            backtrack(x, y+1)
            #decision 3 - include self, go to left one
            backtrack(x, y-1)
            #decision 4 - include self, go to upper one
            backtrack(x-1, y)
            
            
            sol.pop()
            visited.remove((x,y))


        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(i,j)
        
        return res
