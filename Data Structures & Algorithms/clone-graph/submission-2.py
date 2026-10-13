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
        dfs recursive -- intuitive approach
        step 1: clone graph using dfs recursive
        step 2: pair graphs using dic
        """
        
        if not node:
            return None

        oldToNew = {}

        # traverse and create copied nodes
        def dfs(curr):
            if curr in oldToNew:
                return oldToNew[curr]
            oldToNew[curr] = Node(curr.val)
            
            for nei in curr.neighbors:
                dfs(nei)

            return oldToNew[curr]
        
        dfs(node) # get the hashmap done

        for old, new in oldToNew.items():
            for nei in old.neighbors:
                new.neighbors.append(oldToNew[nei])

        
        return oldToNew[node]
        