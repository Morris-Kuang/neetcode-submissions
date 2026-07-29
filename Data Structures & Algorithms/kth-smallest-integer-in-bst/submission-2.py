# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        思路: In-order traversal, 用list 存起來
        創一個 inOrder(node) 就把整棵樹排好
        """
        res = []

        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            res.append(node.val)
            inOrder(node.right)
            

        inOrder(root)
        return res[k-1]



            
            








