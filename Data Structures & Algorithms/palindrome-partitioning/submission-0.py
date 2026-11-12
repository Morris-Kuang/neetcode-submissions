class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Tricky DFS
        Goal: for loop consider all palindrome options from the left (start, end changes)
        whenever it works as a valid palindrome, go dfs(next index)
        Base: whenever last index hits
        """
        res, sol = [], []

        def dfs(start):
            if start == len(s):
                res.append(sol.copy())
                return


            end = start     # very crucial ptr
            
            for i in range(start, len(s)):
                
                # palindrome checking (MUST LEARN)
                substr = s[start:end + 1]
                if substr == substr[::-1]:      # [start:end:step] default tail:head !!
                    sol.append(substr)
                    dfs(end + 1)
                    sol.pop()   # clean up temp sol array 
                
                end += 1  #update end

            return

        dfs(0)
        return res

                

