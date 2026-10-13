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
        DFS: iterative approach to create nodes
        dic: pair old addr with new addr
        seen: recording copied nodes
        stack: put pending neighbors to create nodes

        for loop to match them with neighbors

        edge case: null as input
        """
        if not node:
            return None

        oldToNew = {}
        seen = set()
        stack = [node]

        while stack:
            element = stack.pop()
            if element in seen:
                continue
            else:
                for nei in element.neighbors:
                    stack.append(nei)
                oldToNew[element] = Node(element.val)
                seen.add(element)
        
        for old, new in oldToNew.items():
            for nei in old.neighbors:
                new.neighbors.append(oldToNew[nei])
        
        return oldToNew[node]
            



        