class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        recursive implementing decision making - backtracking
        inside recursion: a. not choose; b. choose that element
        base case: n = len(nums) then append sol to res    
        
        Time: O(n * 2^n) -- copy time per element * total elements
        Space: O(n) since n layers of stack depth
        """



        res, sol = [], []  # res is the returned result, sol is each individual combination to be appended to res
        n = len(nums)

        def backtracking(i):
            # base: make the n + 1 ending case
            if i == n:
                res.append(sol.copy()) #IMPORTANT: NEED TO APPEND A COPY
                return
            
            # not select that layer's element
            backtracking(i+1)

            # adding that layer of element
            sol.append(nums[i])  # make decision
            backtracking(i+1)  # recursion, meet base case
            sol.pop()  # undo decision


        backtracking(0)
        return res

