class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        decision tree: 
        [1] [2] [3]
        [1,2] [1,3] [2,1] [2,3] ... skip self
        [1,2,3] [1,3,2] ... skip self

        backtracking - 
        base: when meet len of [] = len(nums)
        decision: for i in nums, append but skip self if in []
        undo: pop() 
        """

        res, sol = [], []
        n = len(nums)

        def backtrack():
            if len(sol) == n:
                res.append(sol.copy()) #remember!!!
                return
            
            for i in nums:
                if i not in sol:
                    sol.append(i) #decision
                    backtrack()  # recursive
                    sol.pop()  # undo

        backtrack()
        return res