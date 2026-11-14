from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Initialize n isolated nodes
        vertices = {i: set() for i in range(n)}
        res = n

        for u, v in edges:

            # If they were not connected,
            # adding this edge merges two components
            if not self.isConnected(u, v, vertices):
                res -= 1

            # Add undirected edge
            vertices[u].add(v)
            vertices[v].add(u)

        return res

    def isConnected(self, a, b, vertices):
        if a == b:
            return True

        q = deque([a])
        seen = {a}

        while q:
            v = q.popleft()

            for nei in vertices[v]:
                if nei == b:
                    return True

                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)

        return False