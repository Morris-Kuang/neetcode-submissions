# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Tricky! Also need to make sure root.right.left > root
        USE boundary method
        - root.right.left: root < node < root.right
        - root.right.right: root.right < node < +inf
        """
        leftV = float("-inf")
        rightV = float("inf")

        def check(node, leftV, rightV):
            if not node:
                return True
            
            if not (node.val > leftV and node.val < rightV):
                return False
            
            left = check(node.left, leftV, node.val)
            right = check(node.right, node.val, rightV)

            return left and right

        return check(root, leftV, rightV)
        