# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        DFS
        Return Value: # of good nodes
        Base: When meeting None, return 0; when meeting bad node, return 0
        注意與學習：maxNum 不該是 global 而是只跟自己那條線比！
        """

        left = self.check(root.left, root.val)
        right = self.check(root.right, root.val)

        return 1 + right + left


    def check(self, node, maxNum):
        if not node:
            return 0

        good = False
        if node.val >= maxNum:
            good = True

        maxNum = max(node.val, maxNum)
        
        left = self.check(node.left, maxNum)
        right = self.check(node.right, maxNum)

        if good == True:
            return 1 + left + right
        else:
            return left + right


        