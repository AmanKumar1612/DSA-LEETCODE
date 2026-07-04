from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Build the adjacency list
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # BFS to find the minimum edge in the connected component of node 1
        min_score = float('inf')
        visited = set([1])
        queue = deque([1])
        
        while queue:
            node = queue.popleft()
            for neighbor, weight in graph[node]:
                # Track the minimum weight seen in this component
                min_score = min(min_score, weight)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score