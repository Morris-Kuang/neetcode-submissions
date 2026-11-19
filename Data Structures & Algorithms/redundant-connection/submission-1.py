class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        OPTIMAL: Union Find
        ASK if u, v are connected before they link together?
        1. find(u): find u's connected component (head)
        2. union(u,v): 每個 node 不需要直接知道自己的 root, 只需要知道自己的 parent, 想知道 root 時, 再一路往上找。

        Hardest Part: Union find design
        - Union by Size: 樹高變 O(log n)
        - Path Compression: find(x) 找到 root 時，順便把沿途所有 nodes 的 parent 直接改成 root
        => Path Compression + Union by Size: amortized(N) 趨近 const time

        Time: O(N * α(N))
        - α(N): Inverse Ackermann function, which grows extremely slowly.
        Space: O(N)
        - Parent and size arrays
        """
        parent = [0] * (len(edges) + 1) # index match value

        def union(u, v):
            parent_u = find(u)
            parent_v = find(v)
            
            if parent_u == parent_v:
                return True # cycle is true

            # v combined to u's connection
            parent[parent_v] = parent_u

            return False # cycle is false
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # 把自己直接指向整個 Component 的 Root（最上層祖先）
            return parent[x]
        
        for u, v in edges:
            # set initial
            if parent[u] == 0:
                parent[u] = u
            if parent[v] == 0:
                parent[v] = v
            
            # if connected
            if union(u, v):
                return [u, v]
        
        return []

            
