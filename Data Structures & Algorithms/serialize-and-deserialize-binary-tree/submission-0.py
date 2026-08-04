# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    from collections import deque
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        res = []      
        queue = deque([root])
        
        while queue:
            # check queue val
            node = queue.popleft()
            if node == None:
                res.append("None")
                continue
            else:
                res.append(str(node.val))
    
                # add sub
                if node.left:
                    queue.append(node.left) 
                else:
                    queue.append(None) 

                if node.right:
                    queue.append(node.right) 
                else:
                    queue.append(None) 

        return ",".join(res) # 變成輸出字串 "1,2,3,None,None,4,5"
        # 致命錯誤: return str(self.res) => 把 [1,2,3] 變 "[1,2,3]" where res[0] == "[" 

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        val = data.split(',')  # val = ["1", "2", "3", "None", "None", "4", "5"]
        
        if val[0] == "None":
            return None

        idx = 0
        root = TreeNode(int(val[idx]))
        queue = deque([root])
        idx += 1
        
        while queue:
            node = queue.popleft()
            
            if val[idx] != "None": #左子樹
                node.left = TreeNode(int(val[idx]))
                queue.append(node.left)
            idx += 1 #如果是None直接idx+1, 跳下一個數字

            if val[idx] != "None": #右子樹
                node.right = TreeNode(int(val[idx]))
                queue.append(node.right)
            idx += 1

        return root

"""
千萬不能把 None append 進 queue
queue 永遠不會排空,而且每多一個假節點被 dequeue, idx就加一 就會 out of range
"""









