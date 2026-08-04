# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        dfs to the tail but keep an eye on maximum
        root(中心) is the decision points
        can choose to include max(left, right, 0) where 0 = not choosing any
        """
        self.maxS = root.val

        def traverse(node):
            if not node:
                return 0

            leftMax = traverse(node.left)
            rightMax = traverse(node.right)
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)
            self.maxS = max(self.maxS, node.val+leftMax+rightMax) #update maxS 左加右

            return node.val + max(leftMax,rightMax,0) #對上層node來說，只能收到選單一鍊回傳
        
        traverse(root)
        return self.maxS
