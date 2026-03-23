# https://leetcode.com/problems/find-if-path-exists-in-graph/description/
from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # BFS
        graph = {i: [] for i in range(n)}
        for a, b in edges :
            graph[a].append(b)
            graph[b].append(a)
        
        queue = deque([source])
        visited = set([source])

        while queue:
            node = queue.popleft()

            if node == destination:
                return True
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return False

        # stack DFS
class Solution:
    def 