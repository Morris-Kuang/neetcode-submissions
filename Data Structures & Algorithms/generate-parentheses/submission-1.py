class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        decision tree - first put 1 "(", decide between a "(" or a ")"
        "("
        "((" , "()" 
        "(((" "(()" , "()(" "())*" invalid - open < close
        *invalid - open > n
        
        base: if len(sol) == 2n
        """

        ans, sol = [], []
        opn = 1
        close = 0
        sol.append("(") # as a starter

        def backtrack():
            nonlocal opn
            nonlocal close

            if opn < close:
                return
            if opn > n or close > n:
                return
            if len(sol) == 2 * n:
                ans.append("".join(sol.copy()))
                return
            
            # decision 1 - "("
            sol.append("(")
            opn += 1
            backtrack()
            sol.pop()
            opn -= 1

            #decision 2 - ")"
            sol.append(")")
            close += 1
            backtrack()
            sol.pop()
            close -= 1

        
        backtrack()
        return ans

