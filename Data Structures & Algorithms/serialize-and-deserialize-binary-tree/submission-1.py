# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    """
    dfs also work since intermediate string is not checked with the answer
    use preorder since we are starting from the root
    """
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("None")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res) # "1,2,None,None,3,4,5"
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        val = data.split(",")
        self.i = 0

        def dfs():
            if val[self.i] == "None":
                self.i += 1
                return None
            
            root = TreeNode(int(val[self.i]))
            self.i += 1
            
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs() #return 呼叫後結果




