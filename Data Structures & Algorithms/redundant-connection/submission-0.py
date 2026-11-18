class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        brute force: when added the edge, run a dfs to check for cycles
        => O(V * V) since v times of dfs O(V+E) and O(V+E) = O(2V)
        1. Undirected Graph: Adjacency List {1: [], 2: []...}
        2. dfs(start, end) test true / false: answering "Is this graph cyclical?"
        3. 
        """
        adj = {}
        for i in range(1, len(edges)+1): # one additional edge let V = E
            adj[i] = []

        def dfs(node, parent, seen):
            seen.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue

                if nei in seen:
                    return True
                
                if dfs(nei, node, seen):
                    return True
            return False

        
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
            if dfs(e[0], None, set()):
                return e
        
        return[]



