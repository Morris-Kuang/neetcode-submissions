class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        backtracking: O(2^n) for traversal of all combination 
        O(n·2^n) finally since we account for copying solutions
        
        sort first since it 
        - allows correct multiple duplicate removal
        - prune (剪枝) and traverse less cases

        decision - yes or no on traversing that element
        recursive - after choosing candidate[i], backtrack candidate[i+1]
        base case - when sum == target, sum > target, last element
        undo - pop the element we just added

        candidates = [9,2,2,4,6,1,5], target = 8
        candidates = [1,2,2,4,5,6,9], target = 8
        """

        result = []
        solution = [] # holding items
        candidates.sort()

        def backtrack(i, summ):
            # base
            if summ == target: # 放前面因為不希望下面能個先做 就不做這個了
                result.append(solution.copy()) #KEY MISTAKE OFTEN MADE 不能傳還會改的變數
                return
            if i == len(candidates) or summ > target:
                return
            

            # decision - pick
            solution.append(candidates[i])
            backtrack(i+1, summ + candidates[i])  # not summ + candidates[i+1]
            solution.pop()

            # decision - not pick
            """
            the only edge case here: (2,0) (2,2) and not pick does (2,0) again
            let pick finish the case and do not do here
            """
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, summ)  # not pick so do not add candidates[i+1]!!

        backtrack(0, 0)
        return result