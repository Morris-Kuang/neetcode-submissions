"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        dic to create cloned pairing with original
        dfs traversal to link new nodes as old patterns -- recursive
        base: if node is in oldToNew, return its location
        recursive: appending new neighbors

        edge: optional -> consider null as input
        """
        if not node:
            return None
        
        oldToNew = {}

        # traverse and create copied nodes
        def dfs(curr):
            if curr in oldToNew:
                return oldToNew[curr]
            
            copied = Node(curr.val)
            oldToNew[curr] = copied
            for nei in curr.neighbors:
                oldToNew[curr].neighbors.append(dfs(nei))  # node.neighbor 是個 list
                
            
            return copied # 回傳 new node!
        
        dfs(node)
        return oldToNew[node]
 
            



        
