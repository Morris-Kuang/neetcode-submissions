class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        decision tree - sort first [1,1,2]
        [1] []
        [1,1] [], [1] []
        [1,1,2] [2], [1,2] [2] 
        if same, skip

        base - last element
        """
        
        ans, sol = [], []
        nums.sort()
        n = len(nums)

        def traverse(layer):
            if sol not in ans:
                ans.append(sol.copy())
            
            if layer == n:
                return
                
            # decision 1
            sol.append(nums[layer])
            traverse(layer+1)
            sol.pop()

            # decision 2
            traverse(layer+1)


        
        traverse(0)
        return ans
