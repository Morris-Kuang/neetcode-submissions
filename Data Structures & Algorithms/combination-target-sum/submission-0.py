class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Exhausive answer => backtracking

        decision: choose 2 | not choose 2
        choose 2, choose 3 | choose 3, not choose 3
        c2, c3 | c3, c4    | c3, c4  | c4, not choose 4
        ...
        
        base case: when sum > target, or sum == target, or i == n (finish deciding last element)


        Time: O(2^(t/m)) where target / min element 決定最深多深 
        Space: O(t/m) stack depth
        """

        res, sol = [], []
        n = len(nums)

        def backtrack(i, curr_sum):
            # base
            if curr_sum == target:
                res.append(sol.copy())
                return
            
            if curr_sum > target or i == n:
                return
            
            # decision 1: choose smallest element available
            sol.append(nums[i])
            curr_sum += nums[i]
            
            backtrack(i, curr_sum)
            
            curr_sum -= nums[i] #undo
            sol.pop() #undo

            #decision 2: choose to leave blank (proceed next num)
            backtrack(i+1, curr_sum)



        backtrack(0, 0)  # assign i = 0 and curr_sum = 0
        return res

